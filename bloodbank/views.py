from django.shortcuts import render, redirect
from . import forms, models
from django.shortcuts import render

# Create your views here.


def donor_dashboard_view(request):
    return render(request, 'bloodbank/index.html')


def donate_blood_view(request):
    if request.method == 'POST':
        form = forms.DonorForm(request.POST)
        if form.is_valid():
            # Create a new BloodDonate object from the form data
            blooddonate = form.save(commit=False)

            # Set the donor based on the currently logged in user
            blooddonate.donor = models.Donor.objects.get(user=request.user)

            # Save the BloodDonate object to the database
            blooddonate.save()

            # Redirect to a success page
            return redirect('donate_success')
    else:
        form = forms.DonorForm()
    return render(request, 'donor/donate_blood.html', {'form': form})
