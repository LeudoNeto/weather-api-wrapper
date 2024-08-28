import uuid
from django.db import models

class WeatherData(models.Model):
    user_defined_id = models.CharField(max_length=255, help_text="User defined ID for this weather data")
    request_time = models.DateTimeField(auto_now_add=True, help_text="Time when the request was made")
    city_id = models.IntegerField(help_text="City ID from OpenWeatherMap API")
    temperature_celsius = models.FloatField(help_text="Temperature in Celsius")
    humidity = models.FloatField(help_text="Humidity in percentage")

    def __str__(self):
        return f"WeatherData for ID {self.id}"
