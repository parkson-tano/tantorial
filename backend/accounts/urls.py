from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SchoolRegister, TeacherRegister,  RegisterLanderView, StudentRegister, ParentRegister
from django.contrib.auth import views as dj_auth_views

app_name = 'tantorial_auth'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register-option/', RegisterLanderView.as_view(), name='register-option'),
    path('student-register/', StudentRegister.as_view(), name='student-register'),
    path('parent-register/', ParentRegister.as_view(), name='parent-register'),
    path('school-register/', SchoolRegister.as_view(), name='school-register'),
    path('teacher-register/', TeacherRegister.as_view(), name='teacher-register'),
    path('logout/', dj_auth_views.LogoutView.as_view(), name="logout"),
]
