from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AssessmentQuestion)
admin.site.register(AssessmentTarget)
admin.site.register(StudentMark)
admin.site.register(StudentAnswer)
admin.site.register(TeacherAssessment)
admin.site.register(AssessmentType)
