# Generated by Django 4.1.7 on 2023-04-16 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_address_remove_patient_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='user',
            new_name='email',
        ),
    ]