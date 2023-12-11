from django.shortcuts import render
from .models import Weather
from django.http import HttpResponse
import requests
from .seralizers import Weatherseralizers
import datetime



def application(request):
    try:
        if request.method=='POST':
            city=request.POST['city']
            x=Weather(city=city)
            x.save()
        y=Weather.objects.all()
        serilizer=Weatherseralizers(y,many=True)
        l=serilizer.data
        try:
            current_city=l[-1]['city']
        except:
            current_city='mumbai'
        api = '1225f09c1a0407c6edd97e9f8f47baad'
        try:
            get_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={current_city}&units=imperial&APPID={api}").json()
            data={
                'city' : get_weather['name'],
                'temp' : float(get_weather['main']['temp']),
                'min_temp': float(get_weather['main']['temp_min']),
                'max_temp': float(get_weather['main']['temp_max']),
                'pressure': get_weather['main']['pressure'],
                'humidity': get_weather['main']['humidity'],
                'feels_like': float(get_weather['main']['feels_like']),
                'date': datetime.datetime.now()
            }
            return render(request,'sample.html',{'x':data})
        except:
            z = Weather(city='mumbai')
            z.save()
            return HttpResponse("<html><body> <h1 align='center'> City not found </h1> <h2> Check the speeling of your city and try again </h2> </body></html>")

    except:
        return HttpResponse("<html><body> <h1 align='center'> City not found </h1> <h2> Check the speeling of your city and try again </h2> </body></html>")

