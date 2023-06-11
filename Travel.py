import airportsdata
import math as mt
import pandas as pd

airports = airportsdata.load('IATA')
airports_df = pd.DataFrame(airports)
airports_df = airports_df.transpose()
airports_gb = airports_df[airports_df.subd == 'England'].reset_index(drop=True)

class travel:
    '''
    Docstring
    '''

    def __init__(self, arrive_airport, depart_airport):
        self.arrive_airport = arrive_airport
        self.depart_airport = depart_airport

    def distance_travel(self):
        lat1 = airports[self.depart_airport]['lat']*mt.pi/180
        lon1 = airports[self.depart_airport]['lon']*mt.pi/180

        lat2 = airports[self.arrive_airport]['lat']*mt.pi/180
        lon2 = airports[self.arrive_airport]['lon']*mt.pi/180

        distance = mt.acos((mt.sin(lat1)*mt.sin(lat2)) + mt.cos(lat1)*mt.cos(lat2)*mt.cos(lon1-lon2))*6371
        return(distance)