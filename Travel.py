import airportsdata
import math as mt
import pandas as pd
import csv

airports = airportsdata.load('IATA')
airports_df = pd.DataFrame(airports)
airports_df = airports_df.transpose()
airports_gb_df = airports_df[airports_df.subd == 'England'].reset_index(drop=True)
airports_gb_df.index = airports_gb_df['iata']
airports_gb = airports_gb_df.transpose().to_dict()
print(airports_gb['BHX'])


with open('airports.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(airports_gb['BHX'].keys())
    for key in airports_gb:
        writer.writerow((airports_gb[key].values()))

class travel:
    '''
    Docstring
    '''

    def __init__(self, arrive_airport, depart_airport):
        self.arrive_airport = arrive_airport
        self.depart_airport = depart_airport

    def distance_travel(self):
        lat1 = airports_gb[self.depart_airport]['lat']*mt.pi/180
        lon1 = airports_gb[self.depart_airport]['lon']*mt.pi/180

        lat2 = airports_gb[self.arrive_airport]['lat']*mt.pi/180
        lon2 = airports_gb[self.arrive_airport]['lon']*mt.pi/180

        distance = mt.acos((mt.sin(lat1)*mt.sin(lat2)) + mt.cos(lat1)*mt.cos(lat2)*mt.cos(lon1-lon2))*6371
        return(distance)