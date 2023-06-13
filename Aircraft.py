import Engine

#Table de correspondance associant à chaque avion un modèle de moteur ainsi que le nombre de moteur installé sur cet avion
correspondance_avions_moteurs = {
    'AIRBUS A300 B4600': ('CF6-50A', 2),
    'AIRBUS A318': ('CFM56-5B', 2),
    'AIRBUS A319': ('CFM56-5B', 2),
    'AIRBUS A320': ('CFM56-5B', 2),
    'AIRBUS A321': ('CFM56-5B', 2),
    'AIRBUS A330': ('Trent 772', 2),
    'AIRBUS A330 200': ('Trent 772', 2),
    'AIRBUS A330 300': ('PW4168', 2),
    'AIRBUS A340 300': ('CFM56-5C4', 4),
    'AIRBUS A340 600': ('Trent 556-61', 4),
    'ATR ATR72': ('', 2),
    'BAE ATP': ('', 2),
    'BAE AVRO 146RJ 200': ('', 4),
    'BAE AVRO 146RJ 300': ('', 4),
    'BAE JETSTREAM31 3100': ('', 2),
    'BAE JETSTREAM41 4100': ('', 2),
    'BEECH 300': ('', 2),
    'BOEING 737 300': ('CFM56-3-B1', 2),
    'BOEING 737 400': ('CFM56-3C-1', 2),
    'BOEING 737 500': ('CFM56-3-B1', 2),
    'BOEING 737 700': ('CFM56-7B20', 2),
    'BOEING 737 800': ('CFM56-7B26', 2),
    'BOEING 747 400': ('PW4062', 4),
    'BOEING 747 400F': ('PW4062', 4),
    'BOEING 757 200': ('PW2040', 2),
    'BOEING 757 300': ('RB211-535C', 2),
    'BOEING 767 300ER': ('PW4060', 2),
    'BOEING 777 200': ('GE90-77B', 2),
    'BOEING 777 200ER': ('GE90-85B', 2),
    'BOEING 777 300': ('PW4098', 2),
    'BOMBARDIER BD1001A10': ('', 2),
    'BOMBARDIER BD7001A10': ('', 2),
    'CANADAIR CL6002B16': ('', 2),
    'DASSAULT FALCON 2000': ('', 2),
    'DASSAULT FALCON 900': ('', 2),
    'DASSAULT FALCON7X': ('', 3),
    'DE HAVILLAND CANADA DHC8 300': ('', 2),
    'DE HAVILLAND CANADA DHC8 400': ('', 2)}


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