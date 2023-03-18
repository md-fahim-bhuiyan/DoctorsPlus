from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Doctor, Patient

class DoctorRegistrationForm(UserCreationForm):
    specialty = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    contact = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

class PatientRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
