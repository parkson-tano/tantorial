from django.contrib import admin
from .models import *
# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question

admin.site.register((TeacherAssessment, Question, StudentMark, StudentQuestion))

@admin.register(AssessmentType)
class AssessmentTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
