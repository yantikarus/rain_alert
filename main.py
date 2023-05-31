import requests
from twilio.rest import Client

API=

params = {
    "lat": -21.311990,
    "lon": -46.701960,
    "appid": API,
    "exclude":"current,minutely,daily"
}

account_sid =
auth_token =


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"]
weather_slice = hourly_data[:12]
print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="its gonna rain today bring an ☂️",
        from_='',
        to=''
    )