# Generated by Django 5.1.7 on 2025-03-24 07:53

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripbill',
            name='image',
            field=models.ImageField(storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='trip_bills/'),
        ),
    ]
