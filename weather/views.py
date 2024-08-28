from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData
from .tasks import fetch_weather_data
from weather_api_wrapper.settings import LEN_CITIES_LIST

class CollectWeatherData(APIView):

    def post(self, request):
        user_defined_id = request.data.get('user_defined_id')
        
        if not user_defined_id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        if WeatherData.objects.filter(id=id).exists():
            return Response({"error": "ID already exists"}, status=status.HTTP_400_BAD_REQUEST)

        fetch_weather_data.delay(id)

        return Response({"message": "Data collection initiated", "id": str(id)}, status=status.HTTP_202_ACCEPTED)


class CheckProgress(APIView):

    def get(self, request, user_defined_id):
        if not WeatherData.objects.filter(user_defined_id=user_defined_id).exists():
            return Response({"error": "ID not found"}, status=status.HTTP_404_NOT_FOUND)

        collected_count = WeatherData.objects.filter(user_defined_id=user_defined_id).count()
        progress_percentage = (collected_count / LEN_CITIES_LIST) * 100

        return Response({"progress": f"{progress_percentage}%"})
