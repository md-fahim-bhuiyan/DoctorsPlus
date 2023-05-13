from django.contrib import admin

from .models import *
# Register your models here.

class doctorview(admin.ModelAdmin):
    list_display = ('full_name','user','bmdc','mobile', 'gender', 'specialist')

admin.site.register(Doctor, doctorview)
