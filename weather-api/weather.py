import requests

def get_location(city, country):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&language=en&format=json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "results" not in data:
            return None

        for item in data["results"]:
            if item.get("country", "").lower() == country.lower():
                return {
                    "name": item["name"],
                    "country": item["country"],
                    "latitude": item["latitude"],
                    "longitude": item["longitude"]
                }

        return None

    except requests.RequestException:
        print("❌ Failed to fetch location data.")
        return None

def get_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        print("❌ Failed to fetch weather data.")
        return None

def display_weather(location, weather):
    current = weather["current"]

    print("\n🌤 Weather Report")
    print("-" * 30)
    print(f"📍 Location    : {location['name']}, {location['country']}")
    print(f"🌡 Temperature : {current['temperature_2m']} °C")
    print(f"💨 Wind Speed  : {current['wind_speed_10m']} km/h")
    print("-" * 30)


def main():
    print("=== Weather App ===")

    country = input("Enter country: ").strip()
    city = input("Enter city: ").strip()

    location = get_location(city, country)

    if not location:
        print(f"❌ No city named '{city}' found in {country}")
        return

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    if not weather:
        return

    display_weather(location, weather)

if __name__ == "__main__":
    main()