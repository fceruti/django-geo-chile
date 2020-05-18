from django.contrib import admin

from .models import Region, Province, Commune


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "lat", "lng"]
    search_fields = ["name"]


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ["code", "region", "name", "lat", "lng"]
    list_filter = ["region"]
    search_fields = ["name"]


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ["code", "region", "province", "name", "lat", "lng"]
    list_filter = ["region", "province"]
    search_fields = ["name"]
