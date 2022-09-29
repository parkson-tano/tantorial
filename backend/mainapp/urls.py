from django.urls import path
from .views import *
app_name = 'tantorial'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('feed', FeedView.as_view(), name='index_feed'),
    path('feed/all/', ChildCreateView.as_view(), name = 'child')
]