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
                  "email", 'phone_number', "password1", "password2"]
