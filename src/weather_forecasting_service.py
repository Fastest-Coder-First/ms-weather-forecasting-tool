import requests
from configparser import ConfigParser

class WeatherForecastingService:

    _api_base_url = "https://api.openweathermap.org/data/2.5/"
    
    class QueryType:
        CURRENT = "weather"
        TODAY = "forecast"
        TOMORROW = "forecast"
        FIVE_DAY = "forecast"

    def __init__(self):
        self._city = "Bangalore"

    def set_city(self, city) -> None:
        """Sets the city to be used for the weather forecasting tool
        """
        self._city = city
        return
    
    def get_city(self) -> str:
        """Returns the currently set city
        """
        return self._city
    
    def _build_query(self, type) -> str:
        api_key = self._get_api_key()
        url_encoded_city_name = self._city.replace(" ", "+")
        units = ""
        url = (
            f"{self._api_base_url}/{type}?q={url_encoded_city_name}"
            f"&units={units}&appid={api_key}"
        )
        return url
    
    def _get_api_key(self):
        try:
            config = ConfigParser()
            config.read("./secrets.ini")
            return config["openweather"]["api_key"]
        except (FileNotFoundError, KeyError) as e:
            # Handle file not found or key not found errors
            print("Error retrieving API key:", str(e))
            return None
        except Exception as e:
            # Handle other exceptions
            print("An error occurred:", str(e))
            return None
    
    def _get_weather_data(self, query_url):
        try:
            response = requests.get(query_url)
            response.raise_for_status()
            json_data = response.json()
            
            return json_data
        except requests.exceptions.RequestException as e:
            print("An error occurred while fetching weather data from API:", e)
            return None
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
            return None
        except ValueError as e:
            print("An error occurred while parsing the JSON response:", e)
            return None

    def getCurrent(self):
        type = "weather"
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    def getToday(self):
        type = "forecast"
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    def getTomorrow(self):
        type = "forecast"
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    def getFiveDay(self):
        type = "forecast"
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json