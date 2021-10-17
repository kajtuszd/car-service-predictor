from .models import User, Workshop
from .serializers import UserSerializer, WorkshopSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]


class WorkshopViewSet(viewsets.ModelViewSet):
    serializer_class = WorkshopSerializer
    queryset = Workshop.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
