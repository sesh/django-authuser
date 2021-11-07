from django import forms

from .models import User


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        value = self.cleaned_data["email"].strip()
        if User.objects.filter(email=value):
            raise forms.ValidationError("That email is already in user")
        return value

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["password_again"]:
            raise forms.ValidationError("The passwords you entered did not match")
