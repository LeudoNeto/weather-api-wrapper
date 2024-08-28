from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import WeatherData
from time import sleep

class CollectWeatherDataTest(APITestCase):
    def setUp(self):
        self.collect_weather_url = reverse('collect-weather-data')

    def test_post_valid_data(self):
        data = {
            "user_defined_id": "unique_id_123"
        }
        response = self.client.post(self.collect_weather_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn("Data collection initiated", response.data['message'])

    def test_post_no_id(self):
        response = self.client.post(self.collect_weather_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "ID is required")

    def test_post_duplicate_id(self):
        WeatherData.objects.create(
            user_defined_id="unique_id_123",
            city_id=123456,
            temperature_celsius=25.5,
            humidity=60.0
        )
        data = {
            "user_defined_id": "unique_id_123"
        }
        response = self.client.post(self.collect_weather_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "ID already exists")


class CheckProgressTest(APITestCase):
    def setUp(self):
        self.check_progress_url = lambda id: reverse('check-progress', kwargs={'user_defined_id': id})

    def test_get_valid_id(self):
        WeatherData.objects.create(
            user_defined_id="unique_id_123",
            city_id=123456,
            temperature_celsius=25.5,
            humidity=60.0
        )
        response = self.client.get(self.check_progress_url('unique_id_123'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("progress", response.data)

    def test_get_invalid_id(self):
        response = self.client.get(self.check_progress_url('invalid_id'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "ID not found")
