import csv
import json

class CsvReader:

    def __init__(self, fileName, mode='normal'):
        """
        fileName: a csv file to be read
        mode: reading mode, normal reader or dict reader
        """
        self.fileName = fileName
        self.fileHandler = open(self.fileName, 'r+')
        
        if (mode == "dict"):
            self.reader = csv.DictReader(self.fileHandler)
        else:
            self.reader = csv.reder(self.fileHandler)
        
        #use the firt row as the column name
        self.columnName = self.getRecord()
        
    def dumpToJson(self, fileName, record):
        """
        dump a recod to a json file to read with ease
        """
        if(self.mode == "dict"):
            jfile = open(fileName, 'w+')

            json.dump(record, jfile)

    def getRecord(self):
        return next(self.reader)

# a table mapping database keys to record keys, can be changed 
# according to diffrent needs
nameTable = {
    "AID" : "ID",
    "Source" : "Source",
    "TMC" : "TMC",
    "Severity" : "Severity",
    "StartTime" : "Start_Time",
    "EndTime" : "End_Time",
    "Distance" : "Distance(mi)",
    "Description" : "Description",
    
    "LAID" : "ID",
    "StartLat" : "Start_Lat",
    "StartLng" : "Start_Lng",
    "EndLat" : "End_Lat",
    "EndLng" : "End_Lng",
    "_Number" : "Number",
    "Street" : "Street",
    "Side" : "Side",
    "City" : "City",
    "County" : "County",
    "_State" : "State",
    "Zipcode" : "Zipcode",
    "Country" : "Country",
    "Timezone" : "Timezone",
    "AirportCode" : "Airport_Code",
    
    "WAID" : "ID",
    "WeatherTimeStamp" : "Weather_Timestamp",
    "Temperature" : "Temperature(F)",
    "WindChill" : "Wind_Chill(F)",
    "Humidity" : "Humidity(%)",
    "Pressure" : "Pressure(in)",
    "Visibility" : "Visibility(mi)",
    "WindDirection" : "Wind_Direction",
    "WindSpeed" : "Wind_Speed(mph)",
    "Precipitation" : "Precipitation(in)",
    "WeatherCondition" : "Weather_Condition",
    
    "PAID" : "ID",
    "Amenity" : "Amenity",
    "Bump" : "Bump",
    "Crossing" : "Crossing",
    "GiveWay" : "Give_Way",
    "Junction" : "Junction",
    "NoExit" : "No_Exit",
    "RailWay" : "Railway",
    "RoundAbout" : "Roundabout",
    "Station" : "Station",
    "Stop" : "Stop",
    "TrafficCalmig" : "Traffic_Calming",
    "TrafficSignal" : "Traffic_Signal",
    "TurningLoop" : "Turning_Loop",
    
    "TAID" : "ID",
    "SunriseSunset" : "Sunrise_Sunset",
    "CivilTwilight" : "Civil_Twilight",
    "NauticalTwilight" : "Nautical_Twilight",
    "AstronomicalTwilight" : "Astronomical_Twilight",
} 


def parser(record):
    """
    paser one record into several dictionaris
    record: a dictionary returned by CsvReader.getRecord
    return: a tuple containing several dictionaries
    """
    
    