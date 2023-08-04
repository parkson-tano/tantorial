from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(SchoolProfile)
admin.site.register(GuardianProfile)
admin.site.register(StudentGuardian)
admin.site.register(StudentSubject)
admin.site.register(SubjectTeacher)
admin.site.register(ClassTeacher)
