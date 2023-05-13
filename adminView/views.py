from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def bloodbank_index(request):
    return render(request, 'admin/bloodbank_index.html')

def admin_view_donation_requests(request):
    return render (request ,'admin/admin_view_donation_requests.html')

def admin_receiver_request_list(request):
    return render (request ,'admin/admin_receiver_request_list.html')