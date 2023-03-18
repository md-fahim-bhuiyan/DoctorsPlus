from django.http import HttpResponse
from django.shortcuts import render


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm, PatientRegistrationForm
from .models import Doctor, Patient


def home(request):
    return render(request, 'Home/index.html')


def doctor_registration(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            specialty = form.cleaned_data['specialty']
            bio = form.cleaned_data['bio']
            contact = form.cleaned_data['contact']
            doctor = Doctor(user=user, specialty=specialty, bio=bio, contact=contact)
            doctor.save()
            login(request, user)
            return redirect('home')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor_registration.html', {'form': form})

def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            patient = Patient(user=user, phone=phone, address=address, gender=gender)
            patient.save()
            login(request, user)
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient_registration.html', {'form': form})
