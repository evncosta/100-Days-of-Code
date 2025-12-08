# Automated Birthday Wisher Project - Automatically sends birthday emails
import datetime as dt
import pandas
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_EMAIL = "esthervn@yahoo.com"
MY_PASSWORD = "password"  # Note: Actual App Password changed due to privacy and security reasons

now = dt.datetime.now()
month_day = (now.month, now.day)  # Create tuple for date comparison

# Load birthday data from CSV
data = pandas.read_csv("birthdays.csv")
# Create dictionary with (month, day) as keys for easy lookup
birthdays_dict = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}

# Check if today matches any birthday
if month_day in birthdays_dict:
    birthday_person = birthdays_dict[month_day]

    # Select random birthday letter template
    random_num = random.randint(1, 3)
    random_letter = f"letter_{random_num}.txt"
    template_path = f"./letter_templates/{random_letter}"

    # Read and personalize template
    with open(template_path, "r") as file:
        letter_data = file.read()

    letter_data = letter_data.replace("[NAME]", birthday_person["name"])

    # Set up email message
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = birthday_person["email"]
    msg['Subject'] = "Happy Birthday!"

    msg.attach(MIMEText(letter_data, 'plain'))

    # Send email via SMTP
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=msg.as_string()
        )
    print(f"Birthday email sent to {birthday_person['name']}!")
else:
    print("No birthdays today.")
