from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SurveyTrip
from .serializers import SurveyTripSerializer

class SurveyTripViewSet(viewsets.ModelViewSet):
    queryset = SurveyTrip.objects.all()
    serializer_class = SurveyTripSerializer
    permission_classes = []  # Empty list for no authentication requirement