from django.urls import path
from .views import PlaceHolderListAPIView

urlpatterns = [
    path('', PlaceHolderListAPIView.as_view())
]
