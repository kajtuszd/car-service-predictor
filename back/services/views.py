from cars.models import Car, CarPart
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from users.models import User, Workshop

from .models import Service
from .serializers import ServiceSerializer


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

    def get_queryset(self, *args, **kwargs):
        username = self.request.query_params.get('username')
        if username:
            user = User.objects.get(username=username)
            services = Service.objects.filter(workshop=user.workshop)
            return services
        else:
            cars = Car.objects.filter(owner=self.request.user.pk)
            car_parts = []
            for car in cars:
                car_parts += CarPart.objects.filter(car=car)
            services = []
            for car_part in car_parts:
                services += Service.objects.filter(car_part=car_part)
            return services

    @action(detail=False, methods=['get'])
    def all(self, request):
        return Response(Service.objects.all().count())

    @action(detail=False, methods=['get'])
    def most_popular_workshop(self, request):
        if Service.objects.all().count() == 0:
            return Response('') 
        services = Service.objects.values('workshop__workshop_name').annotate(
            num_services=Count('workshop')).order_by('-num_services')
        return Response(services[0]["workshop__workshop_name"])

    @action(detail=False, methods=['get'])
    def most_frequently_fixed_part(self, request):
        if Service.objects.all().count() == 0:
            return Response('') 
        services = Service.objects.values('car_part__category__name').annotate(
            num_services=Count('car_part')).order_by('-num_services')
        return Response(services[0]["car_part__category__name"])
