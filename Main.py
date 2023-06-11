import Data_Reader
import Engine
import Aircraft
import Airline 


df=Data_Reader.Emission_Data_Reader()
moteur = Engine.Moteur('GE90-76B',df)

print(moteur.df_moteur)
print(moteur.equivalent_carbone_LTO)