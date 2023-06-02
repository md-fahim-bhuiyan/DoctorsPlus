# Generated by Django 4.2.1 on 2023-06-02 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminView', '0003_alter_diagnostic_category_alter_diagnostic_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=100)),
                ('remarks', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminView.diagnostic')),
            ],
        ),
    ]
