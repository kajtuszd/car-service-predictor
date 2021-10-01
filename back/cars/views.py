from .models import CarPartCategory, CarPart, Engine, Car
from .serializers import (CarPartCategorySerializer, CarPartSerializer,
                          EngineSerializer, CarSerializer)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'slug'
    permissions_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarPartViewSet(viewsets.ModelViewSet):
    serializer_class = CarPartSerializer
    queryset = CarPart.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


class CarPartCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CarPartCategorySerializer
    queryset = CarPartCategory.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


class EngineViewSet(viewsets.ModelViewSet):
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
