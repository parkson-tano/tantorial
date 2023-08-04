from django.db import models
from subsystem.models import *
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class SchoolProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=56)
    school_address = models.CharField(max_length=256, null=True, blank=True)
    school_logo = models.ImageField(
        upload_to='schoolprofile/', default="images/defaults/defaultschoollogo.svg")
    school_type = models.CharField(max_length=56, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True)
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True)
    sub_division = models.ForeignKey(
        SubDivision, on_delete=models.SET_NULL, null=True, blank=True)
    locality = models.ForeignKey(
        Locality, on_delete=models.SET_NULL, null=True, blank=True)
    subsystem = models.ForeignKey(
        Subsystem, on_delete=models.SET_NULL, null=True, blank=True)
    motto = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.school_name:
            return self.school_name
        return self.user.email


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(
        SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    subsystem = models.ForeignKey(
        Subsystem, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=56, null=True, blank=True)
    last_name = models.CharField(max_length=56, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=56, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='teacherprofile/', default="images/defaults/defaultteacherprofile.svg")
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class SubjectTeacher(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher.first_name + ' ' + self.teacher.last_name


class ClassTeacher(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    class_room = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher.first_name + ' ' + self.teacher.last_name


class GuardianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=56, null=True, blank=True)
    last_name = models.CharField(max_length=56, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='guardianprofile/', default="images/defaults/defaultguardianprofile.svg")
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(
        SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    student_class = models.ForeignKey(
        ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, blank=True)
    subsystem = models.ForeignKey(
        Subsystem, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=56, null=True, blank=True)
    last_name = models.CharField(max_length=56, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=56, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='studentprofile/', default="images/defaults/defaultstudentprofile.svg")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class StudentGuardian(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guardian = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='guardian')
    relationship = models.CharField(max_length=56, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name + ' ' + self.guardian.first_name + ' ' + self.guardian.last_name


class StudentSubject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name + ' ' + self.subject.title
