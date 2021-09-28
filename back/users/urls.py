from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'user', viewset=views.UserViewSet, basename='user')
router.register(r'workshop', viewset=views.WorkshopViewSet, basename='workshop')

urlpatterns = [
] + router.urls
