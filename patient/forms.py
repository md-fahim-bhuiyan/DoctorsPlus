from django import forms
from django.contrib.auth.models import User
from . import models
from .models import DonationRequest, ReceiverRequest
from .models import DiagnosticOrder


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
        fields = ['doner_name','blood_group', 'units_required', 'location', 'contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doner_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['blood_group'].widget.attrs.update({'class': 'form-control'})
        self.fields['units_required'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})
        

class ReceiverRequestForm(forms.ModelForm):
    class Meta:
        model = ReceiverRequest
        fields = ['receiver_name', 'blood_group', 'units_required', 'reason', 'age', 'hospital', 'contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['blood_group'].widget.attrs.update({'class': 'form-control'})
        self.fields['units_required'].widget.attrs.update({'class': 'form-control'})
        self.fields['reason'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['hospital'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

# class DiagnosticOrderForm(forms.ModelForm):
#     class Meta:
#         model = DiagnosticOrder
#         fields = ['patient_name', 'doctor', 'additional_tests', 'Address']
#         widgets = {
#             'additional_tests': forms.CheckboxSelectMultiple(),
#         }

class DiagnosticOrderForm(forms.ModelForm):
    class Meta:
        model = DiagnosticOrder
        fields = ['patient_name', 'patient_age', 'patient_mobile', 'patient_email', 'patient_gender', 'doctor', 'additional_tests', 'Address']
        widgets = {
                # 'additional_tests': forms.CheckboxSelectMultiple(attrs={'class': 'row'}),
                'additional_tests': forms.CheckboxSelectMultiple(),

        }
        labels = {
            'patient_name': 'Patient Name',
            'patient_age': 'Patient Age',
            'patient_mobile': 'Mobile',
            'patient_email': 'Email',
            'patient_gender': 'Gender',
            'doctor': 'Doctor',
            'additional_tests': 'Additional Tests',
            'Address': 'Address',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['patient_age'].widget.attrs.update({'class': 'form-control'})
        self.fields['patient_mobile'].widget.attrs.update({'class': 'form-control'})
        self.fields['patient_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['patient_gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['doctor'].widget.attrs.update({'class': 'form-control'})
        self.fields['Address'].widget.attrs.update({'class': 'form-control'})