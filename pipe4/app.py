import requests

def weather_forecast(city):
    """
    Fetches the weather data for a specified city from OpenWeatherMap API.
    Prints the weather information, including temperature and pressure.
    """
    api_key = '2ad207f1576cc623c5396f3df877c5d7'
    try:
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={'q': city, 'units': 'metric', 'APPID': api_key},
            timeout=10  # Ограничиваем время ожидания
        )

        if response.status_code == 200:
            data = response.json()
            print('City:', data['name'])
            for i in data['main']:
                print('  ', i, '-->', data['main'][i])
        else:
            print('Status Code:', response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as error_name:
        print(f"Unexpected error: {error_name}")


def main():
    """
    The main entry point of the program. Fetches the weather forecast for a default city.
    """
    city_name = "GYUMRI"
    weather_forecast(city_name)

if __name__ == '__main__':
    main()
