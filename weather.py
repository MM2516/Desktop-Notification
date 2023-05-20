from plyer import notification
import requests


def notify_weather():
    api_key = "7035b56d681a0a0e836a75d56b73722b"
    city_name = "Guwahati"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]
        temperature = data["main"]["temp"]
        description = weather["description"]
        with open('file.txt', 'r') as f:
            line_count = sum(1 for line in f)
        with open('file.txt', 'a') as f:
            f.write(f"{line_count + 1},Weather Update, {description}, Weather,Open Weather Map,Low\n")


        title = f"Weather in {city_name}:"
        message = f"{description}, {temperature}°C"
        notification.notify(title=title, message=message, app_icon=None, timeout=2, toast=False)

    else:
        print("Error fetching weather data.")


#notify_weather()
