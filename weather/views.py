from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData
from .tasks import fetch_weather_data
from weather_api_wrapper.settings import LEN_CITIES_LIST
from drf_yasg.utils import swagger_auto_schema
from .swagger import (
    collect_weather_data_schema,
    collect_weather_responses,
    check_progress_responses
)

class CollectWeatherData(APIView):

    @swagger_auto_schema(
        request_body=collect_weather_data_schema,
        responses=collect_weather_responses
    )
    def post(self, request):
        user_defined_id = request.data.get('user_defined_id')
        
        if not user_defined_id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        if WeatherData.objects.filter(user_defined_id=user_defined_id).exists():
            return Response({"error": "ID already exists"}, status=status.HTTP_400_BAD_REQUEST)

        fetch_weather_data.delay(user_defined_id)

        return Response({"message": "Data collection initiated", "id": user_defined_id}, status=status.HTTP_202_ACCEPTED)


class CheckProgress(APIView):

    @swagger_auto_schema(
        responses=check_progress_responses
    )
    def get(self, request, user_defined_id):
        if not WeatherData.objects.filter(user_defined_id=user_defined_id).exists():
            return Response({"error": "ID not found"}, status=status.HTTP_404_NOT_FOUND)

        collected_count = WeatherData.objects.filter(user_defined_id=user_defined_id).count()
        progress_percentage = (collected_count / LEN_CITIES_LIST) * 100

        return Response({"progress": f"{progress_percentage}%"})
