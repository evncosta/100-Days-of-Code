# Automated Birthday Wisher Project

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An automated system that sends personalized birthday emails using scheduled scripts and email templates. This project was completed as part of **Day 32** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 32: Send Email (smtplib) & Manage Dates (datetime)** in the 100 Days of Code curriculum. It focuses on automation, email protocols, and date-based event triggering.

## 🎯 Project Overview

The Automated Birthday Wisher features:
- **Date Detection**: Automatically identifies birthdays matching current date
- **Email Automation**: Sends personalized birthday emails via SMTP
- **Template System**: Random selection from multiple birthday message templates
- **Personalization**: Customizes emails with recipient names
- **SMTP Integration**: Secure email sending with TLS encryption
- **CSV Data Management**: Stores birthday information in structured format

## 🚀 How It Works

1. **Date Checking**: Compares current date with birthday database
2. **Data Lookup**: Finds recipients with birthdays today
3. **Template Selection**: Randomly chooses a birthday message template
4. **Personalization**: Inserts recipient name into the template
5. **Email Composition**: Creates properly formatted email message
6. **Secure Delivery**: Sends email via SMTP with TLS encryption
7. **Confirmation**: Prints success message to console

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **SMTPLib** - Email sending protocol implementation
- **DateTime** - Date and time operations for birthday checking
- **Pandas** - CSV data processing and management
- **Random Module** - Template selection randomization
- **Email Library** - MIME message formatting and composition

## 📋 Learning Objectives

This project helped reinforce understanding of:
- SMTP protocol and email automation
- Date comparison and time-based event triggering
- File I/O operations with template systems
- Data processing with pandas DataFrames
- Secure email transmission with TLS encryption
- Automation script design and scheduling
- Personalized content generation

## 📁 Project Structure

```
Day 32 - Automated Birthday Wisher/
│
├── main.py                     # Main automation script
├── birthdays.csv               # Birthday database (name, email, month, day)
├── letter_templates/
│   ├── letter_1.txt           # Birthday template 1
│   ├── letter_2.txt           # Birthday template 2
│   └── letter_3.txt           # Birthday template 3
└── README.md                   # Project documentation
```

## 📊 Data Structure

### birthdays.csv Format:
```csv
name,email,month,day
John Doe,john@email.com,5,15
Jane Smith,jane@email.com,8,22
```

### Letter Template Format:
```txt
Dear [NAME],

Happy Birthday! Hope you have a wonderful day!

Best wishes,
Your Friend
```

## 🔧 Technical Implementation

### Date Comparison Logic
```python
now = dt.datetime.now()
month_day = (now.month, now.day)  # Create tuple for efficient lookup
birthdays_dict = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}
```

### Email Composition
```python
msg = MIMEMultipart()
msg['From'] = MY_EMAIL
msg['To'] = birthday_person["email"]
msg['Subject'] = "Happy Birthday!"
msg.attach(MIMEText(letter_data, 'plain'))
```

### Secure Email Sending
```python
with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()  # Enable TLS encryption
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(MY_EMAIL, birthday_person["email"], msg.as_string())
```

## 🔒 Security Features

- **TLS Encryption**: Secure email transmission
- **App Passwords**: Use of application-specific passwords (not shown)
- **Data Privacy**: Birthday information stored locally
- **Controlled Access**: Email credentials in secure configuration

## 💼 Practical Applications

- **Personal Use**: Automated birthday reminders for friends and family
- **Business Applications**: Customer birthday marketing campaigns
- **Community Management**: Member engagement for clubs and organizations
- **HR Systems**: Employee recognition programs
- **Educational Tools**: School announcements and reminders

## 🎯 How to Use

1. **Setup Database**: Add birthdays to `birthdays.csv` with name, email, month, day
2. **Create Templates**: Design birthday messages in `letter_templates/` folder with `[NAME]` placeholder
3. **Configure Email**: Update `MY_EMAIL` and `MY_PASSWORD` with your credentials
4. **Schedule Execution**: Set up cron job or task scheduler to run daily
5. **Monitor Results**: Check console output for sent emails

## ⚙️ Automation Setup

### Windows Task Scheduler:
- Create basic task to run daily
- Set program to Python executable
- Add script path as argument

## 🔄 Extension Possibilities

- Add attachment support for birthday cards
- Include SMS notifications via Twilio
- Create web interface for managing birthdays
- Add reminder notifications before birthdays
- Implement holiday greeting system
- Add analytics for sent emails

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
