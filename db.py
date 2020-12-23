"""
Database API
"""

import sqlite3 as lite
import os

class WeatherWrapper:

    def __init__(self, f):
        """
        Create wrapper object for database file with methods to interact with data.

        :param f: string, filename of database including extension
        """
        self.filename = f
        self.exists = self.__check_existence()
        if not self.exists:
            self.create()

    def connect(self):
        """
        Establish connection as attribute of this Wrapper object.
        """
        self.conn = lite.connect(self.filename)

    def close(self):
        """
        Commits and closes database connection.
        """
        self.conn.commit()
        self.conn.close()

    def __check_existence(self):
        this_path = os.path.abspath(os.path.dirname(__file__))
        these_files = os.listdir(this_path)
        if self.filename in these_files:
            return True
        else:
            return False
    
    def create(self):
        """
        Create database tables.
        """

        # Table 1 - LOCATION:
        SQL_CREATE_LOCATION = """
            CREATE TABLE IF NOT EXISTS LOCATION(
                ID int NOT NULL,
                NAME varchar(255),
                TIMEZONE int,
                LONGITUDE decimal,
                LATITUDE decimal
            )
            """

        # Table 2 - REPORT:
        SQL_CREATE_REPORT = """
            CREATE TABLE IF NOT EXISTS REPORT (
                ID int NOT NULL,
                MAIN varchar(25),
                DESCRIPTION varchar(255),
                TEMPERATURE varchar(255),
                FEELS_LIKE varchar(255),
                TEMPERATURE_MIN varchar(255),
                TEMPERATURE_MAX varchar(255),
                PRESSURE varchar(255),
                HUMIDITY varchar(255),
                VISIBILITY varchar(255),
                WIND_SPEED varchar(255),
                WIND_DIRECTION varchar(255)
            )
            """

        self.connect()
        self.conn.execute(SQL_CREATE_LOCATION)
        self.conn.execute(SQL_CREATE_REPORT)
        self.close()

    def insert(self, table, data_list):
        """
        Insert data_list to table.

        :param table: string, table name
        :param data_list: list of tuples, tuples correspond to fields for each entry
        """
        table_fields = {"LOCATION": "(ID, NAME, TIMEZONE, LONGITUDE, LATITUDE)",
                        "REPORT": """(ID, MAIN, DESCRIPTION, TEMPERATURE, FEELS_LIKE, TEMPERATURE_MIN, TEMPERATURE_MAX, PRESSURE,
                              HUMIDITY, VISIBILITY, WIND_SPEED, WIND_DIRECTION"""
        }

        fields = len(data_list[0])
        field_str = "(" + ", ".join(["?" for n in range(fields)]) + ")"

        table = table.upper()
        
        SQL_INSERT = f"""INSERT INTO {table} {table_fields[table]} VALUES {field_str}"""

        self.connect()
        self.conn.executemany(SQL_INSERT, data_list)
        self.close()

    
if __name__ == "__main__":

    d = WeatherWrapper("weather_test.db")

    test_data = [
        (12345, "Toronto", -1, 1.5, 1.5),
        (23456, "London", -2, 2.5, 2.5),
        (34567, "Ottawa", -3, 3.5, 3.5)
    ]

    d.insert("location", test_data)



    

