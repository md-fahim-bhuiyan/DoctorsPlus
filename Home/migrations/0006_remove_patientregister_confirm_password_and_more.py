# Generated by Django 4.1.7 on 2023-04-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_remove_patientregister_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientregister',
            name='confirm_password',
        ),
        migrations.AlterField(
            model_name='patientregister',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
