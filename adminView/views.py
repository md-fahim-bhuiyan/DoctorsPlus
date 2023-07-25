from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomLoginForm, DiagnosticForm
from patient.models import DonationRequest, ReceiverRequest, DiagnosticOrder
from .forms import DonationRequestForm, ReceiverRequestForm
from . import forms, models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.db.models import Sum
from .models import Stock, Diagnostic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm


def admin_dashboard(request):
    return render (request, "admin/dashboard.html")


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

def diagnostic_details_admin(request):
    orders = DiagnosticOrder.objects.filter()
    return render(request, 'diagnostics/diagnostic_details_admin.html', {'orders': orders})


class DiagnosticOrderDetailViewAdmin(DetailView):
    model = DiagnosticOrder
    template_name = 'diagnostics/order_Details_admin.html'
    context_object_name = 'order'

# views.py

# from django.shortcuts import render
from django.http import HttpResponse
# from patient.models import Appointment, User  # Import the necessary models

# def generate_report(request):
#     # Retrieve the data for the report
#     total_appointments = Appointment.objects.count()
#     total_users = User.objects.count()

#     # Generate the report content
#     report_content = f"Total Appointments: {total_appointments}\n"
#     report_content += f"Total Users: {total_users}\n"

#     # Create the HTTP response with the report content
#     response = HttpResponse(report_content, content_type='text/plain')
#     response['Content-Disposition'] = 'attachment; filename="admin_report.pdf"'

#     return response

from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from patient.models import Appointment, User, DonationRequest, ReceiverRequest ,DiagnosticOrder
from doctor.models import Doctor
from django.contrib.auth import get_user_model

def generate_report(request):
    total_appointments = Appointment.objects.count()
    total_users = User.objects.count()
    total_admin = get_user_model().objects.filter(is_staff=True).count()
    total_doctors = Doctor.objects.count()
    total_patients = total_users - total_doctors - total_admin
    total_diagnostic_order = DiagnosticOrder.objects.count()
    total_donate_request = DonationRequest.objects.count()
    total_donate_request_approve = DonationRequest.objects.filter(is_approved='APPROVED').count()
    total_donate_request_reject = DonationRequest.objects.filter(is_approved='REJECT').count()
    total_donate_request_pending = total_donate_request - total_donate_request_approve - total_donate_request_reject

    total_receiver_request = ReceiverRequest.objects.count()
    total_receiver_request_approve = ReceiverRequest.objects.filter(is_approved='APPROVED').count()
    total_receiver_request_reject = ReceiverRequest.objects.filter(is_approved='REJECT').count()
    total_receiver_request_pending = total_receiver_request - total_receiver_request_approve - total_receiver_request_reject

    buffer = BytesIO()
    report = canvas.Canvas(buffer, pagesize=(600, 800))  # Specify the page size here
    report.setTitle("Admin Report")
    report.setFont("Helvetica", 12)
    report.drawString(50, 750, "Number of User:")
    report.drawString(50, 730, "Total Users: " + str(total_users))
    report.drawString(50, 710, "Total Admins: " + str(total_admin))
    report.drawString(50, 690, "Total Doctors: " + str(total_doctors))
    report.drawString(50, 670, "Total Patients: " + str(total_patients))


    report.drawString(50, 630, "Total Appointments: " + str(total_appointments))
    report.drawString(50, 600, "Total Diagnostic Order: " + str(total_diagnostic_order))

    report.drawString(50, 500, "Blood Bank:")
    report.drawString(50, 480, "Blood Bank Donate Info:")
    report.drawString(50, 460, "Total Donate Request: " + str(total_donate_request))
    report.drawString(50, 440, "APPROVE: " + str(total_donate_request_approve))
    report.drawString(50, 420, "PENDING: " + str(total_donate_request_pending))
    report.drawString(50, 400, "REJECT: " + str(total_donate_request_reject))

    report.drawString(50, 380, "Blood Bank Receiver Info:")
    report.drawString(50, 360, "Total Receiver Request: " + str(total_receiver_request))
    report.drawString(50, 340, "APPROVE: " + str(total_receiver_request_approve))
    report.drawString(50, 320, "PENDING: " + str(total_receiver_request_pending))
    report.drawString(50, 300, "REJECT: " + str(total_receiver_request_reject))


    report.showPage()
    report.save()
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="admin_report.pdf"'

    return response
