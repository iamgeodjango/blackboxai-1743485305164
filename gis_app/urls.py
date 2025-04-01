from django.urls import path
from .views import SpatialFeatureListCreateView, SpatialFeatureDetailView, map_view

urlpatterns = [
    path('features/', SpatialFeatureListCreateView.as_view(), name='feature-list'),
    path('features/<int:pk>/', SpatialFeatureDetailView.as_view(), name='feature-detail'),
    path('map/', map_view, name='map-view'),
]
