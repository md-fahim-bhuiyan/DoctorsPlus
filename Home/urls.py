from django.contrib import admin
from django.urls import path
from . import views
from .views import UpdatePrescriptionView, PrescriptionDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('create_result/<int:pk>/', views.TestResultCreateView.as_view(), name='create_result'),
    # path('view_result/<int:pk>/', views.TestResultDetailView.as_view(), name='view_result'),
    # path('edit_result/<int:pk>/', views.TestResultUpdateView.as_view(), name='edit_result'),
    path('appointments/<uuid:appointment_id>/create-prescription/', views.create_prescription, name='create-prescription'),
    path('create-prescription/', views.create_prescription, name='create_prescription'),
    path('prescription-success/', views.prescription_success, name='prescription_success'),
    path('prescription/<str:appointment_id>/edit/', UpdatePrescriptionView.as_view(), name='edit_prescription'),
    path('prescription/<str:appointment_id>/view/', PrescriptionDetailView.as_view(), name='prescription_detail'),

]

