from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData
from .tasks import fetch_weather_data

class CollectWeatherData(APIView):
    
    def post(self, request):
        user_defined_id = request.data.get('user_defined_id')
        
        if not user_defined_id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        if WeatherData.objects.filter(id=id).exists():
            return Response({"error": "ID already exists"}, status=status.HTTP_400_BAD_REQUEST)

        fetch_weather_data.delay(id)

        return Response({"message": "Data collection initiated", "id": str(id)}, status=status.HTTP_202_ACCEPTED)

