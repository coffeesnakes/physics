import requests
import sys

# Get the location as a command line argument
location = sys.argv[1]

# Check the weather using wttr.in
response = requests.get(f'http://wttr.in/{location}?format=%C+%t')


# Print the weather information
print(response.text)


# PS C:\Users\0leg\.cursor-tutor\physics\psuedo> python3 getWeather.py florida
# Clear +19°C
# PS C:\Users\0leg\.cursor-tutor\physics\psuedo> python3 getWeather.py antarctica
# Unknown location; please try ~-82.1081821,34.37824
# PS C:\Users\0leg\.cursor-tutor\physics\psuedo> python3 getWeather.py antartica
# Unknown location; please try ~-82.1081821,34.37824
# PS C:\Users\0leg\.cursor-tutor\physics\psuedo> python3 getWeather.py norway
# Partly cloudy +10°C
# PS C:\Users\0leg\.cursor-tutor\physics\psuedo> python3 getWeather.py russia
# Partly cloudy -5°C
# PS C:\Users\0leg\.cursor-tutor\physics\psuedo> python3 getWeather.py ukraine
# Light rain +9°C