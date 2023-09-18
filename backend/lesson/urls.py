from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from .views import CompleteLessonView, ProgressionViewSet, ChapterViewSet, LessonViewSet, CompetenceViewSet
from .views import *



router = DefaultRouter()
router.register('progressions', ProgressionViewSet)
router.register('chapters', ChapterViewSet)
router.register('lessons', LessonViewSet)
router.register('competences', CompetenceViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subject-assignments', SubjectAssignmentViewSet)

# router.register('complete-lesson', CompleteLessonView, basename='complete-lesson')

urlpatterns = [
    path('', include(router.urls)),
]