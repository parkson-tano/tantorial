from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacherprofile', TeacherProfileViewSet)
router.register('studentprofile', StudentProfileViewSet)
router.register('parentprofile', GuardianProfileViewSet)
router.register('studentguardian', StudentGuardianViewSet)
router.register('studentsubject', StudentSubjectViewSet)
router.register('subjectteacher', SubjectTeacherViewSet)
router.register('classteacher', ClassTeacherViewSet)
router.register('schoolprofile', SchoolProfileViewSet)
router.register('schoolprofileupdate', SchoolProfileUpdateAPIView)
router.register('teacherprofileupdate', TeacherProfileUpdateAPIView)
router.register('studentprofileupdate', StudentProfileUpdateAPIView)
router.register('parentprofileupdate', GuardianProfileUpdateAPIView)


urlpatterns = [
    path('', include(router.urls)),
]
