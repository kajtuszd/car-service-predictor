from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import User, Workshop
from .serializers import UserSerializerDB, WorkshopSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializerDB
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def all(self, request):
        return Response(User.objects.all().count())


class WorkshopViewSet(viewsets.ModelViewSet):
    serializer_class = WorkshopSerializer
    queryset = Workshop.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def all(self, request):
        return Response(Workshop.objects.all().count())
