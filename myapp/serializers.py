from rest_framework import serializers
from .models import Trip, TripBill

class TripBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripBill
        fields = ['id', 'image']

class TripSerializer(serializers.ModelSerializer):
    bills = TripBillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Trip
        fields = [
            'id', 'surveyor_name', 'driver_name', 'start_odometer_reading', 
            'vehicle_number', 'start_date', 'start_location',
            'end_odometer_reading', 'end_location', 'end_date',
            'bills'
        ]
    
    def create(self, validated_data):
        return Trip.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # Update trip fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Handle bill images
        bill_images = self.context['request'].FILES.getlist('bill_images')
        if bill_images:
            for image in bill_images:
                TripBill.objects.create(trip=instance, image=image)
        
        return instance






