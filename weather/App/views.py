from django.shortcuts import render
import requests
import datetime



def application(request):
    try:
        if request.method=='POST':
            city=request.POST.get('city')
        if city:
            pass
        try:
            api = '1225f09c1a0407c6edd97e9f8f47baad'
            get_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api}").json()
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
            return render(request,'sample1.html',{'x':data})
        except:
            return render(request,'sample2.html')
    except:
        return render(request,'sample3.html')
    

    