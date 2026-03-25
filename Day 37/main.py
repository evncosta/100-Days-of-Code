# Habit Tracking Project - Tracks daily cycling activity using Pixela API
import requests
from datetime import datetime

# User configuration (replace with your actual values)
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

# Pixela API endpoints
pixela_endpoint = "https://pixe.la/v1/users"

# User creation parameters (uncomment to create new user)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST - Create new Pixela user (run once)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Graph creation endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"  # Japanese hydrangea color
}

# Authentication header
headers = {
    "X-USER-TOKEN": TOKEN
}

# POST - Create new graph (run once)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixel creation endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date
today = datetime.now()

# Create pixel for today's cycling activity
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# POST - Add today's cycling data
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Update existing pixel endpoint
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# PUT - Update existing pixel (uncomment to use)
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete pixel endpoint
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# DELETE - Remove pixel (uncomment to use)
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)