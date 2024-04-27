from django.shortcuts import render
import requests
import datetime
from weather_app import settings


def index(request):
    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = "Nairobi"
    API_KEY = settings.DJANGO_OPEN_WEATHER_APP_API_KEY
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res["weather"][0]["description"]
    icon = res["weather"][0]["icon"]
    temp = res["main"]["temp"]
    day = datetime.date.today()
    context = {"description": description, "icon": icon, "temp": temp, "day": day, "city": city}
    return render(request, "core/index.html", context)
