# Generated by Django 5.1.7 on 2025-03-21 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyor_name', models.CharField(max_length=100)),
                ('driver_name', models.CharField(max_length=100)),
                ('start_odometer_reading', models.IntegerField()),
                ('vehicle_number', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('start_location', models.CharField(max_length=255)),
                ('end_odometer_reading', models.IntegerField(blank=True, null=True)),
                ('end_location', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='trip_bills/')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='myapp.trip')),
            ],
        ),
    ]
