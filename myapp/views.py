# views.py
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Trip, TripBill
from .serializers import TripSerializer
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def form(request):
    return render(request, 'bill.html')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    parser_classes = [MultiPartParser, FormParser]  # Allow file uploads

    def partial_update(self, request, *args, **kwargs):
        logger.debug(f"Request data: {request.data}")
        logger.debug(f"Request FILES: {request.FILES}")
        
        instance = self.get_object()  # Get the Trip instance being updated
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Save the updated trip details
        self.perform_update(serializer)

        # Handle bill images
        bill_images = request.FILES.getlist('bill_images')  # Get uploaded bill images
        logger.debug(f"Bill images: {bill_images}")
        
        if bill_images:
            # Delete existing bills for this trip (optional)
            # Uncomment if you want to replace old bills
            # instance.bills.all().delete()

            # Create new TripBill objects for the uploaded images
            for image in bill_images:
                try:
                    bill = TripBill.objects.create(trip=instance, image=image)
                    logger.debug(f"Created bill with image URL: {bill.image.url}")
                except Exception as e:
                    logger.error(f"Error creating bill: {e}")

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        logger.debug(f"Create request data: {request.data}")
        logger.debug(f"Create request FILES: {request.FILES}")
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trip = serializer.save()
        
        # Handle bill images during creation
        bill_images = request.FILES.getlist('bill_images')
        logger.debug(f"Bill images during creation: {bill_images}")
        
        if bill_images:
            for image in bill_images:
                try:
                    bill = TripBill.objects.create(trip=trip, image=image)
                    logger.debug(f"Created bill with image URL: {bill.image.url}")
                except Exception as e:
                    logger.error(f"Error creating bill: {e}")
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


