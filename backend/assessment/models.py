from django.db import models
from accounts.models import *
from subsystem.models import *
from lesson.models import *
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class AssessmentType(models.Model):
	title = models.CharField(max_length=256)

	def __str__(self):
		return self.title

class TeacherAssessment(models.Model):
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)
	assessment_type = models.ForeignKey(AssessmentType, on_delete=models.CASCADE)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
	question_type = models.CharField(max_length=256, blank=True, null=True)
	title = models.CharField(max_length=256)
	assessment_class = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
	taken_count = models.IntegerField(default=0)
	complete_count = models.IntegerField(default=0)
	taken_by = models.ManyToManyField(StudentProfile, blank=True, related_name='taken_by')
	publish = models.BooleanField(default=False)
	dateline = models.DateTimeField(blank=True, null=True)
	objective = models.TextField(blank=True, null=True)
	competence = models.TextField(blank=True, null=True)
	deleted = models.BooleanField(default=False)
	archived =  models.BooleanField(default=False)
	date_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)    


	def __str__(self):
		return self.title
	
class AssessmentQuestion(models.Model):
	assessment = models.ForeignKey(TeacherAssessment, on_delete=models.CASCADE)
	question = models.TextField(blank=True, null=True)
	answer_a = models.TextField(blank=True, null=True)
	answer_b = models.TextField(blank=True, null=True)
	answer_c = models.TextField(blank=True, null=True)
	answer_d = models.TextField(blank=True, null=True)
	correct_answer = models.CharField(max_length=15, blank=True, null=True)
	seen_count = models.IntegerField(default=0)
	answered_count = models.IntegerField(default=0)
	answered_by = models.ManyToManyField(StudentProfile, blank=True, related_name='answered_by')
	explanation = models.TextField(null=True, blank=True)
	deleted = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	date_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'question {self.id} for {self.assessment}'

class AssessmentTarget(models.Model):
	assessment = models.ForeignKey(TeacherAssessment, on_delete=models.CASCADE)
	classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
	criteria = models.CharField(max_length=256, blank=True, null=True)
	target = models.ManyToManyField(StudentProfile, blank=True, related_name='target')
	deleted = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	date_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'target {self.id} for {self.assessment}'

class StudentMark(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	test = models.ForeignKey(TeacherAssessment, on_delete=models.CASCADE)
	marks = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	passed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.student} grade for {self.test}'

class StudentAnswer(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE)
	student_answer = models.CharField(max_length=15, blank=True, null=True)
	deleted = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	passed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.student} for {self.question}'