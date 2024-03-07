# assignment03-cso.py
# By Joanne Feeney
# In this assignment I will Write a program that retrieves the dataset for the 
# "exchequer account (historical series)" from the CSO, and store it into a file called "cso.json"

# Importing packages
import requests
import json

# Setting URL
url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D"

# Adding request for URL as per lecture notes
response = requests.get(url)

# Assigning new variable called data
data = response.json()

# Open json file
with open("cso.json", "w") as fp:
    json.dump(data, fp)