from django.urls import include, path
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import ProgressionViewSet, ChapterViewSet, LessonViewSet, CompetenceViewSet
=======
# from .views import CompleteLessonView, ProgressionViewSet, ChapterViewSet, LessonViewSet, CompetenceViewSet
from .views import *


>>>>>>> allowed a school to be abel to create classes, subject and teacher and also alowed a school to be able to assign a teacher to a subject and a class

router = DefaultRouter()
router.register('progressions', ProgressionViewSet)
router.register('chapters', ChapterViewSet)
router.register('lessons', LessonViewSet)
router.register('competences', CompetenceViewSet)
<<<<<<< HEAD
=======
router.register(r'classes', ClassViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subject-assignments', SubjectAssignmentViewSet)

>>>>>>> allowed a school to be abel to create classes, subject and teacher and also alowed a school to be able to assign a teacher to a subject and a class
# router.register('complete-lesson', CompleteLessonView, basename='complete-lesson')

urlpatterns = [
    path('', include(router.urls)),
]