from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bmdc = models.CharField(max_length=10, null=False, unique=True, default='')
    address = models.CharField(max_length=40, default='')
    mobile = models.CharField(
        max_length=20, null=False, unique=True, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    specialist = models.CharField(max_length=40, default='')
    experience = models.CharField(max_length=2, default='')
    hospital = models.CharField(max_length=40, null=True, blank=True)
    consultation_fee = models.CharField(max_length=40, default='')
    bio = models.CharField(max_length=200, default='')
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length=6, choices=gender_choices, null=True, blank=True)

    @property
    def full_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name + " "+self.user.last_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bmdc = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
