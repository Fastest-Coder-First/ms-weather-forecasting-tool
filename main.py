from src import WeatherForecastingTool

if __name__ == "__main__":
    # build a command line tool to get the weather forecast for a given city
    print("Welcome to the Weather Forecasting Tool!")
    continueFlag = True
    while continueFlag:
        city = input("Please enter a city name: ")
        weatherForecastingTool = WeatherForecastingTool()
        weatherForecastingTool.getWeatherForecast(city)
        # ask the user if they want to continue, accept 'y', 'Y', 'n', 'N' only
        invalidChoice = True
        while invalidChoice:
            choice = input("Would you like to continue? (y/n): ")
            if choice == 'y' or choice == 'Y':
                invalidChoice = False
            elif choice == 'n' or choice == 'N':
                invalidChoice = False
                continueFlag = False
            else:
                print("Invalid choice, please enter again.")

    
        
    print("Thank you for using the Weather Forecasting Tool!")
