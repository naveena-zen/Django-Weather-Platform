from django.shortcuts import render
import requests

def home(request):
    city = request.GET.get('city', 'Chennai')  # default city

    api_key = 'YOUR_REAL_API_KEY'  # 🔴 PUT YOUR KEY HERE

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        weather_data = {
            'city': city,
            'temperature': 'N/A',
            'description': 'City not found',
            'icon': '',
        }
    else:
        weather_data = {
           "temperature": data["main"]["temp"],
           "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
}

    return render(request, 'dashboard/home.html', {'weather_data': weather_data})