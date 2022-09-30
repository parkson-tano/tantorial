from django.urls import path
from .views import *
app_name = 'tantorial'
urlpatterns = [
        path('', IndexView.as_view(), name='index'),
    path('feed', FeedView.as_view(), name='index_feed'),
    path('feed/all/', ChildCreateView.as_view(), name = 'child'),
    path('feed/assessment/', CreateAssessmentLanderView.as_view(), name = 'ass_type'),
    path('feed/assessment/create/<str:slug>/', CreateAssessmentView.as_view(), name='create_assessment'),
    path('feed/assessment/my-assessments', TeacherAssessmentView.as_view(), name='my_assessment'),
    path('feed/create/my-assessment/publish-<int:id>/', ManageAssessmentView.as_view(), name = 'manage_publish'),
    path('feed/my-assessment/update/<int:pk>/', TeacherAssessmentUpdateView.as_view(), name='update_assessment'),

]
