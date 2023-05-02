from django.contrib import admin

from .models import *
# Register your models here.
# admin.site.register(Donor)
admin.site.register(Receiver)
admin.site.register(BloodDonate)
admin.site.register(Stock)
admin.site.register(BloodRequest)
