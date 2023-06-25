import requests                         # for making HTTP Requests
from configparser import ConfigParser   # for parsing '../secrets.ini' file

# -------------------------------
# this class is used to fetch weather forecast data from the OpenWeatherMap API
# all the API interactions are handled by this class only
class WeatherForecastingService:
    """This class is used to fetch weather forecast data from the OpenWeatherMap API
    """

    # ---------------------------

    _api_base_url = "https://api.openweathermap.org/data/2.5/"
    
    # enum class for different query types
    class QueryType:
        """Enum class for different query types
        """
        CURRENT = "weather"
        TODAY = "forecast"
        TOMORROW = "forecast"
        FIVE_DAY = "forecast"

    # ---------------------------
    # Constructor - sets the default city to Bangalore
    def __init__(self):
        """Constructor - sets the default city to Bangalore
        """
        self._city = "Bangalore"

    # ---------------------------
    # Setter method for _city
    def set_city(self, city) -> None:
        """Sets the city to be used for the weather forecasting tool
        """
        self._city = city
        return

    # ---------------------------
    # Getter method for _city
    def get_city(self) -> str:
        """Returns the currently set city
        """
        return self._city

    # ---------------------------
    # Builds the query URL for the API
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
    # Fetches the API key from the secrets.ini file
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
    # Fetches the weather data from the API
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
    # returns the current weather forecast dict for the set city
    def getCurrent(self):
        """Returns the current weather forecast dict for the set city
        """
        type = self.QueryType.CURRENT
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json
        
    # ---------------------------

    def getToday(self):
        """Returns the today's weather forecast dict for the set city
        """
        type = self.QueryType.TODAY
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------

    def getTomorrow(self):
        """Returns the tomorrow's weather forecast dict for the set city
        """
        type = self.QueryType.TOMORROW
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------

    def getFiveDay(self):
        """Returns the 5 day weather forecast dict for the set city
        """
        type = self.QueryType.FIVE_DAY
        url = self._build_query(type)
        json = self._get_weather_data(url)
        return json

    # ---------------------------
    
# --------- End of Class --------
# -------------------------------