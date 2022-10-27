from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from accounts.models import *
from subsystem.models import *

User = get_user_model()
# Create your models here.

class Chapter(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    objective = models.TextField(null = True, blank = True)
    subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
    chapter_class = ChainedForeignKey(
        ClassRoom,
        chained_field="subsystem",
        chained_model_field="subsystem",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True
    )
    chapter_subject = ChainedForeignKey(
        Subject,
        chained_field="subsystem",
        chained_model_field="subsystem",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True
    )
    slug = AutoSlugField(populate_from='title')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    content = models.TextField()
    file = models.FileField(upload_to = 'lesson_file', null = True, blank =True)
    objective = models.TextField(null = True, blank = True)
    competence_1 = models.CharField(max_length = 256, null = True, blank = True)
    competence_2 = models.CharField(max_length = 256, null = True, blank = True)
    competence_3 = models.CharField(max_length = 256, null = True, blank = True)
    competence_4 = models.CharField(max_length = 256, null = True, blank = True)
    competence_5 = models.CharField(max_length = 256, null = True, blank = True)
    competence_6 = models.CharField(max_length = 256, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    publish = models.BooleanField(default = False)
    def __str__(self):
        return self.title