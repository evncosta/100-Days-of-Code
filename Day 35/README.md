# Rain Alert Project

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate%2B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An automated weather monitoring system that checks rain forecasts and sends SMS alerts when precipitation is expected. This project was completed as part of **Day 35** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 35: Keys, Authentication & Environment Variables** in the 100 Days of Code curriculum. It focuses on API authentication, secure credential management, and SMS automation.

## 🎯 Project Overview

The Rain Alert Project features:
- **Weather Forecast API**: Fetches 12-hour weather predictions from OpenWeatherMap
- **Rain Detection**: Analyzes weather condition codes to identify precipitation
- **SMS Notifications**: Sends timely alerts via Twilio when rain is expected
- **Secure Credentials**: Uses environment variables for API keys and tokens
- **Proxy Support**: Handles network configurations behind firewalls
- **Automated Monitoring**: Can be scheduled to run daily for regular alerts

## 🚀 How It Works

1. **API Request**: Queries OpenWeatherMap for 5-day/3-hour forecast data
2. **Data Analysis**: Checks weather condition codes for next 12 hours
3. **Rain Detection**: Identifies codes below 700 (indicating rain/snow)
4. **Alert Trigger**: Sends SMS via Twilio if rain is detected
5. **Secure Communication**: Uses environment variables for all sensitive credentials
6. **Status Confirmation**: Prints message status for verification

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Requests Library** - API calls to OpenWeatherMap
- **Twilio API** - SMS notification service
- **Environment Variables** - Secure credential management (os.environ)
- **Weather API** - OpenWeatherMap 5-day forecast endpoint
- **Proxy Handling** - Network configuration for secure environments

## 📋 Learning Objectives

This project helped reinforce understanding of:
- API authentication with API keys
- Environment variables for secure credential storage
- Weather data interpretation (condition codes)
- SMS automation with Twilio
- Proxy configuration for network-restricted environments
- Data filtering and conditional logic
- Scheduled task automation concepts

## 📡 API Integration

### OpenWeatherMap Forecast API
```python
weather_params = {
    "lat": -8.28139,      # Caruaru, Brazil latitude
    "lon": -35.9735,       # Caruaru, Brazil longitude
    "appid": api_key,      # Securely stored API key
    "cnt": 4,              # 4 periods = 12 hours (3-hour intervals)
}
```

### Weather Condition Codes
- **Codes < 700**: Rain, snow, or extreme weather
- **Codes 700-799**: Atmospheric conditions (mist, fog, etc.)
- **Codes 800-899**: Clouds and clear sky
- **Rain Detection**: Checks for any code below 700

## 🔧 Technical Implementation

### Rain Detection Logic
```python
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Rain/snow conditions
        will_rain = True
```

### Secure Credential Management
```python
api_key = os.environ.get("OWM_API_KEY")  # Never hardcode API keys
auth_token = os.environ.get("AUTH_TOKEN")
```

### SMS Alert with Proxy Support
```python
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid, auth_token, http_client=proxy_client)
```

## 📍 Location Configuration

Currently configured for **Caruaru, Brazil**:
```python
"lat": -8.28139    # Caruaru latitude
"lon": -35.9735    # Caruaru longitude
```

To modify for your location:
1. Find your coordinates (Google Maps)
2. Update latitude and longitude values
3. Adjust forecast period count if desired

## 🔒 Security Features

- **Environment Variables**: All API keys and tokens stored securely
- **No Hardcoded Credentials**: Prevents accidental exposure in code
- **Proxy Support**: Secure communication behind firewalls
- **API Key Protection**: Keys never visible in source code
- **Twilio Authentication**: Account SID and auth token protected

## 💼 Practical Applications

- **Daily Commute Planning**: Know if you need an umbrella
- **Outdoor Event Management**: Plan activities around weather
- **Gardening Automation**: Alert for watering needs
- **Travel Planning**: Weather updates for destinations
- **Agricultural Monitoring**: Crop protection from rain

## 🎯 How to Use

1. **Set Up Environment Variables**:
   ```bash
   export OWM_API_KEY="your_openweather_api_key"
   export AUTH_TOKEN="your_twilio_auth_token"
   export https_proxy="your_proxy_url"  # If behind proxy
   ```

2. **Configure Twilio**:
   - Replace `account_sid` with your Twilio SID
   - Update `from_` with your Twilio phone number
   - Set `to` with your verified personal number

3. **Run the Script**:
   ```bash
   python rain_alert.py
   ```

4. **Schedule Automatically**:
   - Use cron (Linux/Mac) or Task Scheduler (Windows)
   - Run daily at desired time (e.g., 7 AM)

## 📊 Sample Output

```
# Console output when rain detected
MessageStatus  # Prints status (e.g., "queued", "sent", "delivered")
```

## ⚠️ Important Notes

- **API Limits**: OpenWeatherMap free tier has limited daily calls
- **Twilio Costs**: SMS messages incur charges (check pricing)
- **Phone Verification**: Twilio requires number verification for trial accounts
- **Proxy Configuration**: Required for some corporate/educational networks
- **Time Zones**: API returns UTC; adjust for local time if needed

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*

## ☔️ Weather Fact

Weather condition codes below 700 include:
- **500-599**: Rain (light, moderate, heavy)
- **600-699**: Snow
- **200-299**: Thunderstorm
- **300-399**: Drizzle
