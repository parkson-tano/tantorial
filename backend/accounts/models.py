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


class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class SubjectAssignment(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_assigned = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher} - {self.subject} - {self.class_assigned}'





class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    first_name = models.CharField(max_length=56, null=True, blank=True)
    last_name = models.CharField(max_length=56, null=True, blank=True)
    username = models.CharField(max_length=35, null=True, unique=True)
    account_type = models.CharField(
        max_length=32, null=True, blank=True, choices=(('student', 'Student'), ('teacher', 'Teacher'), ('parent', 'Parent'), ('school', 'School')))
    role = models.CharField(max_length=32, null=True, blank=True, 
                            choices=((None, None), 
                                     ('supervisor', 'supervisor'),
                                     ('coordinator', 'coordinator'),
                                     ('member', 'member'),
                                     ('focal-point', 'focal-point'),
                                     ('class-supervisor', 'class-supervisor')
                                     )
                            )
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    suspended = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    archived =  models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete = models.CASCADE, null = True, blank = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

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



class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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


class Permissions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_permissions = models.ManyToManyField(Class)
    subject_permissions = models.ManyToManyField(Subject)
    edit_profile = models.BooleanField(default=False)
    delete_profile = models.BooleanField(default=False)
    create_profile = models.BooleanField(default=False)
    edit_class = models.BooleanField(default=False)
    delete_class = models.BooleanField(default=False)
    create_class = models.BooleanField(default=False)
    edit_subject = models.BooleanField(default=False)
    delete_subject = models.BooleanField(default=False)
    create_subject = models.BooleanField(default=False)
    edit_assessment = models.BooleanField(default=False)
    delete_assessment = models.BooleanField(default=False)
    create_assessment = models.BooleanField(default=False)
    edit_lesson = models.BooleanField(default=False)
    delete_lesson = models.BooleanField(default=False)
    create_lesson = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user 
