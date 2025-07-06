import requests

own_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api = "enter your api key"

weather_parameters = {
    "lat": 28.6667,
    "lon": 77.2167,
    "appid": api,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(own_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain=False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

if will_rain:
    print("umbrella")
