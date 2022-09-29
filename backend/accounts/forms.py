from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
# from bootstrap_datepicker_plus import DatePickerInput


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "email", 'phone_number', 'subsystem','student_class', "password1", "password2"]

class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())