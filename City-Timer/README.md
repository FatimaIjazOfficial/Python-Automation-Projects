# City Timer Program

The City Timer Program checks if the International Space Station (ISS) is overhead and if it's currently night time at a specified location. If both conditions are met, the program sends an email notification.

## Description

This program performs the following tasks:

1. Fetches the current location of the ISS.
2. Checks if the ISS is within ±5 degrees of the specified latitude and longitude.
3. Fetches the sunrise and sunset times for the specified location.
4. Checks if it is currently night time at the specified location.
5. Sends an email notification if both conditions are met (ISS overhead and it's night time).

## Usage Instructions

### 1. Setup Email Password

To use this program, you need to create an App Password for your email account. Follow these steps:

- Go to [Google Account](https://myaccount.google.com/).
- Select **Security** on the left and scroll down to **How you sign in to Google**.
- Find the section on **App Passwords** by searching for it.
- Create an App Password for your email (e.g., Python Mail) and click create.
- Copy the generated 16-character password. This is the only time you will see the password.

### 2. Configure Email Credentials

Update the `MY_EMAIL` and `MY_PASSWORD` variables in the `main.py` script with your email address and the generated app password.

### 3. Set Location Coordinates

Update the `MY_LAT` and `MY_LONG` variables with the latitude and longitude of your location.

### 4. Run the Program

Run the `main.py` script. The script will:

- Check the ISS location every 60 seconds.
- Determine if the ISS is overhead and if it's currently night time.
- Send an email notification if both conditions are met.

### Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)