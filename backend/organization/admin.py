from django.contrib import admin
from .models import Teacher, Student, Organization, ClassRoom, Arm
# Register your models here.

# admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(Arm)
admin.site.register(Organization)
admin.site.register(ClassRoom)
