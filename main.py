import os                       # for command line operations ('clear', 'cls', etc)
from datetime import datetime   # for fetching and parsing date and time
from sys import platform        # for fetching OS information

from src import WeatherForecastingService

# -------------------------------
# this class handles all interactions of the tool with the user
class WeatherForecastingTool:
    """This class handles all interactions of the tool with the user
    """

    # ---------------------------
    # constructor - sets the default city to Bangalore
    #               and creates a WeatherForecastingService object
    def __init__(self) -> None:
        """Constructor - sets the default city to Bangalore
                        and creates a WeatherForecastingService object
        Args:
            None

        Returns:
            None

        """
        self._city = "Bangalore"
        self._weather_forecasting_service = WeatherForecastingService()

    # ---------------------------
    # setter method for _city
    def set_city(self, city) -> None:
        """Sets the city to be used for the weather forecasting tool

        Args:
            city (str): the city to be used for the weather forecasting tool

        Returns:
            None

        """
        self._city = city
        self._weather_forecasting_service.set_city(city)
        return

    # ---------------------------
    # getter method for _city
    def get_city(self) -> str:
        """Returns the currently set city

        Args:
            None

        Returns:
            str: the currently set city

        """
        return self._city

    # ---------------------------
    # prints the menu for the Weather Forecasting Tool - only prints
    def _print_menu(self) -> None:
        """Prints the menu for the Weather Forecasting Tool

        Args:
            None

        Returns:
            None

        """

        print("======================================================")
        print("~~~~~~~~~~~ || Weather Forecasting Tool || ~~~~~~~~~~~")
        print("------------------------------------------------------")
        print("[00] Change City (Current: " + self._city + ")")
        print("[01] Current Weather Forecast")
        print("[02] Today's Weather Forecast")
        print("[03] Tomorrow's Weather Forecast")
        print("[04] 5 Day Weather Forecast")
        print("------------------------------------------------------")
        print("[-1] Exit")
        print("======================================================")

        return

    # ---------------------------
    # checks for Request Errors in data_dict
    def _check_error(self, data_dict) -> bool:
        """Checks for Request Errors in data_dict

        Args:
            data_dict (dict): the dictionary to be checked for Request Errors
        
        Returns:
            bool: True if Request Error is present, False otherwise

        """
        if str(data_dict["cod"]) != "200":
            print("------------------------ERROR-------------------------")
            print("Please check the error message below:")
            print("Error Code: " + str(data_dict["cod"]))
            print("Error Message: " + str(data_dict["message"]))
            print("------------------------------------------------------")
            return True
        
        return False

    # ---------------------------
    # fetches and prints the current weather forecast
    def _print_current(self) -> None:
        """Fetches and prints the current weather forecast

        Args:
            None

        Returns:
            None

        """
        data_dict = self._weather_forecasting_service.getCurrent()

        if self._check_error(data_dict):
            return
        
        print("------------------------------------------------------")
        print("City: " + data_dict["name"])
        print("Current Time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("Current Temperature: " + str(data_dict["main"]["temp"]) + " °C")
        print("Feels Like: " + str(data_dict["main"]["feels_like"]) + " °C")
        print("Weather: " + data_dict["weather"][0]["main"])
        print("Weather Description: " + data_dict["weather"][0]["description"].title())
        print("------------------------------------------------------")

        return

    # ---------------------------
    # fetches and prints the today's weather forecast (3 hour interval)
    def _print_today(self) -> None:
        """Fetches and prints the today's weather forecast (3 hour interval)

        Args:
            None

        Returns:
            None

        """
        data_dict = self._weather_forecasting_service.getToday()

        if self._check_error(data_dict):
            return
        
        cnt = 8

        print("------------------------------------------------------")
        print("City: " + data_dict["city"]["name"])

        for i in range(cnt):
            print("------------------------------------------------------")
            print("Time: " + datetime.fromtimestamp(data_dict["list"][i]["dt"]).strftime("%d/%m/%Y %H:%M:%S"))
            print("Temperature: " + str(data_dict["list"][i]["main"]["temp"]) + " °C")
            print("Weather: " + data_dict["list"][i]["weather"][0]["main"])
            print("Weather Description: " + data_dict["list"][i]["weather"][0]["description"].title())

        print("------------------------------------------------------")

        return

    # ---------------------------
    # fetches and prints the tomorrow's weather forecast (3 hour interval)
    def _print_tomorrow(self) -> None:
        """Fetches and prints the tomorrow's weather forecast

        Args:
            None

        Returns:
            None

        """
        data_dict = self._weather_forecasting_service.getTomorrow()

        if self._check_error(data_dict):
            return
        
        cnt = 8

        print("------------------------------------------------------")
        print("City: " + data_dict["city"]["name"])

        for i in range(cnt):
            print("------------------------------------------------------")
            print("Time: " + datetime.fromtimestamp(data_dict["list"][i+8]["dt"]).strftime("%d/%m/%Y %H:%M:%S"))
            print("Temperature: " + str(data_dict["list"][i+8]["main"]["temp"]) + " °C")
            print("Weather: " + data_dict["list"][i+8]["weather"][0]["main"])
            print("Weather Description: " + data_dict["list"][i+8]["weather"][0]["description"].title())

        print("------------------------------------------------------")

        return

    # ---------------------------
    # fetches and prints the 5 day weather forecast (3 hour interval)
    def _print_five_day(self) -> None:
        """Fetches and prints the 5 day weather forecast

        Args:
            None

        Returns:
            None

        """
        data_dict = self._weather_forecasting_service.getFiveDay()

        if self._check_error(data_dict):
            return

        cnt = 40

        print("------------------------------------------------------")
        print("City: " + data_dict["city"]["name"])

        for i in range(cnt):
            print("------------------------------------------------------")
            print("Time: " + datetime.fromtimestamp(data_dict["list"][i]["dt"]).strftime("%d/%m/%Y %H:%M:%S"))
            print("Temperature: " + str(data_dict["list"][i]["main"]["temp"]) + " °C")
            print("Weather: " + data_dict["list"][i]["weather"][0]["main"])
            print("Weather Description: " + data_dict["list"][i]["weather"][0]["description"].title())

        print("------------------------------------------------------")

        return

    # ---------------------------
    # starts the Weather Forecasting Tool
    @staticmethod
    def start():
        """Starts the Weather Forecasting Tool

        Args:
            None

        Returns:
            None

        """
        # create a WeatherForecastingTool object
        weather_forecasting_tool = WeatherForecastingTool()

        continue_flag = True

        while continue_flag:

            # clear the screen
            if platform == "win32":
                os.system("cls")
            else:
                os.system("clear")

            # print the menu
            weather_forecasting_tool._print_menu()

            # keep asking for the choice until a valid choice is entered
            invalid_choice = True
            while invalid_choice:
                choice = int(input("Enter your choice: "))
                invalid_choice = False
                if choice == 0:
                    # city name should not start with a number or a special character
                    invalid_city_name = True
                    while invalid_city_name:
                        city = input("Enter the city: ")
                        if city.replace(" ", "").isalpha():
                            invalid_city_name = False
                        else:
                            print("Invalid city name.\nPlease enter again.")

                    weather_forecasting_tool.set_city(city)
                    weather_forecasting_tool._weather_forecasting_service.set_city(city)
                    

                elif choice == 1:
                    weather_forecasting_tool._print_current()

                elif choice == 2:
                    weather_forecasting_tool._print_today()

                elif choice == 3:
                    weather_forecasting_tool._print_tomorrow()

                elif choice == 4:
                    weather_forecasting_tool._print_five_day()

                elif choice == -1:
                    continue_flag = False
                    continue

                else:
                    print("Invalid choice. Please enter again.")
                    invalid_choice = True

                input("NOTE: Screen will be cleared after this.\nPress Enter to continue...")
            # end of while invalid_choice    
        # end of while continue_flag

        return

    # ---------------------------

# --------- End of Class --------
# -------------------------------

if __name__ == "__main__":
    WeatherForecastingTool.start()