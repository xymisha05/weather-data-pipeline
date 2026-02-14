import requests
import json
from datetime import datetime

# Newark coordinates
LAT = 40.7357
LON = -74.1724

URL = URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=temperature_2m"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()
    return data

def save_raw_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/weather_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Saved raw data to {filename}")

def main():
    data = fetch_weather()
    save_raw_data(data)

if __name__ == "__main__":
    main()