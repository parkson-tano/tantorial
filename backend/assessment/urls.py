from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('assessmentquestion', AssessmentQuestionViewSet)
router.register('assessmenttarget', AssessmentTargetViewSet)
router.register('studentmark', StudentMarkViewSet)
router.register('studentanswer', StudentAnswerViewSet)
router.register('teacherassessment', TeacherAssessmentViewSet)
router.register('assessmenttype', AssessmentTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
