from django.urls import path
from .views import CollectWeatherData, CheckProgress

urlpatterns = [
    path('collect/', CollectWeatherData.as_view(), name='collect-weather-data'),
    path('progress/<str:user_defined_id>/', CheckProgress.as_view(), name='check-progress'),
]
