from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Trip
from .serializers import TripSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    parser_classes = [MultiPartParser, FormParser]  # Allow file uploads

