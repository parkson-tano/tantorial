from rest_framework.permissions import BasePermission

class AccountTypePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        account_type = request.user.account_type

        if account_type == 'student' and view.action in ['list', 'retrieve']:
            return True

        if account_type == 'teacher' and view.action in ['list', 'retrieve', 'destroy']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        account_type = request.user.account_type

        if account_type == 'student':
            return obj.published

        if account_type == 'teacher':
            return obj.teacher == request.user and not obj.deleted and not obj.archived

        return False