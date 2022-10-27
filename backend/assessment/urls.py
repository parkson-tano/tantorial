from django.contrib.auth import get_user_model
from django.urls import path

from .views import *

user = get_user_model()
# from accounts.models import User
app_name = 'tantorial_assessment'

urlpatterns = [
    path('student/assessment/<int:pk>/',
         StudentTakeQuestionView.as_view(), name='answer_question'),
    path('feed/', CreateAssessmentLanderView.as_view(), name='ass_type'),
    path('feed/create/<str:slug>/',
         CreateAssessmentView.as_view(), name='create_assessment'),
    path('feed/my-assessments',
         TeacherAssessmentView.as_view(), name='my_assessment'),
    path('feed/create/my-assessment/publish-<int:id>/',
         ManageAssessmentView.as_view(), name='manage_publish'),
    path('feed/my-assessment/update/<int:pk>/',
         TeacherAssessmentUpdateView.as_view(), name='update_assessment'),
    path('feed/my-assessment/delete/<int:pk>/',
         TeacherAssessmentDeleteView.as_view(), name='delete_assessment'),
    path('feed/create/question/<int:id>/',
         CreateQuestionView.as_view(), name='create_question'),
    path('feed/my-questions/<int:pk>',
         QuestionView.as_view(), name='my_question'),
    path('feed/my-assessment/update/question/<int:pk>/',
         QuestionUpdateView.as_view(), name='update_question'),
    path('feed/my-assessment/delete/question/<int:pk>/',
         QuestionDeleteView.as_view(), name='delete_question'),

]
