import requests
import datetime


class Caller:

    def __init__(self):
        self.key = "a49f7332c904727f99cd4b9791a826dc"
        
       

    def current_data(self, city):
        current_data_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}"
        call_time = datetime.datetime.now()
        j = requests.get(current_data_url).json()
        return (call_time, j)
        


class CurrentReport:

    def __init__(self, t):
        """
        Initialize a current weather report for one city.

        :param t: tuple, (datetime object, json String) - contains datetime of request call and returned json from API
        """
        self.timestamp = t[0]
        self.json = t[1]
        
        # assign data to variables:
        self.date = self.timestamp.date()
        self.time = self.timestamp.time()
        
        self.city = self.json["name"]
        self.weather = self.json["weather"]
        self.numeric = self.json["main"]
        self.celsius = float(self.numeric["temp"]) - 273.15     # Convert from Kelvin to Celsius

    def get_city(self):
        """
        Return String city name.
        """
        return self.city

    def get_date(self):
        """
        Return String in format "YYYY-MM-DD".
        """
        return f"{self.date.year}-{str(self.date.month).zfill(2)}-{str(self.date.day).zfill(2)}"

    def get_time(self):
        """
        Return String in 24-hour format "HH:MM".
        """
        return f"{str(self.time.hour).zfill(2)}:{str(self.time.minute).zfill(2)}"

    def get_classification(self):
        return self.weather[0]["main"]

    def get_temp(self):
        """
        Return String of temperature in degrees Celsius.
        """
        return str(self.celsius)




if __name__ == "__main__":
    c = Caller()
    r = c.current_data("Toronto")
    cr = CurrentReport(r)
    print(cr.get_date())
