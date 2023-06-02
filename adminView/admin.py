from django.contrib import admin

# Register your models here.
from .models import *
from Home.models import TestResult
admin.site.register(Stock)
admin.site.register(Diagnostic)
admin.site.register(TestResult)
