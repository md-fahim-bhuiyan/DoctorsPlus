from django import forms
from django.contrib.auth.models import User
from . import models

class DonorForm(forms.ModelForm):
    class Meta:
        model = models.BloodDonate
        fields = ['name', 'email', 'age', 'bloodgroup',
                  'address', 'mobile',  'disease', 'unit']


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = models.Receiver
        fields = ['name', 'email', 'age', 'bloodgroup', 'disease', 'address',
                  'hospital', 'mobile']


class BloodForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['bloodgroup', 'unit']


class RequestForm(forms.ModelForm):
    class Meta:
        model = models.BloodRequest
        fields = ['receiver_name', 'receiver_age',
                  'reason', 'bloodgroup', 'unit']
