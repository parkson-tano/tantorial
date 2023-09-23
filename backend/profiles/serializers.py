from rest_framework import serializers
from .models import *

class SchoolProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolProfile
        fields = '__all__'

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class GuardianProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianProfile
        fields = '__all__'

class StudentGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGuardian
        fields = '__all__'

class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        fields = '__all__'

class SubjectTeacherSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset = Subject.objects.all())
    class_room = serializers.PrimaryKeyRelatedField(queryset = ClassRoom.objects.all())
    
    class Meta:
        model = SubjectTeacher
        fields = '__all__'

class ClassTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTeacher
        fields = '__all__'

