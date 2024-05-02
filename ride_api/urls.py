from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'rides', RideViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
