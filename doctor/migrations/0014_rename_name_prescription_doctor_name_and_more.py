# Generated by Django 4.2.1 on 2023-05-27 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_remove_test_prescription_remove_prescription_doctor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='name',
            new_name='doctor_name',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='eat_time',
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_blood_pressure',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='specialty',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=255)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(max_length=255)),
                ('dose', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], max_length=20)),
                ('duration', models.CharField(max_length=50)),
                ('eat_time', models.CharField(max_length=10)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
            ],
        ),
    ]
