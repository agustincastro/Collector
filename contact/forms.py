from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'required': 'true', 'placeholder':'Name'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'required': 'true', 'placeholder': 'E-Mail'}))

    message = forms.CharField(
        widget=Textarea(attrs={'required': 'true', 'placeholder': 'Message', 'rows':8}))