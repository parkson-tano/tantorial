from django.contrib import admin
from .models import *
# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question

admin.site.register((AssessmentType, TeacherAssessment, Question, StudentMark, StudentQuestion))