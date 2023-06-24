from sys import platform
import json

from src import WeatherForecastingService

class WeatherForecastingTool:

    def __init__(self) -> None:
        self.city = "Bangalore"

    def __init__(self, city) -> None:
        self.city = city

    def set_city(self, city) -> None:
        """Sets the city to be used for the weather forecasting tool
        """
        self.city = city
        return

    def get_city(self) -> str:
        """Returns the currently set city
        """
        return self.city

    def print_menu(self) -> None:
        """Prints the menu for the Weather Forecasting Tool
        """
        # make a menu with the following options:
        # 0. Change City (Current: )
        # 1. Current Weather Forecast
        # 2. Today's Weather Forecast
        # 3. Tomorrow's Weather Forecast
        # 4. 5 Day Weather Forecast
        # 5. Exit

        print("======================================================")
        print("~~~~~~~~~~~ || Weather Forecasting Tool || ~~~~~~~~~~~")
        print("------------------------------------------------------")
        print("[00] Change City (Current: )")
        print("[01] Current Weather Forecast")
        print("[02] Today's Weather Forecast")
        print("[03] Tomorrow's Weather Forecast")
        print("[04] 5 Day Weather Forecast")
        print("------------------------------------------------------")
        print("[-1] Exit")
        print("======================================================")

        return
    
    def print_current(self, current_weather) -> None:
        """Prints the current weather forecast
        """
        return
    
    def print_today(self, today_weather) -> None:
        """Prints the today's weather forecast
        """
        return
    
    def print_tomorrow(self, tomorrow_weather) -> None:
        """Prints the tomorrow's weather forecast
        """
        return
    
    def print_five_day(self, five_day_weather) -> None:
        """Prints the 5 day weather forecast
        """
        return

    @staticmethod
    def start():
        """Starts the Weather Forecasting Tool
        """
        # create a WeatherForecastingTool object
        weather_forecasting_tool = WeatherForecastingTool()
        continue_flag = True

        while continue_flag:
            # print the menu
            weather_forecasting_tool.print_menu()

            # keep asking for the choice until a valid choice is entered
            invalid_choice = True
            while invalid_choice:
                choice = int(input("Enter your choice: "))
                invalid_choice = False
                if choice == 0:
                    city = input("Enter the city: ")
                    weather_forecasting_tool.set_city(city)

                elif choice == 1:
                    pass

                elif choice == 2:
                    pass

                elif choice == 3:
                    pass

                elif choice == 4:
                    pass

                elif choice == -1:
                    continue_flag = False

                else:
                    print("Invalid choice. Please enter again.")
                    invalid_choice = True
        pass

if __name__ == "__main__":
    WeatherForecastingTool.start()



























