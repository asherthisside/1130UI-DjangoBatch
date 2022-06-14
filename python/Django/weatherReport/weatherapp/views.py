from django.shortcuts import render
import urllib
import json


def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST' :
        city = request.POST['city']

        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city +"&units=metric&appid=8d8c68db2a9d6caf4be9058ebb5cd831").read()

        data = json.loads(source)

        print(data)
        context = {
            'city_name' : city,
            'country_code' : str(data["sys"]["country"]),
            'coords' : "Lat: " + str(data["coord"]["lat"]) + " | Lon: " + str(data["coord"]["lon"]),
            'main' : str(data["weather"][0]["main"]),
            'description' : str(data["weather"][0]["description"]),
            'temprature' : str(data["main"]["temp"]),
            'pressure' : str(data["main"]["pressure"]),
            'humidity' : str(data["main"]["humidity"]),
        }
        return render(request, 'result.html', context)
    else:
        return render(request, 'result.html')  