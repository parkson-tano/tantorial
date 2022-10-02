from django.urls import path
from .views import *
# from django.contrib.auth import get_user_model
# User = get_user_model()
from accounts.models import User
app_name = 'tantorial'

if User.is_authenticated:
    if User.account_type == 'student':
        cls = StudentIndexView.as_view()
    else:
        cls = FeedView.as_view()
else:
    cls = IndexView.as_view()

urlpatterns = [
    path('', cls, name='index'),
    path('feed', FeedView.as_view(), name='index_feed'),
    path('student/feed', StudentIndexView.as_view(), name='index_student'),
    path('student/feed/assessment/<int:pk>/', StudentTakeQuestionView.as_view(), name = 'answer_question'),
    path('feed/all/', ChildCreateView.as_view(), name = 'child'),
    path('feed/assessment/', CreateAssessmentLanderView.as_view(), name = 'ass_type'),
    path('feed/assessment/create/<str:slug>/', CreateAssessmentView.as_view(), name='create_assessment'),
    path('feed/assessment/my-assessments', TeacherAssessmentView.as_view(), name='my_assessment'),
    path('feed/create/my-assessment/publish-<int:id>/', ManageAssessmentView.as_view(), name = 'manage_publish'),
    path('feed/my-assessment/update/<int:pk>/', TeacherAssessmentUpdateView.as_view(), name='update_assessment'),
    path('feed/my-assessment/delete/<int:pk>/', TeacherAssessmentDeleteView.as_view(), name='delete_assessment'),
    path('feed/assessment/create/question/<int:id>/', CreateQuestionView.as_view(), name='create_question'),
    path('feed/assessment/my-questions/<int:pk>', QuestiontView.as_view(), name='my_question'),
    path('feed/my-assessment/update/question/<int:pk>/', QuestionUpdateView.as_view(), name='update_question'),
    path('feed/my-assessment/delete/question/<int:pk>/', QuestionDeleteView.as_view(), name='delete_question'),

]
