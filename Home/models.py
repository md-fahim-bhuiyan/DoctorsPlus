from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    specialty = models.CharField(max_length=50)
    bio = models.TextField()
    contact = models.CharField(max_length=50)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
