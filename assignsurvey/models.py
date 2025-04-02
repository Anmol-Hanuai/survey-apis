# assignsurvey/models.py
from django.db import models

class SurveyTrip(models.Model):
    trip_id = models.CharField(max_length=50, unique=True)
    surveyor_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date = models.DateField()
    vehicle_number = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Trip {self.trip_id} - {self.date}"
    
    class Meta:
        ordering = ['-date']