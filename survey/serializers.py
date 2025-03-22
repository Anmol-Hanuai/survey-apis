from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'id', 'date', 'start_time', 'survey_location', 'start_odometer',
            'camera_position', 'reason_for_not_starting', 'vehicle_number',
            'end_time', 'end_odometer'
        ]