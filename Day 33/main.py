# ISS Tracker - Monitors ISS position and sends email when visible overhead at night
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "esthervn@yahoo.com"
MY_PASSWORD = "password"  # Note: App Password changed for security
MY_LAT = -8.28139  # Caruaru latitude
MY_LONG = -35.9735  # Caruaru longitude

def is_iss_overhead():
    # Check if ISS is within 5 degrees of your location
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False

def is_night():
    # Check if it's currently nighttime at your location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Extract hour from sunrise/sunset times
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Night time is after sunset or before sunrise
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

# Continuous monitoring loop
while True:
    time.sleep(60)  # Check every minute
    if is_iss_overhead() and is_night():
        # Send email notification when ISS is visible
        connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
