# Generated by Django 5.1.7 on 2025-04-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=50, unique=True)),
                ('surveyor_name', models.CharField(max_length=100)),
                ('driver_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('vehicle_number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
