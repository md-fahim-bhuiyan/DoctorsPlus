from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Doctor
from .forms import DoctorForm

def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'doctor/doctorsignup.html',context=mydict)


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
               'bmdc': doctor.bmdc, 'gender': doctor.gender, 'address': doctor.address, 'hospital': doctor.hospital, 'experience':doctor.experience, 'fee': doctor.consultation_fee, 'bio': doctor.bio, 'age': age}
    return render(request, 'docprofile.html', context)


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
