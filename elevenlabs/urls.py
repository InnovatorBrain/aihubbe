from django.urls import path
from .views import ElevenLabs

urlpatterns = [
    path('eleven/', ElevenLabs, name='ElevenLabs'),
]
