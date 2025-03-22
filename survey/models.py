from django.db import models

class Survey(models.Model):
    # Start details
    date = models.DateField()
    start_time = models.TimeField()
    survey_location = models.CharField(max_length=255)
    start_odometer = models.IntegerField()
    camera_position = models.CharField(max_length=10, choices=[('front', 'Front'), ('back', 'Back')])
    reason_for_not_starting = models.TextField(blank=True, null=True)
    vehicle_number = models.CharField(max_length=50)

    # End details (nullable)
    end_time = models.TimeField(null=True, blank=True)
    end_odometer = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Survey for {self.vehicle_number} on {self.date}"