# Importation de paquets, bibliothèques et modules
from . import Engine
from ambiance import Atmosphere

#Table de correspondance associant à chaque avion un modèle de moteur, le nombre de moteur installé sur cet avion et l'altitude de croisière
correspondance_avions_moteurs = {
    #'AVION':('MOTEUR', Nombre de moteur, Altitude de croisière(ft), Mach de croisière, Nombre maximal de passagers, Payload (lb))
    #'' : Signifie que l'avion ne transporte pas de passager ou pas de marchandises 
    'AIRBUS A300 B4600': ('CF6-50A', 2, 35000, 0.82, 345, ''),
    'AIRBUS A318': ('CFM56-5B1', 2, 41000, 0.82, 136, ''),
    'AIRBUS A319': ('CFM56-5B1', 2, 41000, 0.82, 160, ''),
    'AIRBUS A320': ('CFM56-5B1', 2, 41000, 0.82, 180, ''),
    'AIRBUS A321': ('CFM56-5B1', 2, 41000, 0.82, 240, ''),
    'AIRBUS A330': ('Trent 772', 2, 41000, 0.82, 440, ''),
    'AIRBUS A330 200': ('Trent 772', 2, 41000, 0.86, 406, ''),
    'AIRBUS A330 300': ('PW4168', 2, 41000, 0.84, 440, ''),
    'AIRBUS A340 300': ('CFM56-5C4', 4, 39000, 0.84, 440, ''),
    'AIRBUS A340 600': ('Trent 556-61', 4, 39000, 0.84, 475, ''),
    'BAE AVRO 146RJ 200': ('ALF 502R-5', 4, 35000, 0.75, 100, ''),
    'BAE AVRO 146RJ 300': ('ALF 502R-5', 4, 35000, 0.75, 112, ''),
    'BOEING 737 300': ('CFM56-3-B1', 2, 41000, 0.82, 149, ''),
    'BOEING 737 400': ('CFM56-3C-1', 2, 41000, 0.82, 188, ''),
    'BOEING 737 500': ('CFM56-3-B1', 2, 41000, 0.82, 140, ''),
    'BOEING 737 700': ('CFM56-7B20', 2, 41000, 0.82, 149, ''),
    'BOEING 737 800': ('CFM56-7B26', 2, 41000, 0.82, 189, ''),
    'BOEING 747 400': ('PW4062', 4, 35000, 0.86, 660, '' ),
    'BOEING 747 400F': ('PW4062', 4, 35000, 0.86, '', 248600),
    'BOEING 757 200': ('PW2040', 2, 38000, 0.86, 239,''),
    'BOEING 757 200SF': ('PW2040', 2, 38000, 0.86, '',62000),
    'BOEING 757 300': ('RB211-535C', 2, 38000, 0.86, 295, ''),
    'BOEING 767 300ER': ('PW4060', 2, 35000, 0.84, 351, ''),
    'BOEING 767 300ERF': ('PW4060', 2, 35000, 0.84, '', 127000),
    'BOEING 777 200': ('GE90-77B', 2, 39000, 0.86, 440, ''),
    'BOEING 777 200ER': ('GE90-85B', 2, 39000, 0.86, 440, ''),
    'BOEING 777 300': ('PW4098', 2, 39000, 0.86, 550, ''),
    'BOMBARDIER BD1001A10': ('HTF7350 (AS907-2-1A)', 2, 45000, 0.82, 10, ''),
    'BOMBARDIER BD7001A10': ('BR700-710D5-21', 2, 42000, 0.85, 13, ''),
    'CANADAIR CL6002B16': ('CF34-3A', 2, 41000, 0.82, 12, ''),
    'DASSAULT FALCON 2000': ('PW308C', 2, 48000, 0.84, 10, ''),
    'DASSAULT FALCON 900': ('TFE731-3', 2, 51000, 0.85, 14, ''),
    'DASSAULT FALCON7X': ('PW307A', 3, 42000, 0.87, 16, ''),
    'EMBRAER EMB145': ('AE3007A', 2, 37000, 0.77, 50, ''),
    'EMBRAER ERJ195': ('CF34-10E2A1', 2, 41000, 0.78, 100, ''),
    'GRUMMAN G1159': ('SPEY Mk511', 2, 30000, 0.85, 14, ''),
    'GULFSTREAM G200': ('PW306A', 2, 45000, 0.8, 10, ''),
    'EMBRAER EMB135': ('AE3007A', 2, 37000, 0.77, 37, '')}

