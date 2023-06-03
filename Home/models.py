from django.db import models
from patient.models import DiagnosticOrder
from adminView.models import Diagnostic


class TestResult(models.Model):
    test_name = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    order = models.ForeignKey(DiagnosticOrder, on_delete=models.CASCADE)
    result = models.CharField(max_length=100)
    normal_result = models.CharField(max_length=100, default='')
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.test_name.test_name} - Order ID: {self.order.pk}"


from patient.models import Appointment

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    problem = models.CharField(max_length=255)
    date = models.DateField()
    patient_name = models.CharField(max_length=255)
    patient_age = models.IntegerField()
    patient_weight = models.FloatField()
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length=6, choices=gender_choices, null=True, blank=True)
    patient_blood_pressure = models.CharField(max_length=50)
    patient_email = models.EmailField()
    doctor_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    doctor_email = models.EmailField()
    doctor_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.pk}"


class Medicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage_choose = (
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening')
    )
    dosage = models.CharField(max_length=9, choices=dosage_choose, blank=True)
    frequency = models.CharField(max_length=10)
    eat_time_choose = (
        ('Before Eat','Before Eat'),
        ('After Eat','After Eat'),
    )
    eat_time = models.CharField(max_length=10, choices=eat_time_choose)
    def __str__(self):
        return self.name


class Test(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name
