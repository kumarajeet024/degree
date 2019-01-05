import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f3cb19282c7c0636cccf91529010e64b'
    city = 'New Delhi'
    a = requests.get(url.format(city))
    print(a.text)
    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temprature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
        'wind' : r['wind']['speed'],
    }
    context = {'city_weather':city_weather}
    return render(request, 'weather/index.html', context)

