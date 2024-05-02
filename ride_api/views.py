from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from djoser.views import UserViewSet
from .models import Ride
from .serializers import UserSerializer, RideSerializer

class CustomUserViewSet(UserViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    
    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
