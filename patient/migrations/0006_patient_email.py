# Generated by Django 4.1.7 on 2023-04-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_alter_patient_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]