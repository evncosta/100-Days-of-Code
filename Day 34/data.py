import requests

parameters = {
    "amount": 10,
    "type": "boolean",  # Get true/false questions only
}

response = requests.get("https://opentdb.com/api.php", params=parameters) # Fetches quiz questions from Open Trivia Database API
response.raise_for_status()
data = response.json()
question_data = data["results"]  # Store questions for use in main.py