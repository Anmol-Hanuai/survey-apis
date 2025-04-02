# assignsurvey/serializers.py
from rest_framework import serializers
from .models import SurveyTrip

class SurveyTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyTrip
        fields = ['id', 'trip_id', 'surveyor_name', 'driver_name', 
                 'location', 'date', 'vehicle_number']