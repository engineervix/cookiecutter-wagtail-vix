# from django.urls import reverse

from captcha.fields import ReCaptchaField
from django import forms

# import floppyforms as forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import FormActions
from intl_tel_input.widgets import IntlTelInputWidget


class ContactUs(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Name"}),
        required=True,
        max_length=255,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "email@example.com"}),
        required=True,
    )
    phone = forms.CharField(
        widget=IntlTelInputWidget(default_code="zm", preferred_countries=["za", "na"])
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Subject"}),
        required=True,
        max_length=255,
    )
    message = forms.CharField(
        required=True,
        max_length=1000,
        widget=forms.Textarea(attrs={"placeholder": "Message"}),
    )
    captcha = ReCaptchaField()
