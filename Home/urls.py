from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('patientlogin', views.patientlogin, name='patientlogin'),
    # path('patientregister', views.patientregister, name='patientregister'),
    path('logout', views.logout, name='logout'),
]