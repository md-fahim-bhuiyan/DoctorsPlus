from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PatientRegister
from django.forms import ModelForm

class PatientRegister(ModelForm):
    class Meta:
        model = PatientRegister
        fields = '__all__'