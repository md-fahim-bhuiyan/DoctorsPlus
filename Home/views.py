from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import TestResult
from .forms import TestResultForm
from django.urls import reverse_lazy
from patient.models import DiagnosticOrder
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView


def home(request):
    return render(request, 'Home/index.html')


@login_required
def profile(request):
    return render(request, 'Home/after_login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')


class TestResultCreateView(CreateView):
    model = TestResult
    form_class = TestResultForm
    template_name = 'diagnostics/create_result.html'
    success_url = reverse_lazy('diagnostic_details_admin')

    def form_valid(self, form):
        form.instance.order_id = self.kwargs['pk']
        return super().form_valid(form)



# class TestResultDetailView(DetailView):
#     model = TestResult
#     template_name = 'diagnostics/view_result.html'
#     context_object_name = 'test_result'



# class TestResultUpdateView(UpdateView):
#     model = TestResult
#     form_class = TestResultForm
#     template_name = 'diagnostics/edit_result.html'
#     success_url = reverse_lazy('diagnostic_details_admin')

#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset=queryset)
#         return obj

#     def form_valid(self, form):
#         form.instance.order_id = self.kwargs['pk']
#         return super().form_valid(form)



from django.shortcuts import render, redirect
from .forms import PrescriptionForm
from doctor.models import Doctor
from patient.models import Appointment
from .models import Prescription

def create_prescription(request, appointment_id):
    doctor = Doctor.objects.get(user_id=request.user)
    appointment = Appointment.objects.get(appointment_id=appointment_id)
    prescription_form = PrescriptionForm(request.POST or None)
    # medicine_forms = [MedicineForm(prefix=f'medicine_{i}') for i in range(5)]
    # test_forms = [TestForm(prefix=f'test_{i}') for i in range(5)]

    if request.method == 'POST':
        if prescription_form.is_valid():
            prescription = prescription_form.save(commit=False)
            prescription.patient = request.user
            prescription.appointment_id = appointment.appointment_id
            prescription.save()
            return redirect('prescription_success')

    context = {
        'prescription_form': prescription_form,
        'doctor': doctor, 
    }

    return render(request, 'doctor/create_prescription.html', context)
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from uuid import UUID


class UpdatePrescriptionView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'doctor/update_prescription.html'
    success_url = reverse_lazy('prescription_success')

    def get_object(self, queryset=None):
        appointment_id = self.kwargs['appointment_id']
        prescription = Prescription.objects.get(appointment_id=UUID(appointment_id))
        return prescription



class PrescriptionDetailView(DetailView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'doctor/prescription_detail.html'
    context_object_name = 'prescription'
    
    def get_object(self, queryset=None):
        appointment_id = self.kwargs['appointment_id']
        prescription = Prescription.objects.get(appointment_id=UUID(appointment_id))
        return prescription



def prescription_success(request):
    return render(request, 'doctor/prescription_success.html')