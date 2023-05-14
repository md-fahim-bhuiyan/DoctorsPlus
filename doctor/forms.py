
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
        