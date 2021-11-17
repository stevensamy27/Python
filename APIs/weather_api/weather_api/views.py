from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    api_url = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
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
