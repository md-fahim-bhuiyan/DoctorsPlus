from django.urls import path
from .views import MyPasswordChangeView
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('doctorlogin/', LoginView.as_view(template_name='doctor/doctorlogin.html'),name='doctorlogin'),
    path('doctorsignup/', views.doctor_signup_view,name='doctorsignup'),
    path('profile/', views.docProfile, name='docProfile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor-dashboard'),
    path('change-password/', MyPasswordChangeView.as_view(), name='doc_change_password'),
    path('about/', views.about, name='doc_about'),
    path('contact/', views.contact, name='doc_contact'),
    path('contact/success/', views.contact_success, name='doc_contact_success'),
    path('appointments/', views.doctor_appointments, name='doc_appointments'),

]
