from .forms import SearchForm
from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import date
from .models import Patient
from .forms import PatientForm
import datetime
from django.contrib.auth import authenticate, login
from doctor.models import Doctor
from django.http import HttpResponse
from .forms import AppointmentForm
from .models import Appointment

today = datetime.date.today()
formatted_date = today.strftime('%Y-%m-%d')


def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.save()
            print("save")
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            # Log in the user and redirect to home page
            user = authenticate(username=userForm.cleaned_data['username'],
                                password=userForm.cleaned_data['password'])
            login(request, user)
            return redirect('home')
    return render(request,'patient/patientsignup.html',context=mydict)


def patient(user):
    return user.is_authenticated and hasattr(user, 'patient')


def calculate_age(born):
    today = date.today()
    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))
    return age


@login_required
@user_passes_test(Patient)
def profile(request):
    user = request.user
    patient = Patient.objects.get(user=user)
    age = calculate_age(patient.date_of_birth)
    context = {'mobile': patient.mobile, 'gender': patient.gender,'address':patient.address, 'age': age}
    return render(request, 'profile.html', context)
    # return render(request, 'profile.html')


@login_required
@user_passes_test(Patient)
def patient_edit_profile(request):
    user = request.user
    patient = Patient.objects.get(user=user)

    if request.method == 'POST':
        patient_form = PatientForm(request.POST, instance=patient)

        if patient_form.is_valid():
            patient_form.save()
            return redirect('profile')

    else:
        patient_form = PatientForm(instance=patient)

    context = {'patient_form': patient_form}
    return render(request, 'patient/edit_profile.html', context)

@login_required
@user_passes_test(Patient)
def search_results(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            doctors = Doctor.objects.filter(specialist__icontains=search_query)
            print(doctors)
            return render(request, 'patient/search_results.html', {'doctors': doctors})
    else:
        form = SearchForm()
    return render(request, 'patient/search.html', {'form': form})




def patient_dashboard_view(request):
   return render(request,'success.html')

from django.contrib import messages

def book_appointment(request, doctor_pk, doctor_name):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']
            patient_name = form.cleaned_data['patient_name']
            doctor = Doctor.objects.get(pk=doctor_pk)
            appointment = Appointment(appointment_date=appointment_date, appointment_time=appointment_time, doctor=doctor, patient_name=patient_name)
            appointment.save()
            messages.success(request, 'Appointment has been booked successfully!')
            return redirect('payment')
    else:
        form = AppointmentForm(initial={'doctor': doctor_name})
    return render(request, 'patient/book_appointment.html', {'form': form})


def payment(request):
    return render(request, 'patient/appointment.html')