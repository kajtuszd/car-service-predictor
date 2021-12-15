from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Car, CarPart, CarPartCategory, Engine
from .serializers import (CarPartCategorySerializer, CarPartSerializer,
                          CarSerializer, EngineSerializer)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(owner=self.request.user.pk)


class CarPartViewSet(viewsets.ModelViewSet):
    serializer_class = CarPartSerializer
    queryset = CarPart.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        car_slug = self.request.query_params.get('car_slug')
        car = Car.objects.get(slug=car_slug)
        serializer.save(car=car)

    def get_queryset(self, *args, **kwargs):
        car_slug = self.request.query_params.get('car_slug')
        if car_slug is not None:
            car = Car.objects.get(slug=car_slug)
            return self.queryset.filter(car=car)
        cars = Car.objects.filter(owner=self.request.user.pk)
        car_parts_queryset = []
        for car in cars:
            car_parts_queryset += CarPart.objects.filter(car=car)
        return car_parts_queryset


class CarPartCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CarPartCategorySerializer
    queryset = CarPartCategory.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]


class EngineViewSet(viewsets.ModelViewSet):
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
