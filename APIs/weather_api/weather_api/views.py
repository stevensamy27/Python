import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm



# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    if cities:

        for city in cities:
            data_url = url + str(city)
            
            response = requests.get(url)

            city_weather ={

                'city' : city.name,
                'tempreature' : response['main']['temp'],
                'description':response['weather'][0]['description'],
                'icon':response['weather'][0]['icon']

            }


            weather_data.append(city_weather)


    return render(request, 'weather.html', {'weather_data': weather_data, 'form': form})
