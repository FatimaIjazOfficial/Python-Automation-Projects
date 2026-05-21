import requests
from datetime import datetime
import smtplib
import time

# Go to https://myaccount.google.com/
# Select Security on the left and scroll down to How you sign in to Google.
# Find the section on App Passwords by searching for it:
# There you can add an App password.
# Select give your app a name e.g., Python Mail and click create.
# COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.
MY_EMAIL = "your email"
MY_PASSWORD = "your app password"
MY_LAT = 31.520370
MY_LONG = 74.358749


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
