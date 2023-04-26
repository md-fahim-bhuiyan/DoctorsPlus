from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    #email = models.EmailField()
    mobile = models.CharField(max_length=20,null=False, unique=True)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
