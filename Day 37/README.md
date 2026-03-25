# Habit Tracking Project

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate%2B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A comprehensive habit tracking system that uses the Pixela API to log, visualize, and maintain daily activity records. This project was completed as part of **Day 37** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 37: Habit Tracking Project - API Post Requests & Headers** in the 100 Days of Code curriculum. It focuses on creating and managing data through API POST, PUT, and DELETE operations with authentication headers.

## 🎯 Project Overview

The Habit Tracking Project features:
- **User Management**: Create and manage Pixela API users
- **Graph Creation**: Customizable habit tracking graphs with color options
- **Pixel Logging**: Daily activity logging with quantity tracking
- **Data Management**: Update and delete existing entries
- **Authentication**: Token-based security for API operations
- **Visual Output**: Generates shareable graphs of habit progress

## 🚀 How It Works

1. **User Creation**: Creates a new user account on Pixela platform
2. **Graph Configuration**: Sets up a custom graph for tracking cycling distance
3. **Daily Logging**: Prompts for kilometers cycled and creates a pixel
4. **Data Persistence**: Stores all entries in Pixela's cloud platform
5. **Graph Generation**: Automatically creates visual representations of progress
6. **Update/Delete**: Provides options to modify or remove entries

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Requests Library** - API calls to Pixela service
- **Pixela API** - Habit tracking and data visualization platform
- **DateTime Module** - Date handling for pixel creation
- **Authentication Headers** - Token-based API security

## 📋 Learning Objectives

This project helped reinforce understanding of:
- REST API POST, PUT, DELETE operations
- Authentication headers for API security
- Data persistence through third-party services
- User account management via API
- Custom data structure creation
- Real-world application of HTTP methods

## 📡 Pixela API Endpoints

### User Creation
```python
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
```

### Graph Configuration
```python
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"  # Japanese hydrangea (blue-purple)
}
```

### Pixel Operations
```python
# Create pixel
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# Update pixel
new_pixel_data = {"quantity": "4.5"}

# Delete pixel
# DELETE request to pixel endpoint
```

## 🎨 Available Graph Colors

Pixela offers various color options:
- **shibafu**: Green (grass)
- **momiji**: Red (maple leaf)
- **sora**: Blue (sky)
- **ichou**: Yellow (ginkgo)
- **ajisai**: Blue-purple (hydrangea)
- **kuro**: Black

## 🔧 Technical Implementation

### Authentication Headers
```python
headers = {
    "X-USER-TOKEN": TOKEN  # Required for all requests after user creation
}
```

### Date Formatting
```python
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")  # Returns "20240325" format
```

### API Operations Flow
1. **POST /users**: Create user account
2. **POST /graphs**: Create tracking graph
3. **POST /pixels**: Add daily entries
4. **PUT /pixels**: Update existing entries
5. **DELETE /pixels**: Remove entries

## 💼 Practical Applications

- **Fitness Tracking**: Monitor exercise, running, cycling distance
- **Productivity**: Track work hours, tasks completed
- **Health Metrics**: Log water intake, sleep hours, meditation time
- **Learning Goals**: Track study hours, coding sessions
- **Financial Habits**: Monitor savings, spending patterns

## 🎯 How to Use

1. **Create Account** (Run Once):
   ```python
   # Uncomment and run user creation code
   response = requests.post(url=pixela_endpoint, json=user_params)
   ```

2. **Create Graph** (Run Once):
   ```python
   # Uncomment and run graph creation code
   response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
   ```

3. **Daily Logging** (Run Daily):
   ```python
   # Run main script to log today's activity
   python habit_tracker.py
   ```

4. **View Progress**:
   - Visit: `https://pixe.la/v1/users/[USERNAME]/graphs/[GRAPH_ID]`
   - See your habit graph visualized

## 📊 Sample Output

```
How many kilometers did you cycle today? 15.5
{"message":"Success.","isSuccess":true}
```

## 🔗 View Your Progress

After logging data, access your graph at:
```
https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html
```

## ⚠️ Important Notes

- **Token Security**: Keep your token private; it controls your account
- **One-Time Setup**: User and graph creation only needed once
- **Date Format**: Uses YYYYMMDD format (e.g., 20240325)
- **Quantity Type**: Must match graph type (float, int, etc.)
- **Rate Limits**: Pixela has reasonable API rate limits
- **Data Visualization**: Graphs auto-update with new entries

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*

## 🌸 About Pixela

Pixela is a free, open API service that allows users to track and visualize habits through simple REST API calls. The color names (ajisai, shibafu, etc.) are inspired by Japanese nature, adding a cultural touch to habit tracking.