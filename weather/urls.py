from django.urls import path
from .views import CollectWeatherData, CheckProgress
from .swagger import schema_view

urlpatterns = [
    path('collect/', CollectWeatherData.as_view(), name='collect-weather-data'),
    path('progress/<str:user_defined_id>/', CheckProgress.as_view(), name='check-progress'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
