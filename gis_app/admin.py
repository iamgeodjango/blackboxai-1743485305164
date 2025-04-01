from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import SpatialFeature

@admin.register(SpatialFeature)
class SpatialFeatureAdmin(gis_admin.OSMGeoAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    default_lon = 0
    default_lat = 0
    default_zoom = 2