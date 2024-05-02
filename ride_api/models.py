from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    
    rider = models.ForeignKey(User, related_name='rides_requested', on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='rides_driven', null=True, blank=True, on_delete=models.SET_NULL)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.dropoff_location}"
