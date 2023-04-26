from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html'),name='patientlogin'),
    path('patientsignup', views.patient_signup_view,name='patientsignup'),
    # path('patient/success/', views.patient_success_view, name='patient_success'),

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    # path('logout', views.logout, name='logout'),
    # path('make-request', views.make_request_view,name='make-request'),
    # path('my-request', views.my_request_view,name='my-request'),
]