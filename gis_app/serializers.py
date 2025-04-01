from rest_framework import serializers
from .models import SpatialFeature

class SpatialFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialFeature
        fields = ['id', 'name', 'geometry', 'created_at']
        geo_field = 'geometry'