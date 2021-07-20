import pytest

from captcha.client import RecaptchaResponse
from django.apps import apps
from django.core import mail
from django.core.mail import BadHeaderError, send_mail
from wagtail.core.models import Page

from {{cookiecutter.project_slug}}.contact.apps import ContactConfig
from {{cookiecutter.project_slug}}.contact.forms import ContactUs

from faker import Faker
from faker_e164.providers import E164Provider  # E164 Phone Numbers

fake = Faker()
fake.add_provider(E164Provider)

CONTACT_FORM_TEST_DATA = [
    (
        fake.name(),
        fake.email(),
        fake.e164(region_code="US", valid=True, possible=True),
        fake.sentence(),
        fake.paragraph(),
        "PASSED",
        True,
    ),
    (
        fake.name(),
        fake.email(),
        fake.e164(region_code="CA", valid=True, possible=True),
        fake.sentence(),
        fake.paragraph(),
        "PASSED",
        True,
    ),
]

CONTACT_FORM_IDS = [f"contact: {str(data[0])}" for data in CONTACT_FORM_TEST_DATA]
CONTACT_POST_IDS = [f"contact_POST: {str(data[0])}" for data in CONTACT_FORM_TEST_DATA]
BADHEADERERROR_IDS = [
    f"BadHeaderError: {str(data[0])}" for data in CONTACT_FORM_TEST_DATA
]


@pytest.mark.django_db
def test_contact_page(client):
    """Test Rendering of Contact Page"""
    live_pages = Page.objects.live()
    contact_page = live_pages.get(title="Contact")
    response = client.get(contact_page.get_url())

    assert response.status_code == 200
    assert contact_page.get_url() == "/contact/"
    assert "contact/contact.html" in [t.name for t in response.templates]
    assert b"Welcome to the {{cookiecutter.project_name}} Contact Page" in response.content
    assert contact_page.specific.address is not None
    assert contact_page.specific.address.encode() in response.content
    assert contact_page.specific.phone_numbers.all().count() == 2
    assert contact_page.specific.email_addresses.all().count() == 2


@pytest.mark.parametrize(
    "name, email, phone, subject, message, captcha, validity",
    CONTACT_FORM_TEST_DATA,
    ids=CONTACT_FORM_IDS,
)
def test_contact_form(mocker, name, email, phone, subject, message, captcha, validity):
    """Contact Form Tests at lower level"""
    mocker.patch("captcha.fields.client.submit")
    mocker.return_value = RecaptchaResponse(is_valid=True)
    form = ContactUs(
        {
            "name": name,
            "email": email,
            "phone": phone,
            "subject": subject,
            "message": message,
            "g-recaptcha-response": captcha,
        }
    )

    assert form.is_valid() is validity


@pytest.mark.parametrize(
    "name, email, phone, subject, message, captcha, validity",
    CONTACT_FORM_TEST_DATA,
    ids=CONTACT_POST_IDS,
)
@pytest.mark.django_db
def test_contact_form_posts(
    client, mocker, name, email, phone, subject, message, captcha, validity
):
    """Contact Form Tests on the template"""
    mocker.patch("captcha.fields.client.submit")
    mocker.return_value = RecaptchaResponse(is_valid=True)

    response = client.post(
        "/contact/",
        {
            "name": name,
            "email": email,
            "phone": phone,
            "subject": subject,
            "message": message,
            "g-recaptcha-response": captcha,
        },
        follow=True,
    )

    assert response.status_code == 200

    # check that emails were sent
    assert len(mail.outbox) == 2
    assert f"<hr> <br> <br><strong>Sent by:</strong> {name}" in mail.outbox[0].body
    assert f"Dear <strong>{name}</strong>" in mail.outbox[1].body

    # you can check for other mail parameters
    # assert mail.outbox[0].subject == 'Subject here'
    # assert mail.outbox[0].from_email == 'from@example.com'
    # assert mail.outbox[0].to == ['to@example.com']


@pytest.mark.parametrize(
    "name, email, phone, subject, message, captcha, validity",
    CONTACT_FORM_TEST_DATA,
    ids=BADHEADERERROR_IDS,
)
@pytest.mark.django_db
def test_send_mail_bad_header_error(
    client, mocker, name, email, phone, subject, message, captcha, validity
):
    """Contact Form: we raise a BadHeaderError when sending mail"""

    # Empty the test outbox before we proceed
    mail.outbox = []

    mocker.patch(
        "captcha.fields.client.submit", return_value=RecaptchaResponse(is_valid=True)
    )
    # mocker.patch('django.core.mail.send_mail', autospec=True, side_effect=BadHeaderError)
    mocker.patch(
        "{{cookiecutter.project_slug}}.contact.models.send_mail", autospec=True, side_effect=BadHeaderError()
    )

    response = client.post(
        "/contact/",
        {
            "name": name,
            "email": email,
            "phone": phone,
            "subject": subject,
            "message": message,
            "g-recaptcha-response": captcha,
        },
        follow=True,
    )

    assert response.status_code == 200

    # check that emails were not sent (due to BadHeaderError)
    assert len(mail.outbox) == 0

    # get message from context and check that expected text is there
    message = list(response.context.get("messages"))[0]
    assert message.tags == "error"
    assert "Oops! Something went wrong, please try again" in message.message


@pytest.mark.django_db
def test_contact_app():
    assert ContactConfig.name == "{{cookiecutter.project_slug}}.contact"
    assert apps.get_app_config("contact").name == "{{cookiecutter.project_slug}}.contact"
