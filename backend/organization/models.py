from django.db import models
from django.contrib.auth import get_user_model
from account.types import UserType
from django.utils.translation import gettext as _

User: UserType = get_user_model()
ORGANIZATION_CHOICE = (
        (0, _("School Organization")),
        (1, _("Tutorship Organization")),
    )


class Organization(models.Model):
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    type = models.CharField(max_length=50, choices=ORGANIZATION_CHOICE)
    phone = models.CharField(max_length=20)


class ClassRoom(models.Model):
    name = models.CharField
    created = models.DateField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    
class Arm(models.Model):
    arm_name = models.CharField(max_length=100)
    ClassRoom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="arms")
    created = models.DateTimeField(auto_now_add=True)
    teachers = models.ManyToManyField("Teacher")


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Student(models.Model):
    # Am using a many to many relationship here instead of a foreign key because
    # user can belong to multiple schools. For example a student might belong to 
    # a school but also be a student of some tutorship organization
    classrooms = models.ManyToManyField(ClassRoom)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
