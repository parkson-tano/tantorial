from rest_framework.permissions import BasePermission
from .models import TeacherAssessment



class IsStudentInClass(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        class_id = request.query_params.get('class_id')

        if class_id is not None:
            return user.is_authenticated and user.studentprofile.classroom_id == class_id
        else:
            return False
