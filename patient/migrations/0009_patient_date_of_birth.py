# Generated by Django 3.2 on 2023-04-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_remove_patient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]