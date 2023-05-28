from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomLoginForm
from patient.models import DonationRequest, ReceiverRequest
from .forms import DonationRequestForm, ReceiverRequestForm
from . import forms, models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.db.models import Sum
from .models import Stock
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


def bloodbank_index(request):
    totaldonors = DonationRequest.objects.count()
    totalrequest = ReceiverRequest.objects.count()
    totalbloodunit = Stock.objects.aggregate(total=Sum('unit')).get('total', 0)
    totalapprovedrequest = ReceiverRequest.objects.filter(
        is_approved='APPROVED').count()

    context = {
        'totaldonors': totaldonors,
        'totalrequest': totalrequest,
        'totalbloodunit': totalbloodunit,
        'totalapprovedrequest': totalapprovedrequest,
    }

    dict = {
        'bloodForm': forms.BloodForm(),
        'A1': models.Stock.objects.get(bloodgroup="A+"),
        'A2': models.Stock.objects.get(bloodgroup="A-"),
        'B1': models.Stock.objects.get(bloodgroup="B+"),
        'B2': models.Stock.objects.get(bloodgroup="B-"),
        'AB1': models.Stock.objects.get(bloodgroup="AB+"),
        'AB2': models.Stock.objects.get(bloodgroup="AB-"),
        'O1': models.Stock.objects.get(bloodgroup="O+"),
        'O2': models.Stock.objects.get(bloodgroup="O-"),
    }
    return render(request, 'admin/bloodbank_index.html', context={**context, **dict})


def admin_view_donation_requests(request):
    donation_requests = DonationRequest.objects.all().order_by('-created_at')
    return render(request, 'admin/admin_view_donation_requests.html', {'requests': donation_requests})


def admin_edit_donation_request(request, request_id):
    donation_request = get_object_or_404(DonationRequest, id=request_id)

    if request.method == 'POST':
        form = DonationRequestForm(request.POST, instance=donation_request)
        if form.is_valid():
            donation_request = form.save(commit=False)
            if donation_request.is_approved == 'APPROVED':
                blood_group = donation_request.blood_group
                units_donated = donation_request.units_required
                stock, created = Stock.objects.get_or_create(
                    bloodgroup=blood_group)
                stock.unit += units_donated
                stock.save()
            donation_request.save()
            return redirect('admin_view_donation_requests')
    else:
        form = DonationRequestForm(instance=donation_request)

    return render(request, 'admin/admin_edit_donation_request.html', {'form': form})


def admin_edit_receiver_request(request, request_id):
    receiver_request = get_object_or_404(ReceiverRequest, id=request_id)

    if request.method == 'POST':
        form = ReceiverRequestForm(request.POST, instance=receiver_request)
        if form.is_valid():
            receiver_request = form.save(commit=False)
            if receiver_request.is_approved == 'APPROVED':
                blood_group = receiver_request.blood_group
                units_required = receiver_request.units_required
                stock, created = Stock.objects.get_or_create(
                    bloodgroup=blood_group)
                stock.unit -= units_required
                stock.save()
            receiver_request.save()
            return redirect('admin_receiver_request_list')
    else:
        form = ReceiverRequestForm(instance=receiver_request)

    return render(request, 'admin/admin_edit_receiver_request.html', {'form': form})


def admin_receiver_request_list(request):
    receiver_requests = ReceiverRequest.objects.all().order_by('-created_at')
    return render(request, 'admin/admin_receiver_request_list.html', {'requests': receiver_requests})


@login_required
def admin_blood_view(request):
    dict = {
        'bloodForm': forms.BloodForm(),
        'A1': models.Stock.objects.get(bloodgroup="A+"),
        'A2': models.Stock.objects.get(bloodgroup="A-"),
        'B1': models.Stock.objects.get(bloodgroup="B+"),
        'B2': models.Stock.objects.get(bloodgroup="B-"),
        'AB1': models.Stock.objects.get(bloodgroup="AB+"),
        'AB2': models.Stock.objects.get(bloodgroup="AB-"),
        'O1': models.Stock.objects.get(bloodgroup="O+"),
        'O2': models.Stock.objects.get(bloodgroup="O-"),
    }
    if request.method == 'POST':
        bloodForm = forms.BloodForm(request.POST)
        if bloodForm.is_valid():
            bloodgroup = bloodForm.cleaned_data['bloodgroup']
            stock = models.Stock.objects.get(bloodgroup=bloodgroup)
            stock.unit = bloodForm.cleaned_data['unit']
            stock.save()
        return HttpResponseRedirect('admin-blood')
    return render(request, 'admin/admin_blood.html', context=dict)


def about(request):
    return render(request, 'patient/about.html')


from django.views.generic import ListView, DetailView
from .models import Diagnostic
from .forms import DiagnosticForm

def create_diagnostic(request):
    if request.method == 'POST':
        form = DiagnosticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = DiagnosticForm()
    return render(request, 'diagnostics/create.html', {'form': form})

class DiagnosticListView(ListView):
    model = Diagnostic
    template_name = 'diagnostics/list.html'
    context_object_name = 'diagnostics'

class DiagnosticDetailView(DetailView):
    model = Diagnostic
    template_name = 'diagnostics/detail.html'
    context_object_name = 'diagnostic'

class DiagnosticUpdateView(UpdateView):
    model = Diagnostic
    template_name = 'diagnostics/update.html'
    form_class = DiagnosticForm
    context_object_name = 'diagnostic'
    success_url = reverse_lazy('list')


class DiagnosticDeleteView(DeleteView):
    model = Diagnostic
    template_name = 'diagnostics/delete.html'
    context_object_name = 'diagnostic'
    success_url = reverse_lazy('list')