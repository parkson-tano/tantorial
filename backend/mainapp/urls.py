from django.contrib.auth import get_user_model
from django.urls import path

from .views import *

user = get_user_model()
# from accounts.models import User
app_name = 'tantorial'

if user.is_authenticated:
    if User.account_type == 'student':
        cls = StudentIndexView.as_view()
    else:
        cls = FeedView.as_view()

urlpatterns = [
    path('', cls, name='index'),
    path('welcome', IndexView.as_view(), name = 'welcome'),
    path('feed', FeedView.as_view(), name='index_feed'),
    path('student/feed', StudentIndexView.as_view(), name='index_student'),
    path('feed/all/', ChildCreateView.as_view(), name = 'child'),
]
