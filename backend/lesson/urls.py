from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'progressions', views.ProgressionViewSet)
router.register(r'chapters', views.ChapterViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'competences', views.CompetenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]