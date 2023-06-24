from src import WeatherForecastingService

class WeatherForecastingTool:

    def __init__(self) -> None:
        self.city = None

    def __init__(self, city) -> None:
        self.city = city

    def set_city(self, city) -> None:
        self.city = city

    def get_city(self) -> str:
        return self.city

    def print_menu(self) -> None:
        # make a menu with the following options:
        # 0. Change City (Current: )
        # 1. Current Weather Forecast
        # 2. Today's Weather Forecast
        # 3. Tomorrow's Weather Forecast
        # 4. 5 Day Weather Forecast
        # 5. Exit

        # ======================================================
        # ~~~~~~~~~~~ || Weather Forecasting Tool || ~~~~~~~~~~~
        # ------------------------------------------------------
        # [00] Change City (Current: )
        # [01] Current Weather Forecast
        # [02] Today's Weather Forecast
        # [03] Tomorrow's Weather Forecast
        # [04] 5 Day Weather Forecast
        # ------------------------------------------------------
        # [-1] Exit
        # ======================================================

        continueFlag = True
        while continueFlag:
            pass
        pass

    @staticmethod
    def start():
        pass


if __name__ == "__main__":
    WeatherForecastingService.get_api_key()
    WeatherForecastingTool.start()

