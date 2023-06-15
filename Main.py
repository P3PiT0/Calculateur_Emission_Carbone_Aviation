
#import Modules_Calculateur_Emission_Carbone_Aviation
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
    print('\n\nMENU COMPARAISON DES COMPAGNIES')
    print('Voici un diagramme barre de comparaison des émission de CO2/passager des différentes compagnies aériennes britannique')
    Airline.Comparaison_Pollution_Compagnie(df_airline,df,df_fleet)
if Donnees_dict['analyse_compagnie_particuliere']:
    print('\n\nMENU ANALYSE DE COMPAGNIE')
    print(f"Voici une analyse plus précise de la compagnie {Donnees_dict['compagnie']}")
    compagnie = Airline.Airline(Donnees_dict['compagnie'], df_airline, df_fleet, df)
    print(f"Pollution compagnie : {compagnie.CO2_compagnie_total/1000000} tonnes de CO2 en 2010")
    print(f"Pollution compagnie / passager reel : {compagnie.CO2_par_passager_reel/1000000} tonnes de CO2 par personne")
    print(f"Pollution compagnie / passager optimal : {compagnie.CO2_par_passager_optimal/1000000} tonnes de CO2 par personne")
    print(f"Voici un diagramme montrant la répartition des émissions de CO2 de la compagnie {Donnees_dict['compagnie']} en fonction du type de vol effectué")
    compagnie.Repartition_Emission_Type_Vol()
if Donnees_dict['comparaison_VOLS']:
    print('\n\nMENU COMPARAISON DE VOLS')
    print('Voici la comparaison des émissions de CO2 de deux vols')
    voyage1 = Travel.travel(Donnees_dict['arrive_airport1'], Donnees_dict['depart_airport1'], Donnees_dict['avion1'])
    voyage2 = Travel.travel(Donnees_dict['arrive_airport2'], Donnees_dict['depart_airport2'], Donnees_dict['avion2'])
    print(f"\nTrajet1 : {Donnees_dict['depart_airport1']}->{Donnees_dict['arrive_airport1']} à bord d'un {Donnees_dict['avion1']}")
    print(f"Pollution du trajet1 : {voyage1.pollution_trajet()} tonnes de CO2")
    print(f"Pollution par passager : {voyage1.pollution_trajet()/voyage1.aircraft.nombre_passager} tonnes de CO2 par passager")
    print(f"\nTrajet2 : {Donnees_dict['depart_airport2']}->{Donnees_dict['arrive_airport2']} à bord d'un {Donnees_dict['avion2']}")
    print(f"Pollution du trajet2 : {voyage2.pollution_trajet()} tonnes de CO2")
    print(f"Pollution par passager : {voyage2.pollution_trajet()/voyage2.aircraft.nombre_passager} tonnes de CO2")

if (not Donnees_dict['comparaison_VOLS']) and (not Donnees_dict['comparaison_compagnies']) and (not Donnees_dict['analyse_compagnie_particuliere']):
    print("Veillez vous rendre sur le fichier 'Donnes.yaml' et y rentrer les donnees souhaitées")


