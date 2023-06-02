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
