from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'service', viewset=views.ServiceViewSet, basename='service')

urlpatterns = [
] + router.urls
