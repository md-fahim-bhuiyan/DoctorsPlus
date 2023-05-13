from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomLoginForm
from patient.models import DonationRequest, ReceiverRequest
from .forms import DonationRequestForm
from . import forms,models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect

class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def bloodbank_index(request):
    dict={
        'bloodForm':forms.BloodForm(),
        'A1':models.Stock.objects.get(bloodgroup="A+"),
        'A2':models.Stock.objects.get(bloodgroup="A-"),
        'B1':models.Stock.objects.get(bloodgroup="B+"),
        'B2':models.Stock.objects.get(bloodgroup="B-"),
        'AB1':models.Stock.objects.get(bloodgroup="AB+"),
        'AB2':models.Stock.objects.get(bloodgroup="AB-"),
        'O1':models.Stock.objects.get(bloodgroup="O+"),
        'O2':models.Stock.objects.get(bloodgroup="O-"),
    }
    return render(request, 'admin/bloodbank_index.html',context=dict)

def admin_view_donation_requests(request):
    donation_requests = DonationRequest.objects.all().order_by('-created_at')
    return render(request, 'admin/admin_view_donation_requests.html', {'requests': donation_requests})


def admin_edit_donation_request(request, request_id):
    donation_request = get_object_or_404(DonationRequest, id=request_id)

    if request.method == 'POST':
        form = DonationRequestForm(request.POST, instance=donation_request)
        if form.is_valid():
            form.save()
            return redirect('admin_view_donation_requests')
    else:
        form = DonationRequestForm(instance=donation_request)

    return render(request, 'admin/admin_edit_donation_request.html', {'form': form})

def admin_receiver_request_list(request):
    return render (request ,'admin/admin_receiver_request_list.html')


@login_required
def admin_blood_view(request):
    dict={
        'bloodForm':forms.BloodForm(),
        'A1':models.Stock.objects.get(bloodgroup="A+"),
        'A2':models.Stock.objects.get(bloodgroup="A-"),
        'B1':models.Stock.objects.get(bloodgroup="B+"),
        'B2':models.Stock.objects.get(bloodgroup="B-"),
        'AB1':models.Stock.objects.get(bloodgroup="AB+"),
        'AB2':models.Stock.objects.get(bloodgroup="AB-"),
        'O1':models.Stock.objects.get(bloodgroup="O+"),
        'O2':models.Stock.objects.get(bloodgroup="O-"),
    }
    if request.method=='POST':
        bloodForm=forms.BloodForm(request.POST)
        if bloodForm.is_valid() :        
            bloodgroup=bloodForm.cleaned_data['bloodgroup']
            stock=models.Stock.objects.get(bloodgroup=bloodgroup)
            stock.unit=bloodForm.cleaned_data['unit']
            stock.save()
        return HttpResponseRedirect('admin-blood')
    return render(request,'admin/admin_blood.html',context=dict)