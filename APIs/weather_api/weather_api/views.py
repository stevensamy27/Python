from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    api_url = 'https://api.openweathermap.org./data/2.5/weather?appid='
    city_name = "Kuwait"

    url = api_url + city_name
    response = requests.get(url)
    content = response.json()

    city_weather ={

        'city' : city_name,
        'tempreature' : content['main']['temp'],
        'descreption':content['weahter'][0]['descreption'],
        'icon':content['weahter'][0]['icon']

    }

    return render(request, 'weather.html', city_weather)
