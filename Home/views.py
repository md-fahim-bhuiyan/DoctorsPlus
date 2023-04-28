from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'Home/index.html')

@login_required
def profile(request):
    return render(request, 'patient/success.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')