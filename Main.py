import Data_Reader
import Engine
import Aircraft
import Airline 

#Formatage du dataframe
df=Data_Reader.Emission_Data_Reader()


#Création de mon objet moteur et affichage de sa consommation
moteur = Engine.Moteur('GE90-76B',df)

print(moteur.df_moteur)
print(moteur.equivalent_carbone_LTO)
print(moteur.equivalent_carbone_seconde_cruise)