from django.contrib import admin

from .models import Car, CarPart, CarPartCategory, Engine


class CustomCarAdmin(admin.ModelAdmin):
    list_display = (
        'brand', 'model', 'owner', 'production_year', 'daily_mileage',
        'registration', 'mileage', 'capacity', 'horsepower', 'engine_type',)
    search_fields = (
        'brand', 'model', 'owner', 'registration', 'capacity', 'horsepower',)
    ordering = ('brand', 'model', 'owner',)
    list_filter = ('brand', 'model', 'owner',)

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


class CarPartAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'car', 'latest_fix_date', 'latest_fix_mileage',
        'fix_every_period', 'fix_every_mileage',)
    search_fields = ('category', 'car', 'latest_fix_date',)
    ordering = (
        'category', 'car', 'latest_fix_date', 'latest_fix_mileage',
        'fix_every_period', 'fix_every_mileage',)
    list_filter = ('category', 'car',)


class CarPartCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'drive_type',)
    search_fields = ('name',)
    ordering = ('name', 'drive_type',)
    list_filter = ('drive_type',)


admin.site.register(Car, CustomCarAdmin)
admin.site.register(Engine, CustomEngineAdmin)
admin.site.register(CarPartCategory, CarPartCategoryAdmin)
admin.site.register(CarPart, CarPartAdmin)
