from django.db import models

# Create your models here.
class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup
    

class Diagnostic(models.Model):
    CATEGORY_CHOICES = (
        ('blood', 'Blood'),
        ('urine', 'Urine'),
        ('other', 'Other'),
    )

    test_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=200)
