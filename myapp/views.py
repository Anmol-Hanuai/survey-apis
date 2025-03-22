from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Trip, TripBill
from .serializers import TripSerializer
from django.shortcuts import render

def form(request):
    return render(request, 'bill.html')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def update_end_details(self, request):
        vehicle_number = request.data.get('vehicle_number')
        
        if not vehicle_number:
            return Response(
                {"error": "Vehicle number is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            # Find the trip with the given vehicle number and empty end details
            trip = Trip.objects.get(
                vehicle_number=vehicle_number,
                end_date__isnull=True
            )
            
            # Validate end_odometer_reading
            end_odometer_reading = request.data.get('end_odometer_reading')
            if end_odometer_reading == '' or end_odometer_reading is None:
                return Response(
                    {"error": "End odometer reading is required."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not str(end_odometer_reading).isdigit():
                return Response(
                    {"error": "Invalid end odometer reading. Please provide a valid integer."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update end details
            trip.end_odometer_reading = int(end_odometer_reading)
            trip.end_location = request.data.get('end_location')
            trip.end_date = request.data.get('end_date')
            trip.save()
            
            # Handle bill images
            bill_images = request.FILES.getlist('bill_images')
            if bill_images:
                for image in bill_images:
                    TripBill.objects.create(trip=trip, image=image)
            
            return Response(TripSerializer(trip).data, status=status.HTTP_200_OK)
            
        except Trip.DoesNotExist:
            return Response(
                {"error": "No matching trip found with empty end details"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


