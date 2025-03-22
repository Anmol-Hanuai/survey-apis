from rest_framework import serializers
from .models import Trip, TripBill

class TripBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripBill
        fields = ['id', 'image']

class TripSerializer(serializers.ModelSerializer):
    bills = TripBillSerializer(many=True, read_only=True)
    bill_images = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,  # This field is only for input, not output
        required=False,
    )

    class Meta:
        model = Trip
        fields = [
            'id', 'surveyor_name', 'driver_name', 'start_odometer_reading', 
            'vehicle_number', 'start_date', 'start_location',
            'end_odometer_reading', 'end_location', 'end_date',
            'bills', 'bill_images'  # Add bill_images to fields
        ]

    def update(self, instance, validated_data):
        # Remove bill_images from validated_data to avoid errors
        bill_images = validated_data.pop('bill_images', None)

        # Update trip fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle bill images
        if bill_images:
            for image in bill_images:
                TripBill.objects.create(trip=instance, image=image)

        return instance






