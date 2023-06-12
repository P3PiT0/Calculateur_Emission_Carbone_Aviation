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
avion = Aircraft.Aircraft('AIRBUS A300 B4600')

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