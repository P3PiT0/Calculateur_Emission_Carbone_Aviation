

import Data_Reader
import Engine
import Aircraft
import Airline 
import Travel
import Lecteuryamel
import sys

#Formatage du dataframe
df = Data_Reader.Emission_Data_Reader()

df_airline = Data_Reader.Airline_Data_Reader()

df_fleet = Data_Reader.Utilization_Data_Reader()

Airline.Comparaison_Pollution_Compagnie(df_airline,df,df_fleet)

compagnie = Airline.Airline('BRITISH AIRWAYS', df_airline, df_fleet, df)
print(f"Pollution compagnie : {compagnie.CO2_compagnie} ")
print(f"Pollution compagnie / passager reel : {compagnie.CO2_par_passager_reel}")
print(f"Pollution compagnie / passager optimal : {compagnie.CO2_par_passager_optimal} ")

def interface_utilisateur():
    print('\n BIENVENUE, voici un programme de responsabilité écologique et social du voyageur aéronautique ')
    print("\n Il vous permet de comparer l'impact écologique global par passager des différentes compagnies anglaises")
    print("\n Si vous prévoyez un voyage en avion (en Angleterre), vous pouvez également comparer l'impact écologique de différents vols")
    print(input("\n Veuillez remplir le fichier  'Donnees.yaml' afin de communiquer les entrées au programme puis appuyer sur ENTRER"))

    Entrees_yaml = Lecteuryamel.lecteuryamel()
    Donnees_dict = Entrees_yaml.print_content()

    if input("\n Validez-vous ces données ? (OUI/NON)") == 'OUI':
        return Donnees_dict
    else:
        print("\n Veuillez remplir le fichier 'Donnees.yaml' comme vous le souhaiter et réessayer")
        sys.exit()



Donnees_dict = interface_utilisateur()

if Donnees_dict['comparaison_compagnies']:
    #comsignes de comparaison de compagnies
    a=2
elif Donnees_dict['comparaison_VOLS']:
    voyage1 = Travel.travel(Donnees_dict['arrive_airport1'], Donnees_dict['depart_airport1'], Donnees_dict['avion1'])
    voyage2 = Travel.travel(Donnees_dict['arrive_airport2'], Donnees_dict['depart_airport2'], Donnees_dict['avion2'])
    print(f"pollution du trajet1 : {voyage1.pollution_trajet()} tonnes de CO2")
    print(f"pollution du trajet2 : {voyage2.pollution_trajet()} tonnes de CO2")
else:
    print("Veillez vous rendre sur le fichier 'Donnes.yaml' et y rentrer les donnees souhaitées")


