# Generated by Django 4.2.1 on 2023-05-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_donationrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationrequest',
            name='doner_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
