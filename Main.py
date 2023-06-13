
import Data_Reader
import Engine
import Aircraft
import Airline 
import Travel

#Formatage du dataframe
df=Data_Reader.Emission_Data_Reader()


#Création de mon objet moteur et affichage de sa consommation
moteur = Engine.Moteur('GE90-76B',df)

#Création de mon objet moteur 
avion = Aircraft.Aircraft('AIRBUS 300 B4600')

#Création d'un voyage entre deux aéroports 
voyage = Travel.travel('BHX', 'CVT')

#TEST MOTEUR
print(f"Information de mon moteur : {moteur.df_moteur}")
print(f"Emission de CO2 lors de la phase LTO : {moteur.equivalent_carbone_LTO} g")
print(f"Emission de CO2 lors de la phase de croisière : {moteur.equivalent_carbone_seconde_cruise} g/s")

#TEST AVION
print(f"Le moteur de l'avion choisi est le moteur {avion.modele_moteur}")
print(f"Il y a {avion.nombre_moteur} moteur sur cet avion")

#TEST VOYAGE 
print(voyage.distance_travel())

def interface_utilisateur():
    print('BIENVENUE, voici un programme de responsabilité écologique et social du voyageur aéronautique ')
    print("\n Il vous permet de comparer l'impact écologique global par passager des différentes compagnies anglaises")
    print("\n Si vous prévoyez un voyage en avion (en Angleterre), vous pouvez également comparer l'impact écologique de différents vols")
    print("\n Veuillez remplir le fichier  'Donnees.yaml' afin de communiquer les entrées au programme puis appuyer sur ENTRER")

