from .models import User, Customer, Workshop
from .serializers import UserSerializer, CustomerSerializer, WorkshopSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permissions_classes = [IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'user'
    permission_classes = [IsAuthenticated]


class WorkshopViewSet(viewsets.ModelViewSet):
    serializer_class = WorkshopSerializer
    queryset = Workshop.objects.all()
    lookup_field = 'user'
    permission_classes = [IsAuthenticated]
