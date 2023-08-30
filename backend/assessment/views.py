from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class AssessmentQuestionViewSet(viewsets.ModelViewSet):
    queryset = AssessmentQuestion.objects.all()
    serializer_class = AssessmentQuestionSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(deleted=False, archived=False)
        assessment = self.request.query_params_get('assessment', None)

        if assessment is not None:
            return queryset.filter(assessment = assessment)
        else:
            return queryset

class AssessmentTargetViewSet(viewsets.ModelViewSet):
    queryset = AssessmentTarget.objects.all()
    serializer_class = AssessmentTargetSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(deleted=False, archived=False)
        assessment = self.request.query_params_get('assessment', None)
        classroom = self.request.query_params_get('class', None)
        target = self.request.query_params_get('target', None)
        teacher = self.request.query_params_get('user', None)

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer

class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

class TeacherAssessmentViewSet(viewsets.ModelViewSet):
    queryset = TeacherAssessment.objects.all()
    serializer_class = TeacherAssessmentSerializer

class AssessmentTypeViewSet(viewsets.ModelViewSet):
    queryset = AssessmentType.objects.all()
    serializer_class = AssessmentTypeSerializer