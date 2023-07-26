from pyexpat import model
from random import choices
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from subsystem.models import Subsystem, Subject, ClassRoom
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import TeacherProfile, StudentProfile, GuardianProfile, SchoolProfile
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    username = models.CharField(
        max_length=20, blank=True, null=True, unique=False)
    account_type = models.CharField(
        max_length=32, null=True, blank=True)
    role = models.CharField(max_length=32, null=True, blank=True)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    suspended = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
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
        elif instance.account_type == 'guardian':
            GuardianProfile.objects.create(user=instance)
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
    elif instance.account_type == 'guardian':
        instance.guardianprofile.save()
    else:
        pass
