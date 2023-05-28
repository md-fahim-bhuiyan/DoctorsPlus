from django import forms
from django.contrib.auth.forms import AuthenticationForm
from patient.models import DonationRequest, ReceiverRequest
from . import models
from .models import Diagnostic

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['doner_name','blood_group', 'units_required', 'location', 'contact_number','is_approved']

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
        fields = ['receiver_name', 'blood_group', 'units_required', 'reason', 'age', 'hospital', 'contact_number','is_approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['blood_group'].widget.attrs.update({'class': 'form-control'})
        self.fields['units_required'].widget.attrs.update({'class': 'form-control'})
        self.fields['reason'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['hospital'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']


class DiagnosticForm(forms.ModelForm):
    class Meta:
        model = Diagnostic
        fields = ['test_name', 'price', 'category', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['test_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})