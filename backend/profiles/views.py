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
    
    @action(methods=['post'], detail=True, url_path='create-class')
    def create_class(self, request, pk=None):
        school = self.get_object()
        class_data = request.data.get('class')

        if class_data:
            ClassRoom.objects.create(school=school, **class_data)
            return Response({'message': 'Class created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Class data not provided.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='create-subject')
    def create_subject(self, request, pk=None):
        school = self.get_object()
        subject_data = request.data.get('subject')

        if subject_data:
            Subject.objects.create(school=school, **subject_data)
            return Response({'message': 'Subject created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Subject data not provided.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='create-teacher')
    def create_teacher(self, request, pk=None):
        school = self.get_object()
        teacher_data = request.data.get('teacher')

        if teacher_data:
            TeacherProfile.objects.create(school=school, **teacher_data)
            return Response({'message': 'Teacher created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Teacher data not provided.'}, status=status.HTTP_400_BAD_REQUEST)
    

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

class ClassTeacherViewSet(viewsets.ModelViewSet):
    queryset = ClassTeacher.objects.all()
    serializer_class = ClassTeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = self.queryset.filter(Q(teacher=user) | Q(classroom__school__user=user))
        return queryset



