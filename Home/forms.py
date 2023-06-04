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
from .models import Prescription


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = [
            'problem', 'patient_name', 'date', 'patient_age', 'patient_weight', 'gender',
            'patient_blood_pressure', 'patient_email', 'doctor_name', 'registration_number',
            'specialty', 'doctor_email', 'doctor_phone',
            'medicine_name_1', 'dosage_1', 'frequency_1', 'eat_time_1',
            'medicine_name_2', 'dosage_2', 'frequency_2', 'eat_time_2',
            'medicine_name_3', 'dosage_3', 'frequency_3', 'eat_time_3',
            'medicine_name_4', 'dosage_4', 'frequency_4', 'eat_time_4',
            'medicine_name_5', 'dosage_5', 'frequency_5', 'eat_time_5',
            'test_name_1', 'description_1',
            'test_name_2', 'description_2',
            'test_name_3', 'description_3',
            'test_name_4', 'description_4',
            'test_name_5', 'description_5',
        ]

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
            'medicine_name_1': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name_1-field'}),
            'dosage_1': forms.TextInput(attrs={'class': 'form-control', 'id': 'dosage_1-field'}),
            'frequency_1': forms.TextInput(attrs={'class': 'form-control', 'id': 'frequency_1-field'}),
            'eat_time_1': forms.Select(attrs={'class': 'form-control', 'id': 'eat_time_1-field'}),
            'medicine_name_2': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name_2-field'}),
            'dosage_2': forms.TextInput(attrs={'class': 'form-control', 'id': 'dosage_2-field'}),
            'frequency_2': forms.TextInput(attrs={'class': 'form-control', 'id': 'frequency_2-field'}),
            'eat_time_2': forms.Select(attrs={'class': 'form-control', 'id': 'eat_time_2-field'}),
            'medicine_name_3': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name_3-field'}),
            'dosage_3': forms.TextInput(attrs={'class': 'form-control', 'id': 'dosage_3-field'}),
            'frequency_3': forms.TextInput(attrs={'class': 'form-control', 'id': 'frequency_3-field'}),
            'eat_time_3': forms.Select(attrs={'class': 'form-control', 'id': 'eat_time_3-field'}),
            'medicine_name_4': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name_4-field'}),
            'dosage_4': forms.TextInput(attrs={'class': 'form-control', 'id': 'dosage_4-field'}),
            'frequency_4': forms.TextInput(attrs={'class': 'form-control', 'id': 'frequency_4-field'}),
            'eat_time_4': forms.Select(attrs={'class': 'form-control', 'id': 'eat_time_4-field'}),
            'medicine_name_5': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name_5-field'}),
            'dosage_5': forms.TextInput(attrs={'class': 'form-control', 'id': 'dosage_5-field'}),
            'frequency_5': forms.TextInput(attrs={'class': 'form-control', 'id': 'frequency_5-field'}),
            'eat_time_5': forms.Select(attrs={'class': 'form-control', 'id': 'eat_time_5-field'}),
            'test_name_1': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name_1-field'}),
            'description_1': forms.TextInput(attrs={'class': 'form-control', 'id': 'description_1-field'}),
            'test_name_2': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name_2-field'}),
            'description_2': forms.TextInput(attrs={'class': 'form-control', 'id': 'description_2-field'}),
            'test_name_3': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name_3-field'}),
            'description_3': forms.TextInput(attrs={'class': 'form-control', 'id': 'description_3-field'}),
            'test_name_4': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name_4-field'}),
            'description_4': forms.TextInput(attrs={'class': 'form-control', 'id': 'description_4-field'}),
            'test_name_5': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name_5-field'}),
            'description_5': forms.TextInput(attrs={'class': 'form-control', 'id': 'description_5-field'}),
        }

dosage_choose = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening')
)


# class MedicineForm(forms.ModelForm):

#     class Meta:
#         model = Medicine
#         fields = ['name', 'dosage', 'frequency', 'eat_time']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_name'}),
#             'dosage': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_dosage'}),
#             'frequency': forms.TextInput(attrs={'class': 'form-control', 'id': 'medicine_frequency'}),
#             'eat_time': forms.Select(attrs={'class': 'form-control', 'id': 'medicine_eat_time'}),
#         }


# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = ['name', 'description']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_name'}),
#             'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'test_description', 'rows': 3}),
#         }
