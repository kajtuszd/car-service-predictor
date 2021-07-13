from django.contrib import admin
from .models import Car, Engine


class CustomCarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'production_year', 'registration', 'mileage', 'capacity', 'horsepower', 'engine_type',)
    search_fields = ('brand', 'model', 'registration', 'capacity', 'horsepower',)
    ordering = ('brand', 'model',)
    list_filter = ('brand', 'model',)

    def capacity(self, obj):
        return obj.engine.capacity

    def horsepower(self, obj):
        return obj.engine.horsepower

    def engine_type(self, obj):
        return obj.engine.engine_type


class CustomEngineAdmin(admin.ModelAdmin):
    list_display = ('capacity', 'horsepower', 'engine_type',)
    search_fields = ('capacity', 'horsepower',)
    ordering = ('capacity', 'horsepower',)
    list_filter = ('engine_type',)


admin.site.register(Car, CustomCarAdmin)
admin.site.register(Engine, CustomEngineAdmin)
