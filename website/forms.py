from dataclasses import fields
import email
from email import message
from unicodedata import name
from django import forms
from website.models import *
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class Contact_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = NewsLetter
        fields = '__all__'
