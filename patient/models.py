from django.db import models
from django.contrib.auth.models import User
import uuid
from doctor.models import Doctor




class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    #email = models.EmailField()
    mobile = models.CharField(max_length=20,null=False, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
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
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name


class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default= 0)
    # fee = models.IntegerField()

BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
]

APPROVED = [
    ('APPROVED', 'APPROVED'),
    ('PANDING', 'PANDING'),
    ('REJECT', 'REJECT')
]

class DonationRequest(models.Model):
    doner_name = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units_required = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    is_approved = models.CharField(default='PANDING', max_length=8, choices=APPROVED)
    created_at = models.DateTimeField(auto_now_add=True)

class ReceiverRequest(models.Model):
    receiver_name = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units_required = models.PositiveIntegerField()
    reason = models.CharField(max_length=200, blank=True)
    age = models.PositiveIntegerField()
    hospital = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    is_approved = models.CharField(default='PENDING', max_length=8, choices=APPROVED)
    created_at = models.DateTimeField(auto_now_add=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"