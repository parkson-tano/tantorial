from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from subsystem.models import Subsystem, Subject, ClassRoom
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class SchoolProfile(models.Model):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=56)
    subsystem = models.ForeignKey(
        Subsystem, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='schoolprofile/', default="defaultuserprofile.svg")
    motto = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.school_name:
            return self.school_name
        return self.user.email


class TeacherProfile(models.Model):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
    school_name = models.ForeignKey(
        SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    subsystem = models.ForeignKey(
        Subsystem, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'Male'), ('female', 'female')), null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='teacherprofile/', default="defaultuserprofile.svg")
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
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class StudentProfile(models.Model):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE, related_name='student_profile')
    school = models.ForeignKey(
        SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'Male'), ('female', 'female')), null=True, blank=True)
    subsystem = models.ForeignKey(
        Subsystem, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='studentprofile/', default="defaultuserprofile.svg")
    student_class = ChainedForeignKey(ClassRoom,
                                      chained_field="subsystem",
                                      chained_model_field="subsystem",
                                      show_all=False,
                                      auto_choose=True,
                                      sort=True,
                                      null=True,
                                      blank=True
                                      )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class ParentProfile(models.Model):
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE,  related_name='parent_profile')
    date_created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(
        upload_to='parentprofile/', default="defaultuserprofile.svg")
    def __str__(self):
        return f'{self.child.first_name} parent'


class ParentStudent(models.Model):
    parent = models.ForeignKey( 'account.User', on_delete=models.CASCADE, related_name='parent')
    student = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, related_name='student')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.parent} and {self.student}'
