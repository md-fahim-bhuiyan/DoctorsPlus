from django.contrib import admin
from .models import *
# Register your models here.

class patientview(admin.ModelAdmin):
    list_display = ('full_name','user','mobile', 'gender', 'date_of_birth')

admin.site.register(Patient,patientview)


class Appointmentview(admin.ModelAdmin):
    list_display = ('patient_name', 'user', 'doctor', 'appointment_date', 'appointment_time')

admin.site.register(Appointment, Appointmentview)


class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('user','doner_name', 'blood_group', 'units_required', 'location', 'contact_number', 'is_approved', 'created_at')

admin.site.register(DonationRequest, DonationRequestAdmin)
class ReceiverRequestAdmin(admin.ModelAdmin):
    list_display = ('user','receiver_name', 'blood_group', 'units_required',  'contact_number', 'is_approved')
admin.site.register(ReceiverRequest, ReceiverRequestAdmin)
admin.site.register(ContactMessage)

class DiagnosticOrderView(admin.ModelAdmin):
    list_display = ('patient_name', 'payment_amount')

admin.site.register(DiagnosticOrder, DiagnosticOrderView)
