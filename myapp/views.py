from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Trip, TripBill
from .serializers import TripSerializer
from django.shortcuts import render

def form(request):
    return render(request, 'bill.html')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    parser_classes = [MultiPartParser, FormParser]  # Allow file uploads

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the Trip instance being updated
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Save the updated trip details
        self.perform_update(serializer)

        # Handle bill images
        bill_images = request.FILES.getlist('bill_images')  # Get uploaded bill images
        if bill_images:
            # Delete existing bills for this trip (optional, if you want to replace old bills)
            instance.bills.all().delete()

            # Create new TripBill objects for the uploaded images
            for image in bill_images:
                TripBill.objects.create(trip=instance, image=image)

        return Response(serializer.data, status=status.HTTP_200_OK)

