# Generated by Django 3.2 on 2023-04-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_date_of_birth_remove_doctor_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='bloodgroup',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='doctor',
            name='bio',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='doctor',
            name='bmdc',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='consultation_fee',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialist',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
