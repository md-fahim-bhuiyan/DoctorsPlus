from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date
from .models import Patient, ContactMessage, DonationRequest, ReceiverRequest, Appointment
from .forms import SearchForm, PatientForm, ContactForm, DonationRequestForm, ReceiverRequestForm, AppointmentForm
from django.contrib.auth import authenticate, login
from doctor.models import Doctor
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
import datetime
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_google_meet_link():
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/your/credentials.json',
        scopes=SCOPES
    )

    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': 'Appointment',
        'start': {
            'dateTime': datetime.datetime.now().isoformat(),
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(),
            'timeZone': 'UTC',
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'random-string',
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet',
                },
            },
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()

    return created_event.get('conferenceData').get('entryPoints')[0].get('uri')



today = datetime.date.today()
formatted_date = today.strftime('%Y-%m-%d')


def patient_signup_view(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.save()
            print("save")
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            # Log in the user and redirect to home page
            user = authenticate(username=userForm.cleaned_data['username'],
                                password=userForm.cleaned_data['password'])
            login(request, user)
            return redirect('home')
    return render(request, 'patient/patientsignup.html', context=mydict)


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'patient/password_change.html'
    # change to your desired success url
    success_url = reverse_lazy('patient-dashboard')


@login_required
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
    context = {'mobile': patient.mobile, 'gender': patient.gender,
               'address': patient.address, 'age': age}
    return render(request, 'patient/profile.html', context)


@login_required
def patient_dashboard_view(request):
    return render(request, 'patient/patient_dashboard.html')


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


# @login_required
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


@login_required
def book_appointment(request, doctor_pk, doctor_name):
    doctor = Doctor.objects.get(pk=doctor_pk)
    consultation_fee = doctor.consultation_fee

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']
            patient_name = form.cleaned_data['patient_name']

            # Set the user field to the current authenticated user
            appointment = Appointment(
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                doctor=doctor,
                patient_name=patient_name,
                user=request.user  # Set the user field to the current user
            )
            appointment.save()
            messages.success(request, 'Appointment has been booked successfully!')
            return redirect('payment')
    else:
        form = AppointmentForm(initial={'doctor': doctor_name})

    return render(request, 'patient/book_appointment.html', {'form': form, 'consultation_fee': consultation_fee})


def payment(request):
    return render(request, 'patient/payment_process.html')

def process_payment(request):
    if request.method == 'POST':
        # Retrieve the form data
        credit_card_number = request.POST.get('number')
        expiration_date = request.POST.get('expiry')
        cardholder_name = request.POST.get('name')
        cvv = request.POST.get('cvv')

        # Perform payment processing logic here
        # Add your custom payment processing code

        # Assuming the payment is successful, you can display a success message
        messages.success(request, 'Payment successful!')
        return redirect('appointment-details')  # Redirect to the appointment details page or any other appropriate page

    return render(request, 'patient/payment_process.html')

def appointment_details(request):
    appointment_list = Appointment.objects.filter(user=request.user)
    return render(request, 'patient/appointment_details.html', {'appointment_list': appointment_list})


def bloodbank(request):
    return render(request, 'bloodbank/index.html')


@login_required
def doner_dashboard(request):

    requestmade = DonationRequest.objects.filter(user=request.user).count()
    requestpending = DonationRequest.objects.filter(
        is_approved='PANDING').count()
    requestrejected = DonationRequest.objects.filter(
        is_approved='REJECT').count()
    requestapproved = DonationRequest.objects.filter(
        is_approved='APPROVED').count()

    return render(request, 'bloodbank/doner_dashboard.html', {'requestpending': requestpending,
                                                              'requestmade': requestmade,
                                                              'requestrejected': requestrejected,
                                                              'requestapproved': requestapproved})


@login_required(login_url='patientlogin')
def create_donation_request(request):
    if request.method == 'POST':
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            donation_request = form.save(commit=False)
            donation_request.user = request.user
            donation_request.save()
            messages.success(
                request, 'Your donation request has been submitted.')
            return redirect('view_donation_requests')
    else:
        form = DonationRequestForm()
    return render(request, 'bloodbank/create_donation_request.html', {'form': form})


@login_required
def view_donation_requests(request):
    donation_requests = DonationRequest.objects.filter(
        user=request.user).order_by('-created_at')
    return render(request, 'bloodbank/view_donation_requests.html', {'requests': donation_requests})


@login_required
def approve_donation_request(request, pk):
    donation_request = DonationRequest.objects.get(pk=pk)
    donation_request.is_approved = True
    donation_request.save()
    messages.success(request, 'Donation request has been approved.')
    return redirect('view_donation_requests')


@login_required
def reject_donation_request(request, pk):
    donation_request = DonationRequest.objects.get(pk=pk)
    donation_request.delete()
    messages.success(request, 'Donation request has been rejected.')
    return redirect('view_donation_requests')


def blood_receiver_dashboard(request):
    requestmade = ReceiverRequest.objects.filter(user=request.user).count()
    requestpending = ReceiverRequest.objects.filter(
        is_approved='PENDING').count()
    requestrejected = ReceiverRequest.objects.filter(
        is_approved='REJECT').count()
    requestapproved = ReceiverRequest.objects.filter(
        is_approved='APPROVED').count()

    return render(request, 'bloodbank/receiver_dashboard.html', {'requestpending': requestpending,
                                                                 'requestmade': requestmade,
                                                                 'requestrejected': requestrejected,
                                                                 'requestapproved': requestapproved})


def receiver_request_create_view(request):
    form = ReceiverRequestForm()
    if request.method == 'POST':
        form = ReceiverRequestForm(request.POST)
        if form.is_valid():
            receiver_request = form.save(commit=False)
            receiver_request.user = request.user
            receiver_request.save()
            return redirect('receiver_request_success')
    return render(request, 'bloodbank/receiver_request_create.html', {'form': form})


def receiver_request_success_view(request):
    return render(request, 'bloodbank/receiver_request_success.html')


def receiver_request_list_view(request):
    receiver_requests = ReceiverRequest.objects.filter(user=request.user)
    return render(request, 'bloodbank/receiver_request_list.html', {'receiver_requests': receiver_requests})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                name=name, email=email, message=message)
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'patient/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'patient/contact_success.html')


def about(request):
    return render(request, 'patient/about.html')
