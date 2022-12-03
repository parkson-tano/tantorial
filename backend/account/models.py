from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .utils import user_profile_path
from subsystem.models import Subsystem, Subject, ClassRoom
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from profiles.models import *
# Create your models here.

ACCOUNT_TYPE = (
    ('student', 'Student'),
    ('parent', 'Parent'),
    ('teacher', 'Teacher'),
    ('school', 'School'),
)

RELATION = (
    ('mother', 'Mother'),
    ('father', 'Father'),
    ('guardian', 'Guardian')
)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        max_length=20, blank=True, null=True, unique=False)
    phone_number = models.CharField(max_length=24, unique=True)
    account_type = models.CharField(
        max_length=32, choices=ACCOUNT_TYPE, null=True, blank=True)
    code = models.CharField(max_length=16, null=True, blank=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return "{}".format(self.email)



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.account_type == 'student':
            StudentProfile.objects.create(user=instance)
        elif instance.account_type == 'school':
            SchoolProfile.objects.create(user=instance)
        elif instance.account_type == 'teacher':
            TeacherProfile.objects.create(user=instance)
        elif instance.account_type == 'parent':
            ParentProfile.objects.create(user=instance)
        else:
            pass


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.account_type == 'student':
        instance.studentprofile.save()
    elif instance.account_type == 'school':
        instance.schoolprofile.save()
    elif instance.account_type == 'teacher':
        instance.teacherprofile.save()
    elif instance.account_type == 'parent':
        instance.parentprofile.save()
    else:
        pass
