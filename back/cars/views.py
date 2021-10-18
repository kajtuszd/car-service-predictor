from .models import CarPartCategory, CarPart, Engine, Car
from .serializers import (CarPartCategorySerializer, CarPartSerializer,
                          EngineSerializer, CarSerializer)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


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

    # def get_queryset(self, *args, **kwargs):
    #     car = self.request.query_params.get('car')
    #     if car is not None:
    #         return self.queryset.filter(car=car)
    #     return self.queryset


class CarPartCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CarPartCategorySerializer
    queryset = CarPartCategory.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self, *args, **kwargs):
    #     car = self.request.query_params.get('car')
    #     if car is not None:
    #         return self.queryset.filter(car=car)
    #     return self.queryset


class EngineViewSet(viewsets.ModelViewSet):
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
