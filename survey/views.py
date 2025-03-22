from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Survey
from .serializers import SurveySerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    @action(detail=False, methods=['post'])
    def start_survey(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def end_survey(self, request):
        vehicle_number = request.data.get('vehicle_number')
        
        if not vehicle_number:
            return Response(
                {"error": "Vehicle number is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            # Find the survey with the given vehicle number and empty end details
            survey = Survey.objects.get(
                vehicle_number=vehicle_number,
                end_time__isnull=True,
                end_odometer__isnull=True
            )
            
            # Update end details
            survey.end_time = request.data.get('end_time')
            survey.end_odometer = request.data.get('end_odometer')
            survey.save()
            
            return Response(SurveySerializer(survey).data, status=status.HTTP_200_OK)
            
        except Survey.DoesNotExist:
            return Response(
                {"error": "No matching survey found with empty end details"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )