import requests
import datetime
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
env_file = "keys.env"



class Caller:

    def __init__(self):
        load_dotenv(os.path.join(basedir, env_file))
        self.key = os.getenv("API_KEY")
        self.api_response = None
        
    def response(self):
        """Return bool, True if response 200, False if response 404 or other, but return None if not called yet."""
        if self.api_response == 200:
            return True
        elif self.api_response == None:
            return None
        else:
            return False # 404 and any other value



    def report(self, city):
        
        current_data_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}"
        call_time = datetime.datetime.now()
        j = requests.get(current_data_url).json()
        self.api_response = j['cod']

        return CurrentReport(call_time, j)
        
        

class CurrentReport:

    def __init__(self, t, j):
        """
        Initialize a current weather report for one city.

        :param t: tuple, (datetime object, json String) - contains datetime of request call and returned json from API
        """
        self.timestamp = t
        self.json = j
        self.response = self.json["cod"]

        if self.response == 200:
            # assign data to variables:
            self.city = self.json["name"]
            self.date = self.timestamp.date()
            self.time = self.timestamp.time()
            self.weather = self.json["weather"]
            self.numeric = self.json["main"]
            self.celsius = round(float(self.numeric["temp"]) - 273.15, 2)           # Convert from Kelvin to Celsius
            self.feels = round(float(self.json["main"]["feels_like"]) - 273.15, 2)  # Convert from Kelvin to Celsius

    def simple_report(self):
        """
        Return dict of data.
        """
        data = {
            "city": self.city,
            "date": f"{self.date.year}-{str(self.date.month).zfill(2)}-{str(self.date.day).zfill(2)}",
            "time": f"{str(self.time.hour).zfill(2)}:{str(self.time.minute).zfill(2)}",
            "class": self.weather[0]["main"],
            "temp": str(self.celsius),
            "feels": str(self.feels)
        }

        return data


