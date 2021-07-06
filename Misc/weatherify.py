import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = "Hyderabad"

API_KEY = "e3e863c58988f03bcb608402cf36c939"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:                      
   data = response.json()

   main = data['main']

   temperature = int(main['temp']) - 273.15

   report = data['weather']

   print(f"{CITY:-^30}")
   print("Temperature: %.1f" % temperature)
   print(f"Weather Report: {report[0]['description']}")
else:

   print("Error in the HTTP request")
   print(URL)
