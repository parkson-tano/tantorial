from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacherprofile', TeacherProfileViewSet)
router.register('studentprofile', StudentProfileViewSet)
router.register('guardianprofile', GuardianProfileViewSet)
router.register('studentguardian', StudentGuardianViewSet)
router.register('studentsubject', StudentSubjectViewSet)
router.register('subjectteacher', SubjectTeacherViewSet)
router.register('classteacher', ClassTeacherViewSet)
router.register('schoolprofile', SchoolProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
