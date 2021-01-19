from django.forms import ModelForm
from django.forms import Textarea
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
