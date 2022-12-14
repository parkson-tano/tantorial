from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
class UserAdmin(BaseUserAdmin):
    # form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('profile_pic', 'phone_number',
            'account_type', 'first_name', 'last_name','code')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2', 'account_type'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'student_class', 
        'account_type')
    list_display = ('email', 'first_name', 'last_name', 'is_superuser', 
        'account_type', 'code')
    ordering = ('email','account_type' )
admin.site.register(User, UserAdmin)

admin.site.register((StudentProfile, TeacherProfile, SchoolProfile, ParentProfile))