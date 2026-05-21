# Rain Alert Program

The Rain Alert Program checks the weather forecast for the next few hours and alerts you if rain is expected.

## Description

This program performs the following tasks:

1. Fetches the weather forecast data for the specified location using the OpenWeatherMap API.
2. Checks the weather conditions for the next few hours.
3. Prints "Umbrella" if rain is expected.

## Usage Instructions

### 1. Setup OpenWeatherMap API Key

To use this program, you need an API key from OpenWeatherMap. Follow these steps:

- Go to [OpenWeatherMap](https://home.openweathermap.org/).
- Sign up or log in to your account.
- Go to the API Keys section and create a new API key.
- Copy the generated API key.

### 2. Configure API Key and Location Coordinates

Update the `api_key` variable in the script with your OpenWeatherMap API key.

Update the `lat` and `lon` values in the `weather_params` dictionary with the latitude and longitude of your location.

### 3. Run the Program

Run the script. The script will:

- Fetch the weather forecast data for the next few hours.
- Check if rain is expected.
- Print "Umbrella" if rain is expected.

### Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)