from django import forms
from django.contrib.auth.models import User
from . import models


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):

    class Meta:
        model = models.Doctor
        fields = ['mobile', 'date_of_birth', 'address', 'gender']