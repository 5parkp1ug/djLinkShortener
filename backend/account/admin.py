from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'profile_pic',)
    fieldsets = (
        ('Basic Information', {
            'classes': ('extrapretty', 'grp-collapse grp-open',),
            'fields': (('first_name', 'last_name'), 'email',
                       ('profile_pic', 'date_joined'))
        }),
        ('Permissions', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('is_superuser', 'is_staff', 'is_active',)
        }),
        ('Authentication', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('username', 'password', 'last_login',)
        }),
    )