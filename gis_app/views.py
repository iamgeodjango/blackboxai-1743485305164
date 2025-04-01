from django.shortcuts import render
from rest_framework import generics
from .models import SpatialFeature
from .serializers import SpatialFeatureSerializer

class SpatialFeatureListCreateView(generics.ListCreateAPIView):
    queryset = SpatialFeature.objects.all()
    serializer_class = SpatialFeatureSerializer

class SpatialFeatureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpatialFeature.objects.all()
    serializer_class = SpatialFeatureSerializer

def map_view(request):
    return render(request, 'gis_app/map.html')