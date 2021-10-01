from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Workshop


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Address details', {'fields': (
            'city', 'street', 'house_number', 'flat_number', 'zip_code',)}),
    )
    list_display = (
        'first_name', 'last_name', 'email', 'username', 'phone', 'is_superuser',
        'is_staff', 'is_active', 'date_joined', 'workshop',
        )
    ordering = ('email', 'first_name', 'last_name', 'username', 'date_joined',)
    search_fields = ('email', 'phone', 'first_name', 'last_name', 'username',)
    list_filter = ('is_active', 'is_superuser', 'is_staff')


class CustomWorkshopAdmin(admin.ModelAdmin):
    search_fields = ('workshop_name',)
    list_display = ('workshop_name',)
    ordering = ('workshop_name',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Workshop, CustomWorkshopAdmin)
