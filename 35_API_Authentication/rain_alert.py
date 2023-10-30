import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# URL that works:
'''
https://api.openweathermap.org/data/2.8/onecall?lat=42.6187211&lon=25.394461&appid=08feb2bd3e5c8e3da73b377af57f62af
'''
# MY_LAT = 42.6187211  # latitude
# MY_LONG = 25.394461  # longitude
_LAT = 45.068371
_LONG = 7.683070

api_key = os.environ.get("OMW_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall?lat=42.6187211&lon=25.394461&appid=08feb2bd3e5c8e3da73b377af57f62af"

account_sid = "ACee3ed3f3c6abfba811307def53f778ce"
auth_token = os.environ.get("AUTH_TOKEN")

# phone_numbers = ["+359898784412", "+359886708160"]

weather_params = {
    "lat": _LAT,
    "lon": _LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

will_rain = False
if response.status_code == 200:
    weather_data = response.json()
    hourly_forcast = weather_data["hourly"][:12]
    for hour in hourly_forcast:
        weather_condition = hour["weather"][0]["id"]
        main_cond = hour["weather"][0]["main"]
        if weather_condition < 700:
            will_rain = True
            break
            # print(f"Bring umbrella because the weather is {main_cond}")

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
            body="It's going to rain in Kazanlak. Remember to bring an ☔",
            from_="+18302665362",
            to="+359898784412",
        )
    print(message.status)