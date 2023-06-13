
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


#Création de mon objet moteur et affichage de sa consommation
moteur = Engine.Moteur('GE90-76B',df)

#Création de mon objet moteur 
avion = Aircraft.Aircraft('BOEING 737 300', df)

#Création d'un voyage entre deux aéroports 
voyage = Travel.travel('NHT', 'MSE', 'BOEING 737 300')

compagnie = Airline.Airline('BRITISH AIRWAYS', df_airline, df_fleet)

print(f"la compagnie:  {compagnie.df_airline}")

#TEST MOTEUR
print(f"Information de mon moteur : {moteur.df_moteur}")
print(f"Emission de CO2 lors de la phase LTO : {moteur.equivalent_carbone_LTO} g")
print(f"Emission de CO2 lors de la phase de croisière : {moteur.equivalent_carbone_seconde_cruise} g/s")

#TEST AVION
print(f"Le moteur de l'avion choisi est le moteur {avion.moteur.modele}")
print(f"Il y a {avion.nombre_moteur} moteur sur cet avion")
print(f"Vitesse : {avion.vitesse_croisiere} m/s")
print(f"Altitude : {avion.altitude_croisiere} m")

#TEST VOYAGE 
print(f"pollution du trajet : {voyage.pollution_trajet()}")



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
print(Donnees_dict)