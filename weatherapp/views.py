from django.shortcuts import render

from django.shortcuts import render
from .utils import get_weather_by_coordinates

def weather_view(request):
    api_key ="ff7886c96bcde2ab71eab1f93c890b52"
    latitude = 30.1864
    longitude = 71.4886
    weather_data = get_weather_by_coordinates(latitude, longitude, api_key)
    print(f'weather data{weather_data}')  # Log the data to the console for debugging
    
    context = {
        'weather': weather_data,
    }
    return render(request, 'weather/index.html', context)
