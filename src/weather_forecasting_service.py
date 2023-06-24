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
        return
    
    def _build_query(self, city, type) -> str:
        api_key = self.get_api_key()
        url_encoded_city_name = city.replace(" ", "+")
        units = ""
        url = (
            f"{self._api_base_url}/{type}?q={url_encoded_city_name}"
            f"&units={units}&appid={api_key}"
        )
        return url

    def getCurrent(self, city):
        type = "weather"
        url = self._build_query(city, type)
        json = self._get_weather_data(url)
        return json

    def getToday(self, city):
        type = "forecast"
        url = self._build_query(city, type)
        json = self._get_weather_data(url)
        return json

    def getTomorrow(self, city):
        type = "forecast"
        url = self._build_query(city, type)
        json = self._get_weather_data(url)
        return json

    def getFiveDay(self, city):
        type = "forecast"
        url = self._build_query(city, type)
        json = self._get_weather_data(url)
        return json
    
    def get_api_key(self):
        config = ConfigParser()
        config.read("../secrets.ini")
        print(config["openweather"]["api_key"])
        return config["openweather"]["api_key"]
    
    
    def _get_weather_data(self, query_url):
        response = requests.get(query_url)
        return response.json()