from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()
WEATHER_KEY = os.getenv("WEATHER_KEY")
date_now = datetime.now()
def get_weather():
     res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Tel+Aviv,IL&appid={WEATHER_KEY}&units=metric")
     data = res.json()
     print(date_now.strftime("%Y-%m-%d %H:%M:%S"))
     print("City: Tel Aviv")
     print(f"Condition: {data['weather'][0]['description']}")
     print(f"Temperature: {data["main"]["temp"]}")
