import Engine

#Table de correspondance associant à chaque avion un modèle de moteur, le nombre de moteur installé sur cet avion et l'altitude de croisière
correspondance_avions_moteurs = {
    'AIRBUS A300 B4600': ('CF6-50A', 2, 35000),
    'AIRBUS A318': ('CFM56-5B', 2, 41000),
    'AIRBUS A319': ('CFM56-5B', 2, 41000),
    'AIRBUS A320': ('CFM56-5B', 2, 41000),
    'AIRBUS A321': ('CFM56-5B', 2, 41000),
    'AIRBUS A330': ('Trent 772', 2, 41000),
    'AIRBUS A330 200': ('Trent 772', 2, 41000),
    'AIRBUS A330 300': ('PW4168', 2, 41000),
    'AIRBUS A340 300': ('CFM56-5C4', 4, 39000),
    'AIRBUS A340 600': ('Trent 556-61', 4, 39000),
    'ATR ATR72': ('Turboprop', 2, 15000),
    'BAE ATP': ('Turboprop', 2, 15000),
    'BAE AVRO 146RJ 200': ('ALF 502R-5', 4, 35000),
    'BAE AVRO 146RJ 300': ('ALF 502R-5', 4, 35000),
    'BAE JETSTREAM31 3100': ('Turboprop', 2, 25000),
    'BAE JETSTREAM41 4100': ('Turboprop', 2, 25000),
    'BEECH 300': ('Turboprop', 2, 35000),
    'BOEING 737 300': ('CFM56-3-B1', 2, 41000),
    'BOEING 737 400': ('CFM56-3C-1', 2, 41000),
    'BOEING 737 500': ('CFM56-3-B1', 2, 41000),
    'BOEING 737 700': ('CFM56-7B20', 2, 41000),
    'BOEING 737 800': ('CFM56-7B26', 2, 41000),
    'BOEING 747 400': ('PW4062', 4, 35000),
    'BOEING 747 400F': ('PW4062', 4, 35000),
    'BOEING 757 200': ('PW2040', 2, 38000),
    'BOEING 757 300': ('RB211-535C', 2, 38000),
    'BOEING 767 300ER': ('PW4060', 2, 35000),
    'BOEING 777 200': ('GE90-77B', 2, 39000),
    'BOEING 777 200ER': ('GE90-85B', 2, 39000),
    'BOEING 777 300': ('PW4098', 2, 39000),
    'BOMBARDIER BD1001A10': ('HTF7350', 2, 45000),
    'BOMBARDIER BD7001A10': ('BR700-710D5-21', 2, 42000),
    'CANADAIR CL6002B16': ('CF34-3A', 39000),
    'DASSAULT FALCON 2000': ('PW308C', 2, 39000),
    'DASSAULT FALCON 900': ('TFE731-3', 2, 36000),
    'DASSAULT FALCON7X': ('PW307A', 3, 36000),
    'DE HAVILLAND CANADA DHC8 300': ('Turboprop', 2, 20000),
    'DE HAVILLAND CANADA DHC8 400': ('Turboprop', 2, 20000)}


class Aircraft(): 
    '''
    Docstring
    '''
    #Constructeur 
    def __init__(self,modele,df_global):
        '''Constructeur pour initialisation des informations de notre avion à  partir du modele entrée et 
        du dictionnaire 
        
        :param modele: Modele de l'avion 
        :type modele: string
        '''
        try: 
            #Modele de moteur associé à notre avion
            self.modele_moteur = correspondance_avions_moteurs[modele][0]
            #Nombre de moteurs sur notre avion
            self.nombre_moteur = correspondance_avions_moteurs[modele][1]
            #Consommation de l'avion pour la phase LTO
            self.consommation_moteur_LTO, self.consommation_moteur_cruise = self.Consommation_Avion(df_global)
            
        except KeyError:
            #Met fin au code si le modèle de l'avion est mal orthographié ou absent de notre base de donnée 
            print("Le modèle d'avion saisi n'est pas dans notre base de donnée ou est mal orthographié")
            exit()
            
    def Consommation_Avion(self,df_global): 
        '''
        Retourne la masse rejeté en équivalent carbone pendant la phase de croisière de l'avion 
        en gramme par seconde (g/s) ainsi que la masse rejeté durant la phase LTO en gramme (g).
        Pour se faire, on calcul la consommation des moteurs et on multiplie par le nombre de moteurs.  
        
        :return: Masse équivalente de CO2 lors de la phase LTO et taux en g/s lors de la phase de croisière.
        :rtype: float
        '''
        moteur = Engine.Moteur(self.modele_moteur,df_global)
        taux_rejet_avion_cruise = self.nombre_moteur * moteur.Equivalent_CarboneParSeconde_Cruise()
        rejet_avion_LTO = self.nombre_moteur * moteur.Equivalent_Carbone_LTO()
        return rejet_avion_LTO, taux_rejet_avion_cruise 
    
            

        
        
    #Méthodes 