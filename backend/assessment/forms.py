from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class AssessmentTypeForm(forms.ModelForm):
    
    class Meta:
        model = AssessmentType
        fields = ("__all__")


class TeacherAssessmentForm(forms.ModelForm):
    
    class Meta:
        model = TeacherAssessment
        fields = ("title" ,'subsystem', 'assessment_class', 'assessment_subject')


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        exclude = ('assessment', )

class StudentMarkForm(forms.ModelForm):
    
    class Meta:
        model = StudentMark
        fields = ("__all__")




