from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.db.models import Q


# Create your views here.

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(user=user)
        return queryset

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(user=user)
        return queryset
    

class SchoolProfileViewSet(viewsets.ModelViewSet):
    queryset = SchoolProfile.objects.all()
    serializer_class = SchoolProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        subsystem = self.request.query_params.get('subsystem')
        
        queryset = self.queryset  # Start with the base queryset

        if user.is_authenticated:
            queryset = queryset.filter(user=user)

        if subsystem is not None:
            queryset = queryset.filter(subsystem=subsystem)

        return queryset

class GuardianProfileViewSet(viewsets.ModelViewSet):
    queryset = GuardianProfile.objects.all()
    serializer_class = GuardianProfileSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(user=user)
        return queryset

class StudentGuardianViewSet(viewsets.ModelViewSet):
    queryset = StudentGuardian.objects.all()
    serializer_class = StudentGuardianSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(Q(guardian=user) | Q(student=user))
        return queryset
    

class StudentSubjectViewSet(viewsets.ModelViewSet):
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(student=user)
        return queryset

class SubjectTeacherViewSet(viewsets.ModelViewSet):
    queryset = SubjectTeacher.objects.all()
    serializer_class = SubjectTeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(Q(teacher=user) | Q(subject__school__user=user))
        return queryset

class ClassTeacherViewSet(viewsets.ModelViewSet):
    queryset = ClassTeacher.objects.all()
    serializer_class = ClassTeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(Q(teacher=user) | Q(classroom__school__user=user))
        return queryset



