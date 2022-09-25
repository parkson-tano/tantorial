from cProfile import label
from django import forms
from .models import *

from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()
# from bootstrap_datepicker_plus import DatePickerInput


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["account_type","first_name", "last_name", "email",'phone_number', "password", "password_confirm"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is already in use')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('this username is already in use')
        return username

    def clean_password_confirm(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_confirm')

        if ((pass1 and pass2) and (pass1 != pass2)):
            forms.ValidationError("Password don't match")
        return pass2
