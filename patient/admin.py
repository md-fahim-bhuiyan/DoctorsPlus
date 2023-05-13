from django.contrib import admin
from .models import *
# Register your models here.

class patientview(admin.ModelAdmin):
    list_display = ('full_name','user','mobile', 'gender', 'date_of_birth')

admin.site.register(Patient,patientview)


class Appointmentview(admin.ModelAdmin):
    list_display = ('patient_name','doctor', 'appointment_date', 'appointment_time')

admin.site.register(Appointment, Appointmentview)


class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('user','doner_name', 'blood_group', 'units_required', 'location', 'contact_number', 'is_approved', 'created_at')

admin.site.register(DonationRequest, DonationRequestAdmin)
