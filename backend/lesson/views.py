from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import IsLessonCreator
from django.views import View
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action



# Create your views here.

class ProgressionViewSet(viewsets.ModelViewSet):
    queryset = Progression.objects.all()
    serializer_class = ProgressionSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsLessonCreator] 


    def get_permissions(self):
        if self.action == 'list' and not self.request.user.is_authenticated:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Only show published lessons to all
        if self.action == 'list' and user.is_authenticated:
            queryset = queryset.filter(publish=True)
        
        # Only the teacher can see their lessons until published
        if self.action != 'list' and user.is_authenticated:
            queryset = queryset.filter(teacher=user)
        
        return queryset


    def perform_create(self, serializer):
        lesson_class = serializer.validated_data['lesson_class']
        students = lesson_class.students.all()
        lesson = serializer.save(teacher = self.request.user)
        lesson.students.set(students)
        serializer.save(teacher = self.request.user)

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class CompleteLessonView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    @action(detail=True, methods=['post'])
    def complete(self, request, *args, **kwargs):
        instance = self.get_object()
        student = request.user.student_profile
        instance.students_completed.add(student)
        return Response("Lesson completed successfully")