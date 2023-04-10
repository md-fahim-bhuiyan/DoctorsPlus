from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class PatientRegister(models.Model):
    email = models.EmailField(max_length=254, unique=True, primary_key=True)
    phone =  models.CharField(max_length=20, unique=True)
    first_name =  models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    password = models.CharField(max_length=128, blank=False, null=False)


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        db_table='patientregister'
