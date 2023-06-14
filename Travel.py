import airportsdata
import math as mt
import pandas as pd
import csv
import Aircraft
import Data_Reader

airports = airportsdata.load('IATA')
airports_df = pd.DataFrame(airports)
airports_df = airports_df.transpose()
airports_gb_df = airports_df[airports_df.subd == 'England'].reset_index(drop=True)
airports_gb_df.index = airports_gb_df['iata']
airports_gb = airports_gb_df.transpose().to_dict()

df=Data_Reader.Emission_Data_Reader()

with open('Data/AirportData.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(airports_gb['BHX'].keys())
    for key in airports_gb:
        writer.writerow((airports_gb[key].values()))

class travel():
    '''
    Docstring
    '''

    def __init__(self, arrive_airport, depart_airport, aircraft):
        self.arrive_airport = arrive_airport
        self.depart_airport = depart_airport
        self.aircraft = Aircraft.Aircraft(aircraft, df)

    def distance_croisiere(self):
        lat1 = airports_gb[self.depart_airport]['lat']*mt.pi/180
        lon1 = airports_gb[self.depart_airport]['lon']*mt.pi/180

        lat2 = airports_gb[self.arrive_airport]['lat']*mt.pi/180
        lon2 = airports_gb[self.arrive_airport]['lon']*mt.pi/180

        distance = mt.acos((mt.sin(lat1)*mt.sin(lat2)) + mt.cos(lat1)*mt.cos(lat2)*mt.cos(lon1-lon2))*(6371+self.aircraft.altitude_croisiere/1000) - 0.914/(mt.tan(5*mt.pi/180)) - 0.914/(mt.tan(3*mt.pi/180))
        if distance < 0:
            distance = 0
        return(distance)
    
    def pollution_trajet(self):
        moteur_avion = self.aircraft.moteur
        nombre_moteur_avion =  self.aircraft.nombre_moteur

        Emission_CO2_LTO = self.aircraft.moteur.equivalent_carbone_LTO
        Emission_CO2_cruise = self.aircraft.moteur.equivalent_carbone_seconde_cruise

        emissions_trajet = self.distance_croisiere()*1000*Emission_CO2_cruise/(self.aircraft.vitesse_croisiere) + Emission_CO2_LTO
        return emissions_trajet

        