from rest_framework import viewsets
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

    def get_object(self):
        # Override get_object to handle the PATCH request correctly
        obj = super().get_object()
        return obj

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

