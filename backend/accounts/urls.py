from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

app_name = 'tantorial_auth'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register-option', RegisterLanderView.as_view(), name='register-option'),
    path('student-register', StudentRegister.as_view(), name='student-register'),
    path('logout', LogoutView.as_view(), name="logout"),
]