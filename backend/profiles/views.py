from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.query_params.get('user')

        if user is not None:
            queryset =  queryset.filter(user=user)
        return queryset

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.query_params.get('user')

        if user is not None:
            queryset =  queryset.filter(user=user)
        return queryset

class SchoolProfileViewSet(viewsets.ModelViewSet):
    queryset = SchoolProfile.objects.all()
    serializer_class = SchoolProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        subsystem = self.request.query_params.get('subsystem', None)
        user = self.request.query_params.get('user', None)

        if user is not None:
            return queryset.filter(user = user)

        if subsystem is not None:
            return queryset.filter(subsystem=subsystem)
        else:
            return queryset

class GuardianProfileViewSet(viewsets.ModelViewSet):
    queryset = GuardianProfile.objects.all()
    serializer_class = GuardianProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.query_params.get('user')

        if user is not None:
            queryset =  queryset.filter(user=user)
        return queryset

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



