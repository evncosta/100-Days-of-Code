# Stock Trading News Alert Project

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate%2B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An automated stock monitoring system that tracks Tesla stock price changes and sends SMS alerts with relevant news when significant movements occur. This project was completed as part of **Day 36** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 36: Stock Trading News Alert Project** in the 100 Days of Code curriculum. It combines multiple API integrations, data analysis, and automated notifications to create a practical stock monitoring tool.

## 🎯 Project Overview

The Stock Trading News Alert features:
- **Stock Price Monitoring**: Fetches daily stock data from Alpha Vantage API
- **Price Change Analysis**: Calculates percentage changes between consecutive trading days
- **News Integration**: Retrieves relevant news articles from NewsAPI when significant price movements occur
- **SMS Notifications**: Sends formatted alerts via Twilio with stock changes and news headlines
- **Visual Indicators**: Uses 🔺/🔻 emojis to show price trend direction
- **Multi-Article Support**: Sends up to 3 news articles per significant price movement

## 🚀 How It Works

1. **Stock Data Fetch**: Retrieves daily time series data for Tesla (TSLA) from Alpha Vantage
2. **Price Comparison**: Compares closing prices from the last two trading days
3. **Change Calculation**: Computes percentage difference and determines trend direction
4. **Threshold Check**: Triggers alerts when price change exceeds 1%
5. **News Retrieval**: Fetches latest news articles about Tesla from NewsAPI
6. **Message Formatting**: Creates formatted SMS with price change and top 3 headlines
7. **Alert Delivery**: Sends notifications via Twilio SMS service

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Requests Library** - API calls to multiple services
- **Alpha Vantage API** - Stock market data provider
- **NewsAPI** - News article retrieval service
- **Twilio API** - SMS notification delivery
- **Data Analysis** - Percentage change calculations and trend analysis

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Multiple API integration in a single application
- Financial data analysis and interpretation
- Conditional logic for alert thresholds
- Data formatting for SMS delivery
- Error handling in API responses
- Real-world automation scenarios
- Multi-source data correlation

## 📡 API Configuration

### Alpha Vantage (Stock Data)
```python
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,  # "TSLA" for Tesla
    "apikey": STOCK_API_KEY,
}
```

### NewsAPI (Article Retrieval)
```python
news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,  # "Tesla Inc" for Tesla news
}
```

## 🔧 Technical Implementation

### Price Change Analysis
```python
difference = float(yesterday_price) - float(day_before_price)
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / float(yesterday_price)) * 100)
```

### Alert Threshold Logic
```python
if abs(diff_percent) > 1:  # Trigger when change exceeds 1%
    # Fetch and send news alerts
```

### SMS Message Formatting
```python
formatted_articles = [
    f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
    for article in three_articles
]
```

## 📊 Sample Alert Message

```
TSLA: 🔺2.5%
Headline: Tesla Announces New Battery Technology
Brief: The company's stock surges following breakthrough in battery efficiency research.
```

## 🔒 Configuration Requirements

### API Keys Needed:
- **Alpha Vantage API Key**: Free tier available at alphavantage.co
- **NewsAPI Key**: Free tier at newsapi.org
- **Twilio Credentials**: Account SID and Auth Token from twilio.com

### Phone Numbers:
- Twilio virtual number (purchased through Twilio)
- Verified personal number (must be verified in Twilio trial account)

## 💼 Practical Applications

- **Personal Investment Tracking**: Monitor stocks in your portfolio
- **Day Trading Support**: Get real-time alerts for volatile stocks
- **Market Research**: Correlate news with price movements
- **Automated Trading Signals**: Foundation for trading bots
- **Portfolio Management**: Track multiple stocks simultaneously

## 🎯 How to Use

1. **Get API Keys**:
   - Register at Alpha Vantage for stock API key
   - Register at NewsAPI for news API key
   - Set up Twilio account for SMS service

2. **Configure Credentials**:
   ```python
   STOCK_API_KEY = "your_alphavantage_key"
   NEWS_API_KEY = "your_newsapi_key"
   TWILIO_SID = "your_twilio_sid"
   TWILIO_AUTH_TOKEN = "your_twilio_token"
   ```

3. **Set Phone Numbers**:
   - Replace `VIRTUAL_TWILIO_NUMBER` with your Twilio number
   - Update `VERIFIED_NUMBER` with your personal phone

4. **Run the Script**:
   ```bash
   python stock_news_alert.py
   ```

5. **Schedule Regular Checks**:
   - Use cron jobs or Task Scheduler
   - Run after market close for daily alerts

## ⚙️ Customization Options

- **Change Stock**: Modify `STOCK_NAME` and `COMPANY_NAME`
- **Adjust Threshold**: Change the 1% trigger value
- **Article Count**: Modify the number of articles sent
- **Alert Frequency**: Adjust scheduling for different intervals
- **Multiple Stocks**: Extend to monitor multiple symbols

## ⚠️ Important Notes

- **API Limits**: Free tiers have rate limits (Alpha Vantage: 5 calls/minute, NewsAPI: 100 calls/day)
- **Market Days**: Only trading days have data; weekends show last trading day
- **SMS Costs**: Twilio charges per message; monitor usage
- **Data Accuracy**: API data may have slight delays from real-time
- **Time Zones**: Market closing times vary by exchange

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
