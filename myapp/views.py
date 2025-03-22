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


