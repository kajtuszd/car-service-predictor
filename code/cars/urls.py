from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'car', viewset=views.CarViewSet, basename='car')
router.register(r'car-part', viewset=views.CarPartViewSet, basename='car-part')
router.register(r'car-part-category', viewset=views.CarPartCategoryViewSet,
                basename='car-part-category')
router.register(r'engine', viewset=views.EngineViewSet, basename='engine')

urlpatterns = [
] + router.urls
