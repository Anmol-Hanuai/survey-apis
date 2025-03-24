from rest_framework import serializers
from .models import Trip, TripBill  # Import your models
import cloudinary  # For handling Cloudinary images (if used)
import logging  # For proper error logging
from cloudinary.utils import cloudinary_url

logger = logging.getLogger(__name__)

class TripBillSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = TripBill
        fields = ["id", "image"]

    def get_image(self, obj):
        try:
            if obj.image:
                public_id = getattr(obj.image, "public_id", None)
                print(f"Public ID: {public_id}")  # Debugging log

                if public_id:
                    url, _ = cloudinary_url(public_id, secure=True)
                    return url
                
                return obj.image.url  # Fallback (if Cloudinary URL is already set)
        except Exception as e:
            print(f"Error fetching image URL: {e}")

        return None

class TripSerializer(serializers.ModelSerializer):
    bills = TripBillSerializer(many=True, read_only=True)
    bill_images = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Trip
        fields = [
            'id', 'surveyor_name', 'driver_name', 'start_odometer_reading', 
            'vehicle_number', 'start_date', 'start_location',
            'end_odometer_reading', 'end_location', 'end_date',
            'bills', 'bill_images'
        ]






