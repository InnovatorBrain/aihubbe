from rest_framework.urls import path
from .views import ChatAPIView

urlpatterns = [
    path("", ChatAPIView.as_view(), name="chat"),
]
