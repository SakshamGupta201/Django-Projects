
import os
import requests
from django.shortcuts import render
from django.utils import timezone
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


def home(request):
    
    city = request.POST.get('city', 'Delhi')

    API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    params = {'units': 'metric'}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network issues, invalid responses)
        description = 'Error fetching weather data'
        icon = 'unknown'
        temp = 'N/A'
        print(f"Error: {e}")

    day = timezone.now().strftime('%A')

    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city
    }

    return render(request, 'home.html', context)
