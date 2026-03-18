# Rain Alert Project - Checks weather forecast and sends SMS alert if rain is expected
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# API Configuration
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")  # Store API key in environment variables
account_sid = "YOUR ACCOUNT SID"  # Replace with your Twilio account SID
auth_token = os.environ.get("AUTH_TOKEN")  # Store auth token in environment variables

# Weather parameters for Caruaru, Brazil
weather_params = {
    "lat": -8.28139,
    "lon": -35.9735,
    "appid": api_key,
    "cnt": 4,  # Number of forecast periods (4 = next 12 hours at 3-hour intervals)
}

# Fetch weather forecast data
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])  # Debug: print first weather condition code

# Check if rain is expected in any forecast period
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Weather codes below 700 indicate rain/snow
        will_rain = True

# Send SMS alert if rain is expected
if will_rain:
    # Configure proxy client for environments behind firewall
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # Initialize Twilio client with proxy
    client = Client(account_sid, auth_token, http_client=proxy_client)

    # Send SMS alert
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",  # Replace with your Twilio phone number
        to="YOUR TWILIO VERIFIED REAL NUMBER"  # Replace with your personal phone number
    )
    print(message.status)  # Print message status for confirmation
