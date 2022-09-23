from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .utils import user_profile_path
# Create your models here.

ACCOUNT_TYPE = (
    (0, 'student'),
    (1, 'parent'),
    (2, 'school'),
    (4, 'teacher'),
    (5, 'admin'),
)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=24)
    profile_pic = models.ImageField(upload_to=user_profile_path, default="images/defaults/defaultuserprofile.svg")
    student_class = models.CharField(max_length=32, null=True, blank=True)
    account_type = models.CharField(
        max_length=32, choices=ACCOUNT_TYPE, default='student')
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return "{}".format(self.email)
