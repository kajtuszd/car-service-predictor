from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .models import Car, CarPart, CarPartCategory, Engine
from .serializers import (CarPartCategorySerializer, CarPartSerializer,
                          CarSerializer, EngineSerializer)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(owner=self.request.user.pk)

    @action(detail=False, methods=['get'])
    def all(self, request):
        return Response(Car.objects.all().count())

    @action(detail=False, methods=['get'])
    def most_popular_brand(self, request):
        if Car.objects.all().count() == 0:
            return Response('')
        cars = Car.objects.values('brand').annotate(
            num_cars=Count('model')).order_by('-num_cars')
        return Response(cars[0]["brand"])

    @action(detail=False, methods=['get'])
    def most_popular_model(self, request):
        if Car.objects.all().count() == 0:
            return Response('')
        cars = Car.objects.values('brand', 'model').annotate(
            num_cars=Count('model')).order_by('-num_cars')
        return Response((cars[0]["brand"], cars[0]["model"],))

    @action(detail=False, methods=['get'])
    def different_models_number(self, request):
        if Car.objects.all().count() == 0:
            return Response('')
        cars = Car.objects.values('brand', 'model').annotate(
            num_cars=Count('model')).order_by('-num_cars')
        return Response(cars)


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

    @action(detail=False, methods=['get'])
    def all(self, request):
        return Response(CarPart.objects.all().count())


class CarPartCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CarPartCategorySerializer
    queryset = CarPartCategory.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]


class EngineViewSet(viewsets.ModelViewSet):
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def most_popular_drive_type(self, request):
        if Engine.objects.all().count() == 0:
            return Response('')
        engines = Engine.objects.values('engine_type').annotate(
            num_engines=Count('engine_type')).order_by('-num_engines')
        return Response(engines[0]["engine_type"])
