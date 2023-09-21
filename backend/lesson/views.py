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

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Only show published lessons to all
        if self.action == 'list' and user.is_authenticated:
            queryset = queryset.filter(publish=True)
        
        # Only the teacher can see their lessons until published
        if self.action != 'list' and user.is_authenticated:
            queryset = queryset.filter(chapter__progression__teacher=user)
        
        return queryset

    def perform_create(self, serializer):
        lesson = serializer.save()
        students = lesson.chapter.progression.class_room.students.all()
        for student in students:
            StudentLesson.objects.create(student=student, lesson=lesson)

    def perform_update(self, serializer):
        lesson = serializer.save()
        students = lesson.chapter.progression.class_room.students.all()
        
        for student in students:
            StudentLesson.objects.get_or_create(student=student, lesson=lesson)

    @action(detail=True, methods=['post'])
    def complete(self, request, *args, **kwargs):
        lesson = self.get_object()
        student = request.user.student_profile

        if StudentLesson.objects.filter(student=student, lesson=lesson).exists():
            return Response("You have already completed this lesson.", status=400)

        StudentLesson.objects.create(student=student, lesson=lesson)
        return Response("Lesson completed successfully")

    @action(detail=True, methods=['post'])
    def publish(self, request, *args, **kwargs):
        lesson = self.get_object()
        lesson.publish = True 
        lesson.save()
        return Response("Lesson published successfully")

    def perform_destroy(self, instance):
        instance.delete = True 
        instance.save()


        def get_queryset(self):
        return Lesson.objects.filter(teacher=self.request.user.teacherprofile)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teacherprofile)

    def perform_update(self, serializer):
        serializer.save(teacher=self.request.user.teacherprofile)

    def perform_destroy(self, instance):
        instance.delete()



class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer



class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectAssignmentViewSet(viewsets.ModelViewSet):
    queryset = SubjectAssignment.objects.all()
    serializer_class = SubjectAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'])
    def assign(self, request, *args, **kwargs):
        subject_assignment = self.get_object()
        teacher_id = request.data.get('teacher_id')
        class_id = request.data.get('class_id')

        if not teacher_id or not class_id:
            return Response("Teacher ID and Class ID are required.", status=400)

        teacher = get_object_or_404(Teacher, id=teacher_id)
        class_assigned = get_object_or_404(Class, id=class_id)

        subject_assignment.teacher = teacher
        subject_assignment.class_assigned = class_assigned
        subject_assignment.save()

        return Response("Teacher assigned to the subject and class successfully.")

    @action(detail=True, methods=['post'])
    def unassign_teacher(self, request, *args, **kwargs):
        subject_assignment = self.get_object()
        subject_assignment.teacher = None
        subject_assignment.class_assigned = None
        subject_assignment.save()

        return Response("Teacher unassigned from the subject and class.")