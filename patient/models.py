from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    #email = models.EmailField()
    mobile = models.CharField(max_length=20,null=False, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length=6, choices=gender_choices, null=True, blank=True)
    

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
