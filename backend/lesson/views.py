from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class ProgressionViewSet(viewsets.ModelViewSet):
    queryset = Progression.objects.all()
    serializer_class = ProgressionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Only show published lessons to all
        if self.action == 'list' and user.is_authenticated:
            queryset = queryset.filter(teacher=user)
        
        # Only the teacher can see their lessons until published
        if self.action != 'list' and user.is_authenticated:
            queryset = queryset.filter(teacher=user)
        
        return queryset


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Only show published lessons to all
        if self.action == 'list' and user.is_authenticated:
            queryset = queryset.filter(progression__teacher=user)
        
        # Only the teacher can see their lessons until published
        if self.action != 'list' and user.is_authenticated:
            queryset = queryset.filter(progression__teacher=user)
        
        return queryset

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [permissions.IsAuthenticated] 

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user

    #     # Only show published lessons to all
    #     if self.action == 'list' and user.is_authenticated:
    #         queryset = queryset.filter(publish=True)
        
    #     # Only the teacher can see their lessons until published
    #     if self.action != 'list' and user.is_authenticated:
    #         queryset = queryset.filter(chapter__progression__teacher=user)
        
    #     return queryset

    # def perform_create(self, serializer):
    #     lesson = serializer.save()
    #     students = lesson.chapter.progression.class_room.students.all()
    #     for student in students:
    #         StudentLesson.objects.create(student=student, lesson=lesson)

    # @action(detail=True, methods=['post'])
    # def complete(self, request, *args, **kwargs):
    #     lesson = self.get_object()
    #     student = request.user.student_profile

    #     if StudentLesson.objects.filter(student=student, lesson=lesson).exists():
    #         return Response("You have already completed this lesson.", status=400)

    #     StudentLesson.objects.create(student=student, lesson=lesson)
    #     return Response("Lesson completed successfully")

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Only show published lessons to all
        if self.action == 'list' and user.is_authenticated:
            queryset = queryset.filter(teacher=user)
        
        # Only the teacher can see their lessons until published
        if self.action != 'list' and user.is_authenticated:
            queryset = queryset.filter(teacher=user)
        
        return queryset