from rest_framework.permissions import BasePermission

class AccountTypePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        account_type = request.user.account_type

        if account_type in ['teacher', 'student', 'parent', 'school'] or view.action == 'list':
            return True

        return False