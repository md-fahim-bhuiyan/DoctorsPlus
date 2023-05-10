from django import forms
from django.contrib.auth.models import User
from . import models
from .models import DonationRequest


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    
    class Meta:
        model=models.Patient
        fields = ['mobile', 'date_of_birth','address','gender']

        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobile-field'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'id': 'dob-field'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address-field'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender-field'}),
        }


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search Query', max_length=100)

class AppointmentForm(forms.Form):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))
    doctor = forms.CharField(widget=forms.HiddenInput())
    patient_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs:
            initial = kwargs['initial']
            self.fields['doctor'].initial = initial['doctor']


class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['blood_group', 'units_required', 'location', 'contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blood_group'].widget.attrs.update({'class': 'form-control'})
        self.fields['units_required'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})