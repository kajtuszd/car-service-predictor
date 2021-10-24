from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Car, CarPart, CarPartCategory, Engine
from .serializers import (CarPartCategorySerializer, CarPartSerializer,
                          CarSerializer, EngineSerializer)
# from rest_framework.decorators import action
# from users.serializers import UserSerializerDB
# from users.models import User
# from rest_framework.response import Response


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(owner=self.request.user.pk)
    
    # @action(detail=True, methods=['get'])
    # def car_owner(self, request):
    #     car = self.get_object()
    #     user = User.objects.get(username=car.owner.username)
    #     serializer = UserSerializerDB(data=user.data)
    #     return Response(serializer.data)


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
        return self.queryset


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
