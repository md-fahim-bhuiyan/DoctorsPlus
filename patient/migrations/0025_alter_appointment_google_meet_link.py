# Generated by Django 4.2.1 on 2023-05-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0024_alter_appointment_consultation_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='google_meet_link',
            field=models.URLField(blank=True, default='https://meet.google.com/ehp-jepq-sym', null=True),
        ),
    ]
