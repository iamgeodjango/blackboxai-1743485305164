from django.contrib.gis.db import models

class SpatialFeature(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.GeometryField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spatial Feature"
        verbose_name_plural = "Spatial Features"
        indexes = [
            models.Index(fields=['geometry']),
        ]