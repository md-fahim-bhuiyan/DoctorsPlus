# Generated by Django 4.2.1 on 2023-05-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_donationrequest_doner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequest',
            name='is_approved',
            field=models.CharField(choices=[('APPROVE', 'APPROVE'), ('PANDING', 'PANDING'), ('REJECT', 'REJECT')], default='PANDING', max_length=8),
        ),
    ]
