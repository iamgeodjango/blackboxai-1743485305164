from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from gis_app.models import SpatialFeature

class Command(BaseCommand):
    help = 'Load sample spatial data into the database'

    def handle(self, *args, **options):
        sample_data = [
            {'name': 'London', 'geometry': Point(-0.1276, 51.5072)},
            {'name': 'New York', 'geometry': Point(-74.0060, 40.7128)},
            {'name': 'Tokyo', 'geometry': Point(139.6917, 35.6895)},
        ]

        for data in sample_data:
            SpatialFeature.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Created {data["name"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data'))