from django.urls import path
from . import views

app_name="weatherapp"
urlpatterns = [
    
    path('',views.weather_view,name='index')
]
