from django.urls import path
from . import views

urlpatterns = [
    path('donor-dashboard/', views.donor_dashboard_view, name='donor-dashboard'),
    
]
