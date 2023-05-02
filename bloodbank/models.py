from . import models as dmodels
from . import models as rmodels
from django.db import models
from django.contrib.auth.models import User

# 'name', 'email', 'age', 'bloodgroup', 'disease', 'address',
# 'hospital', 'mobile'


class Receiver(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    disease = models.CharField(max_length=100)
    address = models.CharField(max_length=40)
    hospital = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.name


class BloodDonate(models.Model):
    name = models.CharField(max_length=30, default=" ")
    email = models.EmailField(max_length=40, unique=True, null=True)
    disease = models.CharField(max_length=100, default="Nothing")
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    address = models.CharField(max_length=40, default="Nothing")
    mobile = models.CharField(max_length=20, null=True)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.donor


class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.bloodgroup


class BloodRequest(models.Model):
    request_by_receiver = models.ForeignKey(
        rmodels.Receiver, null=True, on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(
        dmodels.BloodDonate, null=True, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=30)
    receiver_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.bloodgroup
