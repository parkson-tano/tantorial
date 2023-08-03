from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class SchoolProfileViewSet(viewsets.ModelViewSet):
    queryset = SchoolProfile.objects.all()
    serializer_class = SchoolProfileSerializer
class GuardianProfileViewSet(viewsets.ModelViewSet):
    queryset = GuardianProfile.objects.all()
    serializer_class = GuardianProfileSerializer

class StudentGuardianViewSet(viewsets.ModelViewSet):
    queryset = StudentGuardian.objects.all()
    serializer_class = StudentGuardianSerializer

class StudentSubjectViewSet(viewsets.ModelViewSet):
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer

class SubjectTeacherViewSet(viewsets.ModelViewSet):
    queryset = SubjectTeacher.objects.all()
    serializer_class = SubjectTeacherSerializer

class ClassTeacherViewSet(viewsets.ModelViewSet):
    queryset = ClassTeacher.objects.all()
    serializer_class = ClassTeacherSerializer


class SchoolProfileUpdateAPIView(viewsets.ModelViewSet):
    serializer_class = SchoolProfileSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return SchoolProfile.objects.filter(user=user_id)
    
class TeacherProfileUpdateAPIView(viewsets.ModelViewSet):
    serializer_class = TeacherProfileSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return TeacherProfile.objects.filter(user=user_id)
    
class StudentProfileUpdateAPIView(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return StudentProfile.objects.filter(user=user_id)
    

class GuardianProfileUpdateAPIView(viewsets.ModelViewSet):
    serializer_class = GuardianProfileSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return GuardianProfile.objects.filter(user=user_id)

