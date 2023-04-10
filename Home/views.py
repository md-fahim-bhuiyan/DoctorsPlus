from django.http import HttpResponse
from django.shortcuts import render


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm, PatientRegistrationForm
from .models import Doctor, Patient


def home(request):
    return render(request, 'Home/index.html')

