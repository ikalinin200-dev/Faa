import json
from urllib.request import urlopen
from urllib.error import URLError


def get_weather(city_name):
    try:
        # Кодируем название города для URL
        from urllib.parse import quote
        city_encoded = quote(city_name.encode('utf-8'))

        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_encoded}&count=1&language=ru&format=json"

        with urlopen(geocode_url) as response:
            data = json.loads(response.read().decode('utf-8'))

        if not data.get('results'):
            print(f"Город '{city_name}' не найден.")
            return

        location = data['results'][0]
        lat = location['latitude']
        lon = location['longitude']
        full_name = location['name']
        country = location.get('country', '')

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"

        with urlopen(weather_url) as response:
            weather_data = json.loads(response.read().decode('utf-8'))

        current = weather_data.get('current_weather')

        if current:
            temp = current['temperature']
            wind_speed = current['windspeed']
            weather_code = current.get('weathercode')

            # Расшифровка кода погоды
            weather_codes = {
                0: "Ясно", 1: "В основном ясно", 2: "Переменная облачность",
                3: "Пасмурно", 45: "Туман", 51: "Морось", 61: "Дождь",
                71: "Снег", 80: "Ливень"
            }
            weather_desc = weather_codes.get(weather_code, "Данные не получены")

            print("\n" + "=" * 40)
            print(f"Погода в городе: {full_name}, {country}")
            print("=" * 40)
            print(f"Описание: {weather_desc}")
            print(f"Температура: {temp}°C")
            print(f"Скорость ветра: {wind_speed} км/ч")
            print("=" * 40)

    except URLError as e:
        print(f"Ошибка подключения: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    city = input("Введите название населённого пункта: ")
    get_weather(city)