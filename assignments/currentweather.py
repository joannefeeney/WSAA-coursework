# currentweather.py
# By Joanne Feeney
# In this assignment I will write a python program called currentweather.py that 
# will print out the current temperature on the console 
# (and print out the current wind direction (10m) as well.)

# Importing packages
from xml.dom.minidom import parseString
import requests
import csv

# Setting URL & defining function
def current_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
# Adding request for URL
# https://www.w3schools.com/python/python_try_except.asp
    try:
        response = requests.get(url)
        # Assigning new variable called data
        data = response.json()
        
        if "temperature_2m" in data["current"] and 'wind_speed_10m' in data["current"]:
        # "current" is defined in the api
            temperature = data["current"]["temperature_2m"]
            wind_speed = data["current"]["wind_speed_10m"]
            print(f"Current Temperature: {temperature}°C")
            print(f"Current Wind Speed (10m): {wind_speed} m/s")
    # Adding except (will not work if I don't)
    except:
        print(f"Error")

# Check if script being run as main 
if __name__ == "__main__":
    current_weather()