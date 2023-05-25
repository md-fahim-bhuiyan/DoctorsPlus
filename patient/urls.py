from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
from .views import MyPasswordChangeView


urlpatterns = [
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html'),name='patientlogin'),
    path('patientsignup', views.patient_signup_view,name='patientsignup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.patient_edit_profile,name='patient_edit_profile'),
    path('search/', views.search_results, name='search_results'),
    path('book_appointment/<int:doctor_pk>/<str:doctor_name>/', views.book_appointment, name='book_appointment'),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('bloodbank', views.bloodbank, name='bloodbank'),
    path('donation/request/', views.create_donation_request, name='create_donation_request'),
    path('donation/requests/', views.view_donation_requests, name='view_donation_requests'),
    path('donation/requests/<int:pk>/approve/', views.approve_donation_request, name='approve_donation_request'),
    path('donation/requests/<int:pk>/reject/', views.reject_donation_request, name='reject_donation_request'),
    path('doner_dashboard',views.doner_dashboard, name='doner_dashboard'),
    path('blood_receiver_dashboard', views.blood_receiver_dashboard, name='blood_receiver_dashboard'),
    path('receiver-request/create/', views.receiver_request_create_view, name='receiver_request_create'),
    path('receiver-request/success/', views.receiver_request_success_view, name='receiver_request_success'),
    path('receiver-request/list/', views.receiver_request_list_view, name='receiver_request_list'),
    path('change-password/', MyPasswordChangeView.as_view(), name='change_password'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('about/', views.about, name='about'),
    path('payment/', views.payment, name='payment'),
    path('process-payment/', views.process_payment, name='process-payment'),
    path('appointment-details/', views.appointment_details, name='appointment-details'),



]