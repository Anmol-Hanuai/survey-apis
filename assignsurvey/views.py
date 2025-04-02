from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SurveyTrip
from .serializers import SurveyTripSerializer

class SurveyTripViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows survey trips to be viewed or edited.
    """
    queryset = SurveyTrip.objects.all()
    serializer_class = SurveyTripSerializer
    permission_classes = [IsAuthenticated]