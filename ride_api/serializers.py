from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ride

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RideSerializer(serializers.ModelSerializer):
    rider = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    driver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Ride
        fields = ['id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at']
