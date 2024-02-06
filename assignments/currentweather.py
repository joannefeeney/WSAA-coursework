# currentweather.py
# By Joanne Feeney
# In this assignment I will write a python program called currentweather.py that 
# will print out the current temperature on the console 
# (and print out the current wind direction (10m) as well.)

# Importing packages
import requests

# Setting URL
url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"

# Adding request for URL as per lecture notes
response = requests.get(url)

# Assigning new variable called data
data = response.json()

# Assigning variable bpi
v1 = data["v1"]

# Assigning variable temperature
temperature = v1["temperature_2m"]

#Print
print(temperature)