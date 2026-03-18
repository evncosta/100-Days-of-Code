# ISS Tracker

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate%2B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A continuous monitoring system that tracks the International Space Station's position and sends email notifications when it's visible overhead at night. This project was completed as part of **Day 33** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 33: API Endpoints & API Parameters** in the 100 Days of Code curriculum. It focuses on working with external APIs, handling JSON responses, and creating automated notification systems.

## 🎯 Project Overview

The ISS Tracker features:
- **Real-time ISS Tracking**: Fetches current ISS position from Open Notify API
- **Location-Based Visibility**: Checks if ISS is within 5 degrees of your coordinates
- **Night Detection**: Uses Sunrise-Sunset API to determine local night time
- **Automated Notifications**: Sends email alerts when ISS is visible
- **Continuous Monitoring**: Runs 24/7 with 60-second check intervals
- **Smart Conditions**: Only notifies when ISS is overhead AND it's dark enough to see

## 🚀 How It Works

1. **ISS Position Check**: Queries Open Notify API for current ISS coordinates
2. **Proximity Calculation**: Determines if ISS is within 5° of your location
3. **Night Detection**: Checks if it's currently nighttime using sunrise/sunset times
4. **Condition Evaluation**: Combines both conditions (overhead + night)
5. **Email Notification**: Sends alert when ISS is potentially visible
6. **Continuous Loop**: Repeats every minute for real-time monitoring

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Requests Library** - API calls and JSON data handling
- **SMTPLib** - Email notification system
- **DateTime Module** - Time parsing and comparison
- **External APIs**: 
  - Open Notify API (ISS position)
  - Sunrise-Sunset API (local night times)
- **Time Module** - Continuous monitoring loop control

## 📋 Learning Objectives

This project helped reinforce understanding of:
- RESTful API integration and endpoint usage
- API parameters and query string construction
- JSON response parsing and data extraction
- Conditional logic combining multiple data sources
- Continuous monitoring system design
- Automated notification workflows
- Time-based event triggering

## 📡 API Integration

### Open Notify API (ISS Position)
```python
response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

### Sunrise-Sunset API
```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
```

## 🔧 Technical Implementation

### Visibility Conditions
```python
def is_iss_overhead():
    # Check if ISS is within 5 degrees of your location
    return (MY_LAT-5 <= iss_latitude <= MY_LAT+5 and 
            MY_LONG-5 <= iss_longitude <= MY_LONG+5)

def is_night():
    # Night time is after sunset or before sunrise
    return time_now >= sunset or time_now <= sunrise
```

### Monitoring Loop
```python
while True:
    time.sleep(60)  # Check every minute
    if is_iss_overhead() and is_night():
        # Send email notification
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
```

## 🎯 Location Configuration

The tracker is currently configured for London:
```python
MY_LAT = 51.507351   # London latitude
MY_LONG = -0.127758  # London longitude
```

To use for your location:
1. Find your coordinates (Google Maps)
2. Update the `MY_LAT` and `MY_LONG` variables
3. Adjust proximity tolerance if needed (currently ±5°)

## 📊 Detection Logic

- **Overhead Condition**: ISS within 5° latitude/longitude of your position
- **Night Condition**: Current hour is after sunset OR before sunrise
- **Notification Trigger**: Both conditions must be TRUE simultaneously
- **Check Frequency**: Every 60 seconds for real-time accuracy

## 💼 Practical Applications

- **Amateur Astronomy**: ISS spotting opportunities
- **Educational Tool**: Teaching about satellite orbits
- **Photography**: Alert for night sky photography
- **Space Enthusiasts**: Real-time ISS tracking
- **STEM Education**: Demonstrating API integration

## 🎯 How to Use

1. **Configure Location**: Update latitude/longitude for your position
2. **Set Up Email**: Configure SMTP settings with your email credentials
3. **Run Program**: Execute script for continuous monitoring
4. **Wait for Alert**: Receive email when ISS is visible at night
5. **Enjoy the View**: Look up to spot the ISS passing overhead!

## ⚠️ Important Notes

- **API Limits**: Free APIs have rate limits; 60-second intervals are safe
- **Email Security**: Use app-specific passwords, not main account passwords
- **Continuous Operation**: Program runs indefinitely; use Ctrl+C to stop
- **Weather Dependent**: Clear skies needed for actual visibility

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
