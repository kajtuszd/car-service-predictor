from .models import Service
from .serializers import ServiceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import Workshop
from cars.models import CarPart


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        workshop_name = self.request.query_params.get('workshop_name')
        car_part_slug = self.request.query_params.get('car_part_slug')
        workshop = Workshop.objects.get(workshop_name=workshop_name)
        car_part = CarPart.objects.get(slug=car_part_slug)
        serializer.save(workshop=workshop, car_part=car_part)
