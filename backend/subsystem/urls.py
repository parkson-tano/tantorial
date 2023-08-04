from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('subsystem', SubsystemViewSet)
router.register('language', LanguageViewSet)
router.register('classroom', ClassRoomViewSet)
router.register('subject', SubjectViewSet)
router.register('country', CountryViewSet)
router.register('region', RegionViewSet)
router.register('division', DivisionViewSet)
router.register('subdivision', SubDivisionViewSet)
router.register('locality', LocalityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
