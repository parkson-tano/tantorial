from django.urls import path, reverse_lazy, include

from .views import SchoolRegister, TeacherRegister,  RegisterLanderView, StudentRegister, ParentRegister
from django.contrib.auth import views as dj_auth_views

app_name = 'tantorial_auth'

urlpatterns = [
    path('api/', include("accounts.api.urls")),
    path('register/', RegisterLanderView.as_view(), name='register-option'),
    path('register/student/', StudentRegister.as_view(), name='student-register'),
    path('register/parent/', ParentRegister.as_view(), name='parent-register'),
    path('register/school/', SchoolRegister.as_view(), name='school-register'),
    path('register/teacher/', TeacherRegister.as_view(), name='teacher-register'),
    path('logout/', dj_auth_views.LogoutView.as_view(), name="logout"),
    path("change-password/", dj_auth_views.PasswordChangeView.as_view(
        template_name="account/password_change.html",
        success_url=reverse_lazy("tantorial:index"),
    )),
]
