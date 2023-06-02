from django.db import models
from patient.models import DiagnosticOrder
from adminView.models import Diagnostic


class TestResult(models.Model):
    test_name = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    order = models.ForeignKey(DiagnosticOrder, on_delete=models.CASCADE)
    result = models.CharField(max_length=100)
    normal_result = models.CharField(max_length=100, default='')
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.test_name.test_name} - Order ID: {self.order.pk}"
