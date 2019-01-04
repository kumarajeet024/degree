import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f3cb19282c7c0636cccf91529010e64b'
    city = 'New Delhi'
    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'weather/index.html')

