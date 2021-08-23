from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('date_of_birth','first_name', 'last_name')}),
        (_('Details'), {'fields': ('employee_id','emp_ctc','manager_name','department','remarks')}),
        (_('Important dates'), {'fields': ('date_joined', 'date_of_exit')}),
        (_('Files'), {'fields': ('emp_cv', 'emp_images')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('employee_id','email', 'password1', 'password2'),
        }),
    )
    list_display = ('employee_id','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('employee_id',)