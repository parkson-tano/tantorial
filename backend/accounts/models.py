from pyexpat import model
from random import choices
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from subsystem.models import Subsystem, Subject, ClassRoom
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import TeacherProfile, StudentProfile, GuardianProfile, SchoolProfile
import random
import string
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    first_name = models.CharField(max_length=56, null=True, blank=True)
    last_name = models.CharField(max_length=56, null=True, blank=True)
    username = models.CharField(max_length=35, null=True, unique=True)
    account_type = models.CharField(
        max_length=32, null=True, blank=True, choices=(('student', 'Student'), ('teacher', 'Teacher'), ('parent', 'Parent'), ('school', 'School')))
    role = models.CharField(max_length=32, null=True, blank=True, )
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    suspended = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    archived =  models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return "{}".format(self.email)

    def _generate_random_username(self):
        # Generate a random 4-digit number
        random_number = ''.join(random.choices(string.digits, k=7))

        # Map role to abbreviation
        account_abbreviations = {
            'student': 'STD',
            'teacher': 'TEA',
            'parent': 'PAR',
            'school': 'SCH',
        }

        account_type_abbr = account_abbreviations.get(
            self.account_type.lower(), 'OTH')

        # Format the username as "TAN/1234/role"
        return f"TAN-{random_number}-{account_type_abbr}"

    def save(self, *args, **kwargs):
        if not self.username:
            username = self._generate_random_username()
            while User.objects.filter(username=username).exists():
                username = self._generate_random_username()
            self.username = username
        super().save(*args, **kwargs)


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
