from .models import Service
from .serializers import ServiceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
