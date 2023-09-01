from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *

# Create your views here.

from rest_framework.permissions import AllowAny

class AssessmentQuestionViewSet(viewsets.ModelViewSet):
    queryset = AssessmentQuestion.objects.all()
    serializer_class = AssessmentQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(deleted=False, archived=False)
        assessment = self.request.query_params.get('assessment', None)

        if assessment is not None:
            return queryset.filter(assessment = assessment)
        else:
            return queryset

class AssessmentTargetViewSet(viewsets.ModelViewSet):
    queryset = AssessmentTarget.objects.all()
    serializer_class = AssessmentTargetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(deleted=False, archived=False)
        assessment = self.request.query_params_get('assessment', None)
        classroom = self.request.query_params_get('class', None)
        target = self.request.query_params_get('target', None)
        teacher = self.request.query_params_get('user', None)

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.archived = True
        instance.save()

        

class TeacherAssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherAssessmentSerializer
    permission_classes = [IsAuthenticated, IsStudentInClass]

    def get_queryset(self):
        class_id = self.request.query_params.get('class_id')

        if class_id is not None:
            current_datetime = timezone.now()
            return TeacherAssessment.objects.filter(
                assessment_class__id=class_id,
                deleted=False,
                archived=False,
                dateline__gt=current_datetime,  # Filter by dateline not yet arrived
            )
        else:
            return TeacherAssessment.objects.none()

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.archived = True
        instance.save()



class AssessmentTypeViewSet(viewsets.ModelViewSet):
    queryset = AssessmentType.objects.all()
    serializer_class = AssessmentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]