from django.urls import path
from .views import CollectWeatherData

urlpatterns = [
    path('collect/', CollectWeatherData.as_view(), name='collect-weather-data'),
]
