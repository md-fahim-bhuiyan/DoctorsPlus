from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import PatientRegister

def home(request):
    return render(request, 'Home/index.html')

# def patientregister(request):
#     if request.method == 'POST':
#         form = PatientRegister(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = PatientRegister()
#         context = {'form': form}
#         return render(request, 'patientregister.html', context)


# def patientlogin(request):
#     return render (request, 'patientlogin.html')

def logout(request):
    auth.logout(request)
    return redirect('home')