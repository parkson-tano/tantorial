from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacherprofile', TeacherProfileViewSet, basename='teacherprofile')
router.register('studentprofile', StudentProfileViewSet, basename='studentprofile' )
router.register('parentprofile', GuardianProfileViewSet, basename='parentprofile')
router.register('studentguardian', StudentGuardianViewSet, basename='studentguardian')
router.register('studentsubject', StudentSubjectViewSet, basename='studentsubject')
router.register('subjectteacher', SubjectTeacherViewSet, basename='subjectteacher')
router.register('classteacher', ClassTeacherViewSet, basename='classteacher')
router.register('schoolprofile', SchoolProfileViewSet, basename='schoolprofile')
router.register('schoolprofile-fetch', SchoolProfileUpdateAPIView, basename='schoolprofileupdate')
router.register('teacherprofile-fetch', TeacherProfileUpdateAPIView, basename='teacherprofileupdate')
router.register('studentprofile-fetch', StudentProfileUpdateAPIView, basename='studentprofileupdate')
router.register('parentprofile-fetch', GuardianProfileUpdateAPIView, basename='parentprofileupdate')


urlpatterns = [
    path('', include(router.urls)),
]
