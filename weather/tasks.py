import requests
from time import sleep
from celery import shared_task
from django.utils import timezone
from .models import WeatherData
from weather_api_wrapper.settings import (
    OPEN_WEATHER_API_KEY,
    CITIES_LIST,
)

@shared_task
def fetch_weather_data(user_defined_id):

    for city_id in CITIES_LIST:
        url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={OPEN_WEATHER_API_KEY}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            WeatherData.objects.create(
                user_defined_id=user_defined_id,
                city_id=city_id,
                temperature_celsius=data['main']['temp'],
                humidity=data['main']['humidity'],
                request_time=timezone.now()
            )
        sleep(1) # Avoid hitting the API rate limit
