from django.db import models

class Trip(models.Model):
    # Start journey details
    surveyor_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    start_odometer_reading = models.IntegerField()
    vehicle_number = models.CharField(max_length=50)
    start_date = models.DateField()
    start_location = models.CharField(max_length=255)
    
    # End journey details (nullable)
    end_odometer_reading = models.IntegerField(null=True, blank=True)
    end_location = models.CharField(max_length=255, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.driver_name} - {self.vehicle_number} - {self.start_date}"

class TripBill(models.Model):
    trip = models.ForeignKey(Trip, related_name='bills', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trip_bills/')
    
    def __str__(self):
        return f"Bill for {self.trip}"





