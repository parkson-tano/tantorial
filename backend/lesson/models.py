from django.db import models
from accounts.models import *
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Progression(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, blank=True, null=True)
    publish = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='chapter', blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    progression = models.ForeignKey(Progression, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='lesson', blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Competence(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=256, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title