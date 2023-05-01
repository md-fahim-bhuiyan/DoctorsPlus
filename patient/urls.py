from django.urls import path

from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html'),name='patientlogin'),
    path('patientsignup', views.patient_signup_view,name='patientsignup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('profile/edit/', views.patient_edit_profile,name='patient_edit_profile'),
    path('search/', views.search_results, name='search_results'),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
]