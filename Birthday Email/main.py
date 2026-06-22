import random
import smtplib
from datetime import datetime
import pandas

# Go to https://myaccount.google.com/
# Select Security on the left and scroll down to How you sign in to Google.
# Find the section on App Passwords by searching for it:
# There you can add an App password.
# Select give your app a name e.g., Python Mail and click create.
# COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.

email = "enter email"
password = "enter app password"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=email, password=password)
        connections.sendmail(from_addr=email,
                             to_addrs=birthday_person["email"],
                             msg=f"Subject:Happy Birthday!\n\n{contents}")
