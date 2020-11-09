"""
This script is used to insert all data into the mysql database,
and provids some managements if possible
"""

import mysql.connector
import CsvReader

class DataBase:

    def __init__(self, table, login, reader):
        """
        a class used to manage  all manipulaitons of database "table"
        table: database nameTable
        login: a tuple containing login information
        reader: an object retrving recorders
        """
        self.connection = mysql.connector.connect\
        (user=login[0], password=login[1],database=table)
        
        self.cursor = self.connection.cursor()
        self.reader = reader
        
    def insert(self, tableName, keys, record):
        """
        apply insert operation to table "tableName" using value in "values"
        tableName : the name of the table to be manipulated
        keys : keys of the table
        record: all key values
        """
        addSql = "insert into {Name}".format(Name = tableName) + "(" +\
        ",".join(keys) + ")" +\
        "values (" + ("%s, "*len(keys)).rstrip(' ').rstrip(',') + ")"
        
        nameTable = CsvReader.nameTable
        dataSql = []
        for key in keys:
            value = record[nameTable[key]]
            if value == '':
                value = None 
            dataSql.append(value)
        dataSql = tuple(dataSql)
        
        print(addSql)
        print(dataSql)
        
        self.cursor.execute(addSql, dataSql)
        self.connection.commit()
    
    def insertAll(self):
    
        while(True):
            try:
                record = self.reader.getRecord()
                
                #insert into accident table
                self.insert("Accident", ["AID", "Source", "TMC", "Severity", \
                "StartTime", "EndTime", "Distance", "Description"], record)
                
                #insert into Location table
                self.insert("Location", ["LAID","StartLat", "StartLng", "EndLat", \
                "EndLng", "_Number", "Street", "Side" , "City" , "County", \
                "_State", "Zipcode", "Country", "Timezone", "AirportCode"], record)
                
                #insert into WeatherCondition table
                self.insert("WeatherCondition", ["WAID","WeatherTimeStamp", "Temperature", \
                "WindChill", "Humidity", "Pressure", "Visibility", "WindDirection", \
                "WindSpeed", "Precipitation", "WeatherCondition"], record)       
                
                #insert into PointOfInterst table
                self.insert("PointOfInterst", ["PAID","Amenity", "Bump", "Crossing", \
                "GiveWay", "Junction", "NoExit", "RailWay", "RoundAbout", \
                "Station", "Stop", "TrafficCalmig", "TrafficSignal", "TurningLoop"], record)
                
                #insert into the Twilight table
                self.insert("Twilight", ["TAID","SunriseSunset", "CivilTwilight", \
                "NauticalTwilight", "AstronomicalTwilight"], record)
            except StopIteration:
                break
     
    def bye(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

reader = CsvReader.CsvReader('../US_Accidents_June20.csv', 'dict')
db = DataBase("CarAccident", ("root", "314159265"), reader)
db.insertAll()
db.bye()