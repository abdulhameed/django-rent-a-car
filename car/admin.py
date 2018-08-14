from django.contrib import admin
from . import models


@admin.register(models.FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'power', 'consumation')
    search_fields = ('name',)
    list_filter = ('name', 'consumation')


@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.AditionalEquipment)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'model_year', 'engine', 'price_hourly', 'available', 'rate')
    search_fields = ('name',)
    list_editable = ('price_hourly', 'available')
    list_filter = ('available', 'rate')

    def model(self, obj):
        return obj.model

    def engine(self, obj):
        return obj.engine


@admin.register(models.Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('photo', 'car')

    def car(self, obj):
        return obj.car




