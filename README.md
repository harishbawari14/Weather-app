**Text-to-Speech Weather Application**

****Overview****

This Python script provides real-time weather updates for a specified city using WeatherAPI and converts the output to speech using Microsoft Speech API (SAPI).

**Features:**

Retrieves the current temperature and humidity of a given city.

Converts the weather details into speech using the win32com.client library.

Allows the user to enter multiple city names for weather updates.

Exits the program when the user inputs 'q'.

**Prerequisites:**

Ensure you have the following installed before running the script:

Python 3.x

**Required Python packages:**
   
   Ensure you have the following installed before running the script:
    1.Python 3.x

   Required Python packages:
     1.pywin32

     2.requests

To install the required packages, run:

pip install pywin32 requests

API Key Setup

This script uses WeatherAPI. You need an API key to access the weather data.

Visit WeatherAPI and create a free account.

Obtain your API key and replace the placeholder in the script:

url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

**Usage:**

Run the script:

python script.py

Enter a city name when prompted.

The weather details will be displayed on the screen and spoken aloud.

Enter 'q' to exit the program.

**Example Output:**

Enter the name of the city
London
Current Temperature: 15°C
Humidity: 60%
Last Updated: 2025-03-01 12:00 PM
(Speech Output: "The current temperature in London is 15 degrees...")

**Troubleshooting:**

If the speech output does not work, ensure that SAPI is installed and configured correctly on your system.

If you receive an API error, check your API key and internet connection.
