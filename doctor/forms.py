from django import forms
from django.contrib.auth.models import User
from . import models


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields = ['address', 'mobile',  'gender', 'bmdc',
                  'date_of_birth', 'consultation_fee', 'specialist', 'experience', 'hospital', 'bio']

        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobile-field'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'id': 'dob-field'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address-field'}),
            'bmdc': forms.TextInput(attrs={'class': 'form-control', 'id': 'bmdc'}),
            'consultation_fee': forms.TextInput(attrs={'class': 'form-control', 'id': 'consultation_fee'}),
            'specialist': forms.TextInput(attrs={'class': 'form-control', 'id': 'specialist'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'id': 'experience'}),
            'hospital': forms.TextInput(attrs={'class': 'form-control', 'id': 'hospital'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'id': 'bio'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender-field'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    bmdc = forms.CharField(label='BMDC', max_length=10)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

from django import forms

class PrescriptionForm(forms.Form):
    problem = forms.CharField(max_length=255)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    patient_name = forms.CharField(max_length=255)
    patient_age = forms.IntegerField()
    patient_weight = forms.FloatField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    patient_blood_pressure = forms.CharField(max_length=50)
    patient_email = forms.EmailField()
    doctor_name = forms.CharField(max_length=255)
    registration_number = forms.CharField(max_length=50)
    specialty = forms.CharField(max_length=255, disabled=True)
    doctor_email = forms.EmailField()
    doctor_phone = forms.CharField(max_length=20)

class MedicationForm(forms.Form):
    medication = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control medication', 'required': True}))
    dose = forms.MultipleChoiceField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')],
                                     widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    duration = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    eat_time = forms.ChoiceField(choices=[('before', 'Before'), ('after', 'After')], widget=forms.Select(attrs={'class': 'form-control', 'required': True}))

class TestForm(forms.Form):
    test = forms.CharField(max_length=255)


