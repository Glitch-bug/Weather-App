#! python3
# quickWeather.py - Prints the weather for a location from the command line.
# place copy in folder and git push as cli weather app (incomplete)
import json, requests, sys, csv

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py city country)')
    sys.exit()
location = ' '.join(sys.argv[1:])
locationFile = open('worldcities.csv', encoding="utf-8")
location_db = csv.reader(locationFile)

for row in location_db:
    if (sys.argv[1].title() == row[0] or sys.argv[1].title() == row[4]) & (sys.argv[2].title() == row[0] or sys.argv[2].title() == row[4]):
        lat = row[2]
        lon = row[3]
# map database obtained here https://simplemaps.com/data/world-cities
key = '60acc4dfaa5d2d1ac3c3b29e8c753a14'
# cnt = 3

# TODO: Get latitude and longitude for country and city name
# Download the JSON data from OpenWeather.org's API
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}' 
response = requests.get(url)
response.raise_for_status()


# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['weather']
print('Current weather in %s:' % (location.title()))
print(w[0]['main'], '-', w[0]['description'])
