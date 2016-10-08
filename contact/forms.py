from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'required': 'true', 'class': 'form-control col-md-7 col-md-offset-0', 'placeholder': 'Name'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'required': 'true', 'class': 'form-control col-md-7 col-md-offset-0', 'placeholder': 'E-Mail'}))

    message = forms.CharField(
        widget=Textarea(attrs={'required': 'true', 'class': 'form-control col-md-11 col-md-offset-0', 'placeholder': 'Message', 'rows':8}))