class Aircraft():
    '''
    Classe représentant un avion.
    '''
    #Constructeur 
    def __init__(self,modele,df_engine):
        '''Constructeur pour initialisation des informations de notre avion à partir du modèle entrée et 
        du dictionnaire de correspondance. 
        
        :param modele: Modele de l'avion 
        :type modele: string
        :param df_engine: Dataframe contenant les informations de tous les moteurs
        :type df_engine: Pandas Dataframe
        '''
        try: 
            #Modele de moteur associé à notre avion
            self.moteur = Engine.Moteur(correspondance_avions_moteurs[modele][0], df_engine)
            #Nombre de moteurs sur notre avion
            self.nombre_moteur = correspondance_avions_moteurs[modele][1]
            #Vitesse de croisiere de l'avion
            self.vitesse_croisiere = self.Vitesse_croisière(modele)
            #Altitude de croisière en m (initialement en ft)
            self.altitude_croisiere = correspondance_avions_moteurs[modele][2]/3.28 
            #Consommation de l'avion pour la phase LTO (g) et Croisière (g/s) 
            self.consommation_moteur_LTO, self.consommation_moteur_cruise = self.Emission_Avion()
 
        except KeyError:
            #Met fin au code si le modèle de l'avion est mal orthographié ou absent de notre base de donnée 
            print("Le modèle de l'avion saisi n'est pas dans notre base de donnée ou est mal orthographié")
            exit()

    #Méthodes          
    def Emission_Avion(self): 
        '''
        Retourne la masse de gaz rejeté en équivalent carbone pendant la phase de croisière de l'avion 
        en gramme par seconde (g/s) ainsi que la masse rejeté durant la phase LTO (Landing, Take Off) en gramme (g).
        Pour se faire, on calcul la consommation des moteurs et on multiplie par le nombre de moteurs.  
        
        :return: Masse équivalente de CO2 lors de la phase LTO et taux en g/s lors de la phase de croisière.
        :rtype: float
        '''
        #Taux de la phase de croisière
        taux_rejet_avion_cruise = self.nombre_moteur * self.moteur.Equivalent_CarboneParSeconde_Cruise()
        #Masse de la phase LTO 
        rejet_avion_LTO = self.nombre_moteur * self.moteur.Equivalent_Carbone_LTO()
        return rejet_avion_LTO, taux_rejet_avion_cruise 
    
    def Vitesse_croisière(self,modele):
        '''
        Retourne la vitesse de croisière de l'avion en m/s en fonction de son mach de croisière et de son altitude de croisière.  
        
        :param modele: Modele de l'avion 
        :type modele: string
        :return: vitesse de croisière de l'avion en m/s
        :rtype: float
        '''
        #On créé un objet atmosphère à l'altitude de croisière de l'avion
        atmosphere = Atmosphere(correspondance_avions_moteurs[modele][2])
        #Retourne la vitesse du son à l'altitude choisie (m/s)
        vitesse_son = atmosphere.speed_of_sound
        #Calcul de la vitesse de croisière grâce au mach de croisière (m/s)
        vitesse_croisiere = correspondance_avions_moteurs[modele][3]*vitesse_son
        return round(float(vitesse_croisiere),2)
   
class Freighter(Aircraft): 
    '''
    Classe représentant un avion transportant des marchandises.
    Cette classe hérite de la classe Aircraft.
    '''
    def __init__(self, modele, df_engine):
        '''Constructeur pour initialisation des informations de notre avion Cargo à partir du modèle entrée et 
        du dictionnaire. On réutilise le constructeur de la super classe.
        
        :param modele: Modele de l'avion 
        :type modele: string
        :param df_engine: Dataframe contenant les informations de tous les moteurs
        :type df_engine: Pandas Dataframe
        '''
        super().__init__(modele, df_engine)
        try:
            #Capacité de transport en lb de l'avion cargo
            self.payload = float(correspondance_avions_moteurs[modele][5])
        except ValueError : 
            #Si l'avion créé n'est pas un avion de fret 
            print(f"L'objet Freighter créé n'est pas un avion cargo ou n'est pas renseigné dans le dictionnaire")
            exit()
            
class Airliner(Aircraft): 
    '''
    Classe représentant un avion transportant des passagers.
    Cette classe hérite de la classe Aircraft.
    '''
    def __init__(self, modele, df_engine):
        '''Constructeur pour initialisation des informations de notre avion de ligne à partir du modele entrée et 
        du dictionnaire. On réutilise le constructeur de la super classe.
        
        :param modele: Modele de l'avion 
        :type modele: string
        :param df_engine: Dataframe contenant les informations de tous les moteurs
        :type df_engine: Pandas Dataframe
        '''
        super().__init__(modele, df_engine)
        try: 
            #Nombre de places passager dans l'avion
            self.nombre_passager = correspondance_avions_moteurs[modele][4]
        except ValueError : 
            #Si l'avion créé n'est pas un avion de ligne 
            print(f"L'objet Airliner créé n'est pas un avion de ligne ou n'est pas renseigné dans le dictionnaire")
            exit()
    