from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # تحديد الحقول التي يجب عرضها في واجهة الإدارة
    list_display = ('email', 'first_name', 'last_name',
                    'phone_number', 'is_staff')

    # تحديد حقول التصفية في الواجهة الإدارية
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # تحديد الحقول التي يمكن البحث فيها
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')

    # تحديد الحقول التي يمكن تحريرها في الواجهة الإدارية
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('first_name',)
    # تحديد حقول الإدخال في الواجهة الإدارية
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
