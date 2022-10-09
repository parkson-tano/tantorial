from email.policy import default
from pydoc import describe
from django.db import models
from accounts.models import *
from subsystem.models import *
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey
from autoslug import AutoSlugField
# Create your models here.

class AssessmentType(models.Model):
	title = models.CharField(max_length=256)
	description = models.CharField(max_length = 256)
	slug = AutoSlugField(populate_from='title')
	def __str__(self):
		return self.title

class TeacherAssessment(models.Model):
	teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
	assessment_type = models.ForeignKey(AssessmentType, on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
	assessment_class = ChainedForeignKey(
        ClassRoom,
        chained_field="subsystem",
        chained_model_field="subsystem",
        show_all=False,
        auto_choose=True,
        sort=True,
        null = True,
        blank = True
        )
	assessment_subject = ChainedForeignKey(
        Subject,
        chained_field="subsystem",
        chained_model_field="subsystem",
        show_all=False,
        auto_choose=True,
        sort=True,
        null = True,
        blank = True
        )
	slug = AutoSlugField(populate_from = 'title')
	publish = models.BooleanField(default=False)
	student_count = models.IntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + str(self.id)


class Question(models.Model):
	assessment = models.ForeignKey(TeacherAssessment, on_delete=models.CASCADE)
	question_no = models.IntegerField(blank=True, null=True)
	question = models.TextField(blank=True, null=True)
	answer_a = models.TextField(blank=True, null=True)
	answer_b = models.TextField(blank=True, null=True)
	answer_c = models.TextField(blank=True, null=True)
	answer_d = models.TextField(blank=True, null=True)
	correct_answer = models.CharField(max_length=15, choices = (
		('a', 'a'), ('b', 'b'), ('c','c'), ('d', 'd')
		), blank=True, null=True)
	explanation = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'question {self.id} for {self.assessment}'


class StudentMark(models.Model):
	student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
	test = models.ForeignKey(TeacherAssessment, on_delete=models.CASCADE)
	marks = models.IntegerField(default=0)
	timer = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	percentage = models.FloatField(default=0)
	passed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.student} grade for {self.test}'

class StudentQuestion(models.Model):
	student = models.ForeignKey(StudentMark, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	graded = models.BooleanField(default = False)
	passed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.student} for {self.question}'