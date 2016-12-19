from django import forms
from django.forms import ModelForm

from authentication.models import User


class UserForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")
        return self.cleaned_data


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label=("Email address"), max_length=254)


class SetPasswordForm(forms.Form):
    """
    Form to let the user change their password
    """
    new_password = forms.CharField(label=("New password"), widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label=("New password confirmation"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(SetPasswordForm, self).clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_new_password")

        if password != confirm_password:
            raise forms.ValidationError(
                    "password and confirm_password does not match"
            )
        return self.cleaned_data
