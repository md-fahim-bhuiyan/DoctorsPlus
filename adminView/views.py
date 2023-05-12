from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')