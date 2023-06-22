import airportsdata
import math as mt
from Modules import Aircraft
from . import Data_Reader

#Importation des données, un dictionnaire contenant les aéroports pris en compte et un dataframe contenant les données sur les émissions de gaz à effet de serre
airports = airportsdata.load('IATA')
df= Data_Reader.Emission_Data_Reader()

class travel():
    '''
    Docstring
    '''

    def __init__(self, arrive_airport, depart_airport, aircraft):
        '''Constructeur pour initialisation dede la classe travel, celle-ci contient trois attributs : 
        Les codes iata des aéroports d'arrivée/départ du voyage et l'objet avion réalisant le vol 
        
        :param arrive_airport: code IATA de l'aéroport d'arrivée 
        :type arrive_airport: string
        :param depart_airport: code IATA de l'aéroport de départ
        :type depart_airport: string
        :param aircraft: Modèle de l'avion sélectionné
        :type aircraft: string
        '''
        self.arrive_airport = arrive_airport
        self.depart_airport = depart_airport
        self.aircraft = Aircraft(aircraft, df)

    def distance_croisiere(self):
        '''Fonction qui calcule la distance de croisière du voyage
        Celle-ci est retournée en km
        
        :return: distance du voyage en km 
        :rtype: float
        '''
        #Calculs de latitude et longitude des aéroports en radian
        lat1 = airports[self.depart_airport]['lat']*mt.pi/180
        lon1 = airports[self.depart_airport]['lon']*mt.pi/180

        lat2 = airports[self.arrive_airport]['lat']*mt.pi/180
        lon2 = airports[self.arrive_airport]['lon']*mt.pi/180

        #Calcul de la distance de croisière : on calcule le rayon du trajet à l'altitude de croisière et on retranche les phases de montée et de descente comprises dans la phase LTO
        distance = mt.acos((mt.sin(lat1)*mt.sin(lat2)) + mt.cos(lat1)*mt.cos(lat2)*mt.cos(lon1-lon2))*(6371+self.aircraft.altitude_croisiere/1000) - 0.914/(mt.tan(5*mt.pi/180)) - 0.914/(mt.tan(3*mt.pi/180))

        #Si l'avion n'entre pas dans la phase de croisière(la distance est inférieure à zero), alors on retourne zero
        if distance < 0:
            distance = 0
        #On retourne la distance de croisière
        return(distance)
    
    def pollution_trajet(self):
        '''Fonction qui calcule et renvoie l'émission de CO2 du trajet en question à partir des données disponibles sur l'avion et ses moteurs
        l'émission est renvoyée en tonnes de CO2
        
        :return: pollution du voyage en tonnes de CO2 
        :rtype: float
        '''
        #Récupération des émissions de CO2 de la phase LTO par seconde de l'avion en question
        Emission_CO2_LTO = self.aircraft.moteur.equivalent_carbone_LTO
        Emission_CO2_cruise = self.aircraft.moteur.equivalent_carbone_seconde_cruise

        #Calcul des émissions totales du trajet en calculant le temps passé en croisière grâce à la distance de croisière et à la vitesse de croisière de l'avion
        emissions_trajet = self.distance_croisiere()*1000*Emission_CO2_cruise/(self.aircraft.vitesse_croisiere) + Emission_CO2_LTO
        #On retourne le poids de CO2 en tonne
        return round(emissions_trajet/1000000,3)

        