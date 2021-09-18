from django.contrib import admin
from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Auto)
class AutoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VehiclePassport)
class VehiclePassportAdmin(admin.ModelAdmin):
    pass
