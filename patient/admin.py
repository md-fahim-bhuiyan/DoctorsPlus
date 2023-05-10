from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)


class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'units_required', 'location', 'contact_number', 'is_approved', 'created_at')

admin.site.register(DonationRequest, DonationRequestAdmin)
