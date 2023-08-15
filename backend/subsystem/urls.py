from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('subsystem', SubsystemViewSet, basename='subsystem')
router.register('language', LanguageViewSet, basename='language')
router.register('classroom', ClassRoomViewSet, basename='classroom')
router.register('classroom-fetch', ClassFetchAPIView, basename='classroom-fetch')
router.register('subject', SubjectViewSet, basename='subject')
router.register('country', CountryViewSet, basename='country')
router.register('region', RegionViewSet, basename='region')
router.register('division', DivisionViewSet, basename='division')
router.register('subdivision', SubDivisionViewSet, basename='subdivision')
router.register('locality', LocalityViewSet, basename='locality')


urlpatterns = [
    path('', include(router.urls)),
]
