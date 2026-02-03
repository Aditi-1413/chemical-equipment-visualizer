from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatasetViewSet, health_check

router = DefaultRouter()
router.register(r'datasets', DatasetViewSet, basename='dataset')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check, name='health_check'),
]