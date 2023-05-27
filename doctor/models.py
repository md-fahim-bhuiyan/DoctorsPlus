from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bmdc = models.CharField(max_length=10, null=False, unique=True, default='')
    address = models.CharField(max_length=40, default='')
    mobile = models.CharField(
        max_length=20, null=False, unique=True, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    specialist = models.CharField(max_length=40, default='')
    experience = models.CharField(max_length=2, default='')
    hospital = models.CharField(max_length=40, null=True, blank=True)
    consultation_fee = models.CharField(max_length=40, default='')
    bio = models.CharField(max_length=200, default='')
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length=6, choices=gender_choices, null=True, blank=True)

    @property
    def full_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name + " "+self.user.last_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bmdc = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


from django.db import models

class Prescription(models.Model):
    problem = models.CharField(max_length=255)
    date = models.DateField()
    patient_name = models.CharField(max_length=255)
    patient_age = models.IntegerField()
    patient_weight = models.FloatField()
    gender = models.CharField(max_length=10)
    patient_blood_pressure = models.CharField(max_length=50)
    patient_email = models.EmailField()
    doctor_name = models.CharField(max_length=255, default='')
    registration_number = models.CharField(max_length=50)
    specialty = models.CharField(max_length=255)
    doctor_email = models.EmailField()
    doctor_phone = models.CharField(max_length=20)

class Medication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    FREQUENCY_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    dose = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    duration = models.CharField(max_length=50)
    eat_time = models.CharField(max_length=10)

class Test(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    test = models.CharField(max_length=255)


