from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('doctor_registration', views.doctor_registration, name='doctor_registration'),
    path('patient_registration', views.patient_registration, name='patient_registration'),

]