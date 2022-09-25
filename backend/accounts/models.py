from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .utils import user_profile_path
from subsystem.models import *
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

ACCOUNT_TYPE = (
    ('student', 'Student'),
    ('parent', 'Parent'),
    ('teacher', 'Teacher'),
    ('school', 'School'),
)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=20, blank=True, null=True, unique=False)
    phone_number = models.CharField(max_length=24)
    profile_pic = models.ImageField(upload_to=user_profile_path, default="images/defaults/defaultuserprofile.svg")
    account_type = models.CharField(
        max_length=32, choices=ACCOUNT_TYPE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return "{}".format(self.email)


class SchoolProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=56)
    profile_pic = models.ImageField(upload_to='schoolprofile/',default="images/defaults/defaultuserprofile.svg")
    motto = models.CharField(max_length=256, null=True, blank=True)
    code = models.CharField(max_length=16)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.school_name:
            return self.school_name
        return self.user.email

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE, null=True, blank=True )
    teacher_class = ChainedManyToManyField(ClassRoom, 
        chained_field="subsystem",
        chained_model_field="subsystem"
        )
    subject = ChainedForeignKey(
        Subject,
        chained_field="subsystem",
        chained_model_field="subsystem",
        show_all=False,
        auto_choose=True,
        sort=True,
        null = True,
        blank = True
        )
    code = models.CharField(max_length=16)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, 
        null=True, blank=True, related_name='student_parent')
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE, null=True, blank=True )
    student_class = ChainedForeignKey(ClassRoom, 
        chained_field="subsystem",
        chained_model_field="subsystem",
        show_all=False,
        auto_choose=True,
        sort=True,
        null = True,
        blank = True
        )
    code = models.CharField(max_length=16)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.account_type == 'student':
            StudentProfile.objects.create(user=instance)
        elif instance.account_type == 'school':
            SchoolProfile.objects.create(user=instance)
        elif instance.account_type == 'teacher':
            TeacherProfile.objects.create(user=instance)
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
    else:
        pass