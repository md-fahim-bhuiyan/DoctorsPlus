from django import forms
from .models import TestResult
from adminView.models import Diagnostic
# from patient.models import DiagnosticOrder

class TestResultForm(forms.ModelForm):
    test_name = forms.ModelChoiceField(queryset=Diagnostic.objects.all())
    # order = forms.ModelChoiceField(queryset=DiagnosticOrder.objects.all())

    class Meta:
        model = TestResult
        fields = ['test_name', 'result','normal_result', 'remarks']
    def __init__(self, *args, **kwargs):
        order = kwargs.pop('order', None)
        super().__init__(*args, **kwargs)
        if order:
            self.fields['test_name'].initial = order.diagnostic    