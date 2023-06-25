import requests                         # for making HTTP Requests
from configparser import ConfigParser   # for parsing '../secrets.ini' file

class WeatherForecastingService:

    # ---------------------------

    _api_base_url = "https://api.openweathermap.org/data/2.5/"
    
    class QueryType:
        CURRENT = "weather"
        TODAY = "forecast"
        TOMORROW = "forecast"
        FIVE_DAY = "forecast"

    # ---------------------------

    def __init__(self):
        self._city = "Bangalore"

    # ---------------------------

    def set_city(self, city) -> None:
        """Sets the city to be used for the weather forecasting tool
        """
        self._city = city
        return

    # ---------------------------
    
    def get_city(self) -> str:
        """Returns the currently set city
        """
        return self._city

    # ---------------------------
    
    def _build_query(self, type) -> str:
        api_key = self._get_api_key()
        url_encoded_city_name = self._city.replace(" ", "+")
        units = ""
        url = (
            f"{self._api_base_url}/{type}?q={url_encoded_city_name}"
            f"&units={units}&appid={api_key}"
        )
        return url

    # ---------------------------
    
    def _get_api_key(self):
        try:
            config = ConfigParser()
            config.read("./secrets.ini")
            return config["openweather"]["api_key"]

        # Handle file not found or key not found errors
        except (FileNotFoundError, KeyError) as e:
            raise e
        
        # Handle other exceptions
        except Exception as e:
            raise e

    # ---------------------------
    
    def _get_weather_data(self, query_url):
        try:
            response = requests.get(query_url)
            response.raise_for_status()
            json_data = response.json()
            
            return json_data

        # Handle request exceptions
        except requests.exceptions.RequestException as e:
            print("An error occurred while fetching weather data from API: ", e)
            raise e
        
        # Handle HTTP Errors
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
            raise e

        # Handle ValueErrors while parsing JSON object
        except ValueError as e:
            print("An error occurred while parsing the JSON response: ", e)
            raise e

    # ---------------------------
        
    def getCurrent(self):
        type = self.QueryType.CURRENT
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------

    def getToday(self):
        type = self.QueryType.TODAY
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------

    def getTomorrow(self):
        type = self.QueryType.TOMORROW
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------

    def getFiveDay(self):
        type = self.QueryType.FIVE_DAY
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------
    
# --------- End of Class --------
# -------------------------------