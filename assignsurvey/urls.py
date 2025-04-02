from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyTripViewSet

router = DefaultRouter()
router.register(r'trips', SurveyTripViewSet)

app_name = 'assignsurvey'

urlpatterns = [
    path('', include(router.urls)),
]