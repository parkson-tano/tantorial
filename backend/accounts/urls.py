from django.urls import path, include

from .views import *

app_name = 'tantorial_auth'

urlpatterns = [
    path('api/', include("accounts.api.urls")),
    path('register/', RegisterLanderView.as_view(), name='register-option'),
    path('register/student/', StudentRegister.as_view(), name='student-register'),
    path('register/parent/', ParentRegister.as_view(), name='parent-register'),
    path('register/school/', SchoolRegister.as_view(), name='school-register'),
    path('register/teacher/', TeacherRegister.as_view(), name='teacher-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', passwordchange, name='password_change'),
    path('password_reset/', password_reset_request, name="password_reset"),

]
