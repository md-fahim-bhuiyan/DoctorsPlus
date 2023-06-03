from django import forms
from .models import TestResult
from adminView.models import Diagnostic
# from patient.models import DiagnosticOrder

class TestResultForm(forms.ModelForm):
    test_name = forms.ModelChoiceField(queryset=Diagnostic.objects.all())
    # order = forms.ModelChoiceField(queryset=DiagnosticOrder.objects.all())

    class Meta:
        model = TestResult
        fields = ['test_name', 'result','normal_result', 'remarks']
    def __init__(self, *args, **kwargs):
        order = kwargs.pop('order', None)
        super().__init__(*args, **kwargs)
        if order:
            self.fields['test_name'].initial = order.diagnostic    


from django import forms
from .models import Prescription, Medicine, Test


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['problem', 'patient_name', 'date', 'patient_age', 'patient_weight', 'gender',
                  'patient_blood_pressure', 'patient_email', 'doctor_name', 'registration_number',
                  'specialty', 'doctor_email', 'doctor_phone']

        widgets = {
            'problem': forms.TextInput(attrs={'class': 'form-control', 'id': 'problem-field'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'patient_name-field'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date-field', 'type': 'date'}),
            'patient_age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'patient_age-field'}),
            'patient_weight': forms.NumberInput(attrs={'class': 'form-control', 'id': 'patient_weight-field'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender-field'}),
            'patient_blood_pressure': forms.TextInput(attrs={'class': 'form-control', 'id': 'blood_pressure-field'}),
            'patient_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'patient_email-field'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'doctor_name-field'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'registration_number-field'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'id': 'specialty-field'}),
            'doctor_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'doctor_email-field'}),
            'doctor_phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'doctor_phone-field'}),
        }

dosage_choose = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening')
)


class MedicineForm(forms.ModelForm):
    dosage = forms.MultipleChoiceField(
        choices=dosage_choose,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Medicine
        fields = ['name', 'dosage', 'frequency', 'eat_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_frequency'}),
            'eat_time': forms.Select(attrs={'class': 'form-control', 'id': 'medicine_eat_time'}),
        }


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_description', 'rows': 3}),
        }
