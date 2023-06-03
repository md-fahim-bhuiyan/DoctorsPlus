from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date
from .models import Doctor, ContactMessage
from .forms import DoctorForm, ContactForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from patient.models import Appointment


def doctor_signup_view(request):
    userForm = forms.DoctorUserForm()
    doctorForm = forms.DoctorForm()
    mydict = {'userForm': userForm, 'doctorForm': doctorForm}
    if request.method == 'POST':
        userForm = forms.DoctorUserForm(request.POST)
        doctorForm = forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save(commit=False)
            doctor.user = user
            doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request, 'doctor/doctorsignup.html', context=mydict)


def calculate_age(born):
    today = date.today()
    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))
    return age


@login_required
def docProfile(request):
    user = request.user
    doctor = Doctor.objects.get(user=user)
    age = calculate_age(doctor.date_of_birth)
    context = {'mobile': doctor.mobile, 'specialist': doctor.specialist,
               'bmdc': doctor.bmdc, 'gender': doctor.gender, 'address': doctor.address, 'hospital': doctor.hospital, 'experience': doctor.experience, 'fee': doctor.consultation_fee, 'bio': doctor.bio, 'age': age}
    return render(request, 'doctor/docprofile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    doctor = Doctor.objects.get(user=user)

    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)

        if doctor_form.is_valid():
            doctor_form.save()
            return redirect('docProfile')

    else:
        doctor_form = DoctorForm(instance=doctor)

    context = {'doctor_form': doctor_form}
    return render(request, 'doctor/edit_profile.html', context)


def doctor_dashboard(request):
    return render(request, 'doctor/doctor_dashboard.html')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'doctor/password_change.html'
    success_url = reverse_lazy('doctor-dashboard')


def about(request):
    return render(request, 'patient/about.html')


def contact(request):
    user = request.user
    doctor = Doctor.objects.get(user=user)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                name=name, email=email, message=message)
            return redirect('doc_contact_success')
    else:
        form = ContactForm()
    return render(request, 'doctor/contact.html', context={'form': form, 'bmdc': doctor.bmdc})


def contact_success(request):
    return render(request, 'doctor/contact_success.html')




def doctor_appointments(request):
    doctor = request.user.doctor  # Assuming you have a OneToOneField relationship between User and Doctor models
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor/appointments.html', {'appointments': appointments})

# def prescription(request):
#     return render (request, "doctor/prescription.html")


from django.shortcuts import render, redirect
# from .forms import PrescriptionForm, MedicationForm, TestForm
# from .models import Prescription, Medication, Test
from django.forms import formset_factory

# def create_prescription(request):
#     MedicationFormset = formset_factory(MedicationForm, extra=1)
#     TestFormset = formset_factory(TestForm, extra=1)
    
#     if request.method == 'POST':
#         prescription_form = PrescriptionForm(request.POST)
#         medication_formset = MedicationFormset(request.POST, prefix='medication')
#         test_formset = TestFormset(request.POST, prefix='test')

#         if prescription_form.is_valid() and medication_formset.is_valid() and test_formset.is_valid():
#             prescription = Prescription.objects.create(
#                 problem=prescription_form.cleaned_data['problem'],
#                 date=prescription_form.cleaned_data['date'],
#                 patient_name=prescription_form.cleaned_data['patient_name'],
#                 patient_age=prescription_form.cleaned_data['patient_age'],
#                 patient_weight=prescription_form.cleaned_data['patient_weight'],
#                 gender=prescription_form.cleaned_data['gender'],
#                 patient_blood_pressure=prescription_form.cleaned_data['patient_blood_pressure'],
#                 patient_email=prescription_form.cleaned_data['patient_email'],
#                 doctor_name=prescription_form.cleaned_data['doctor_name'],
#                 registration_number=prescription_form.cleaned_data['registration_number'],
#                 specialty=prescription_form.cleaned_data['specialty'],
#                 doctor_email=prescription_form.cleaned_data['doctor_email'],
#                 doctor_phone=prescription_form.cleaned_data['doctor_phone'],
#             )

#             for form in medication_formset:
#                 Medication.objects.create(
#                     prescription=prescription,
#                     medication=form.cleaned_data['medication'],
#                     dose=form.cleaned_data['dose'],
#                     duration=form.cleaned_data['duration'],
#                     eat_time=form.cleaned_data['eat_time'],
#                 )

#             for form in test_formset:
#                 Test.objects.create(
#                     prescription=prescription,
#                     test=form.cleaned_data['test'],
#                 )

#             return redirect('prescription_success')
#     else:
#         prescription_form = PrescriptionForm()
#         medication_formset = MedicationFormset(prefix='medication')
#         test_formset = TestFormset(prefix='test')

#     return render(request, 'doctor/prescription.html', {
#         'prescription_form': prescription_form,
#         'medication_formset': medication_formset,
#         'test_formset': test_formset,
#     })

# from django.shortcuts import get_object_or_404
# # from patient.models import appointment_id
# from patient.models import Appointment


# def create_prescription(request, appointment_id):
#     appointment = Appointment.objects.get(appointment_id=appointment_id)
#     if request.method == 'POST':
#         form = PrescriptionForm(request.POST)
#         if form.is_valid():
#             prescription = form.save(commit=False)
#             prescription.appointment = appointment
#             prescription.save()
#             return HttpResponseRedirect('/doctor/appointments/')  # Redirect to appointments page
#     else:
#         form = PrescriptionForm()
#     return render(request, 'doctor/prescription.html', {'form': form, 'appointment': appointment})


