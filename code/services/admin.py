from django.contrib import admin

from .models import Service


class CustomServiceAdmin(admin.ModelAdmin):
    list_display = (
        'car_part', 'car', 'owner', 'cost', 'registration', 'date_start',
        'date_finish', 'is_active', 'created_at', 'updated_at',
        )
    ordering = ('car_part', 'created_at', 'date_start', 'date_finish',)
    list_filter = ('car_part', 'is_active',)

    def car(self, obj):
        return obj.car_part.car

    def owner(self, obj):
        return obj.car_part.car.owner

    def registration(self, obj):
        return obj.car_part.car.registration


admin.site.register(Service, CustomServiceAdmin)
