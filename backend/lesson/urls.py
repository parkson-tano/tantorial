from django.urls import include, path
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
<<<<<<< HEAD
from .views import ProgressionViewSet, ChapterViewSet, LessonViewSet, CompetenceViewSet
=======
=======
>>>>>>> 3939e8daf9edc541d7eecfaabb52952ea8dd26e7
# from .views import CompleteLessonView, ProgressionViewSet, ChapterViewSet, LessonViewSet, CompetenceViewSet
from .views import *


<<<<<<< HEAD
>>>>>>> allowed a school to be abel to create classes, subject and teacher and also alowed a school to be able to assign a teacher to a subject and a class
=======
>>>>>>> 3939e8daf9edc541d7eecfaabb52952ea8dd26e7

router = DefaultRouter()
router.register('progressions', ProgressionViewSet)
router.register('chapters', ChapterViewSet)
router.register('lessons', LessonViewSet)
router.register('competences', CompetenceViewSet)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 3939e8daf9edc541d7eecfaabb52952ea8dd26e7
router.register(r'classes', ClassViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subject-assignments', SubjectAssignmentViewSet)

<<<<<<< HEAD
>>>>>>> allowed a school to be abel to create classes, subject and teacher and also alowed a school to be able to assign a teacher to a subject and a class
=======
>>>>>>> 3939e8daf9edc541d7eecfaabb52952ea8dd26e7
# router.register('complete-lesson', CompleteLessonView, basename='complete-lesson')

urlpatterns = [
    path('', include(router.urls)),
]