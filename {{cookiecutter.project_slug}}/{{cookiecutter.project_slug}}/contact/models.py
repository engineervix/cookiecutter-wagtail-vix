from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey

# from wagtail.images.edit_handlers import ImageChooserPanel
from phonenumber_field.modelfields import PhoneNumberField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    # FieldRowPanel,
    InlinePanel,
    # MultiFieldPanel,
)

# from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page

# from wagtail.snippets.models import register_snippet
from wagtail.search import index

# from djexmo import send_message


# @register_snippet
# class ContactNumber(models.Model):
#     phone_number = PhoneNumberField()

#     panels = [
#         FieldPanel('phone_number'),
#     ]

#     def __str__(self):
#         return str(self.phone_number)

#     class Meta:
#         verbose_name_plural = 'Contact Numbers'


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(blank=True)

    panels = [FieldPanel("phone_number")]

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        abstract = True


class EmailAddress(models.Model):
    email_address = models.EmailField(blank=True)

    panels = [FieldPanel("email_address")]

    def __str__(self):
        return self.email_address

    class Meta:
        abstract = True


class ContactPagePhoneNumber(Orderable, PhoneNumber):
    page = ParentalKey(
        "ContactPage", on_delete=models.CASCADE, related_name="phone_numbers"
    )


class ContactPageEmailAddress(Orderable, EmailAddress):
    page = ParentalKey(
        "ContactPage", on_delete=models.CASCADE, related_name="email_addresses"
    )


class ContactPage(Page):
    address = models.TextField(blank=True)

    def get_phone_numbers(self):
        all_phone_numbers = self.phone_numbers.all()
        phone_numbers_list = []
        for number in all_phone_numbers:
            phone_numbers_list.append(number)
        return phone_numbers_list

    def get_email_addresses(self):
        all_email_addresses = self.email_addresses.all()
        email_address_list = []
        for email in all_email_addresses:
            email_address_list.append(email)
        return email_address_list

    search_fields = Page.search_fields + [index.SearchField("address")]

    content_panels = Page.content_panels + [
        FieldPanel("address"),
        InlinePanel("phone_numbers", label="Phone Numbers"),
        InlinePanel("email_addresses", label="Email Addresses"),
    ]

    template = "contact/contact.html"

    def serve(self, request):
        from .forms import ContactUs

        if request.method == "POST":
            contact_us_form = ContactUs(request.POST)
            if contact_us_form.is_valid():
                """
                contact_data = contact_us_form.save()
                return render(request, 'contact/thankyou.html', {
                    'page': self,
                    'contact_data': contact_data,
                })
                """
                subject = contact_us_form.cleaned_data["subject"]
                from_email = contact_us_form.cleaned_data["email"]
                # phone_number = str(contact_us_form.cleaned_data['phone'])
                recipient = contact_us_form.cleaned_data["name"]
                # sms_recipient = recipient.split(' ', 1)[0]
                message = (
                    "<strong>The Message:</strong> <br> <hr> "
                    + contact_us_form.cleaned_data["message"]
                    + "<hr> <br> <br><strong>Sent by:</strong> "
                    + contact_us_form.cleaned_data["name"]
                    + "<br> <br><strong>Phone Number:</strong> "
                    + str(contact_us_form.cleaned_data["phone"])
                    + "<br> <br><strong>Email Adddress:</strong> "
                    + contact_us_form.cleaned_data["email"]
                )
                thank_u_msg = f'Dear <strong>{recipient}</strong>,<br> <br> Thank you for getting in touch via our website!<br> <br> We appreciate you contacting us concerning <strong>{subject}</strong>. We will do our best to get back to you shortly.<br> <br> Thanks in advance for your patience.<br> <br> Have a blessed day!<br> <br> Best Regards,<br> <br> <hr> <a href="https://{{cookiecutter.domain_name}}">{{cookiecutter.project_name}}</a> <hr>'
                try:
                    send_mail(
                        subject="New Website Contact Form Message | " + subject,
                        message=message,
                        from_email="{{cookiecutter.project_name}} Website <hello@{{cookiecutter.domain_name}}>",
                        recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
                        html_message=message,
                        # html_message='<p>Hello Rock stars!</p>',
                        # fail_silently=False
                    )
                    send_mail(
                        subject="{{cookiecutter.project_name}} » Thank you for getting in touch with us",
                        message=thank_u_msg,
                        from_email="{{cookiecutter.project_name}} <me@{{cookiecutter.domain_name}}>",
                        recipient_list=[from_email],
                        html_message=thank_u_msg,
                        # html_message='<p>Hello Rock stars!</p>',
                        # fail_silently=False
                    )
                except BadHeaderError:
                    # return HttpResponse('Invalid header found.')
                    # messages.error(request, 'span class="glyphicon glyphicon-hand-right"></span> <strong>Error Message</strong> <hr class="message-inner-separator"> <p>Invalid header found.</p>')
                    messages.error(
                        request,
                        "Oops! Something went wrong, please try again and ensure you correctly fill in the contact form.",
                    )
                # return redirect('success')
                # messages.success(request, 'span class="glyphicon glyphicon-ok"></span> <strong>Message Successfully Sent!</strong> <hr class="message-inner-separator"> <p>Thank you for getting in touch with us, we will get back to you in a jiffy. Have a pleasant day!</p>')
                messages.success(
                    request,
                    "Thank you for getting in touch with us, we will get back to you soon. Have a blessed day!",
                )
                # send_message(frm=settings.NEXMO_DEFAULT_FROM, to=phone_number, text=f'Thanks {sms_recipient} for contacting us,we\'ll be in touch soon.Grace & Peace')
                contact_us_form = ContactUs()
        else:
            contact_us_form = ContactUs()

        return render(
            request, ContactPage.template, {"page": self, "form": contact_us_form}
        )

    # Specifies parent to ContactPage as being HomeeIndexPage
    parent_page_types = ["home.HomePage"]

    # Specifies what content types can exist as children of ArticlePage.
    # Empty list means that no child content types are allowed.
    subpage_types = []
