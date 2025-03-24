from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, form

router = DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('form/', form)
]

# Serve media files during development and on Render
if settings.DEBUG or True:  # Always serve media files, even in production
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
