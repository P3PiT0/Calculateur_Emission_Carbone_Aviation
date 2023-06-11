import pandas as pd

class Moteur(): 
    '''
    Docstring
    '''
    
    #Attribut
    
    #Constructeur 
    def __init__(self,modele,df_global):
        '''
        Constructeur pour initialisation du modèle ainsi que des différentes informations du moteur grâce à un df
        
        :param modele: Modele du moteur 
        :type modele: string
        :param df_global: Dataframe contenant les informations de tous les moteurs
        :type constructeur: Pandas Dataframe
        '''
        self.modele = modele 
        #Selectionne et retourne la ligne de notre dataframe contenant le modèle de notre moteur avec ses informations
        self.df_moteur = df_global.loc[df_global['Modele'] == modele]
        #On réinitialise l'index à 1
        self.df_moteur.reset_index(drop=True, inplace=True)
        #On calcul la masse de CO2 émise durant la phase LTO (g)
        self.equivalent_carbone_LTO = self.Equivalent_Carbone_LTO()
   
    #Méthodes 
    def Conversion_Equivalent_Carbone (self, HC_value, CO_value, NOx_value):
        '''
        Retourne l'équivalent carbone de chaque gaz en fonction de son PRG (Potentiel Réchauffement Global) 
        sur 100 ans. 
        
        :param HC_value: Taux Hydrocarbure HC 
        :type HC_value: float
        :param CO_value: Taux Monoxyde de Carbone CO 
        :type CO_value: float
        :param NOx_value: Taux Oxyde d'Azote NOx 
        :type NOx_value: float
        
        :return: Renvoi les taux équivalent CO2 .
        :rtype: liste.
        '''
        #Potentiel Réchauffement Global des gaz étudiés
        PRG_CO = 1
        PRG_HC = 28 #Hypothèse du méthane (plus présent en aéronautique)
        PRG_NOx = 300 
        
        return [HC_value*PRG_HC, CO_value*PRG_CO, NOx_value*PRG_NOx]
    
    def Equivalent_Carbone_LTO(self): 
        '''
        Retourne la masse rejeté en équivalent carbone pour la phase LTO (phase de décollage, d'atterrissage 
        et de montée) du moteur en gramme (g). 
        
        :return: Masse équivalent CO2 de la phase LTO en gramme.
        :rtype: float
        '''    
        #Conversion en équivalent carbone
        equivalent_carbone = self.Conversion_Equivalent_Carbone(self.df_moteur.loc[0,'HC_LTO'],self.df_moteur.loc[0,'CO_LTO'],self.df_moteur.loc[0,'NOx_LTO'])
        masse_CO2_LTO = sum(equivalent_carbone)
        return masse_CO2_LTO
    
    def Taux_Carbone_Cruise(self): 
        '''
        Retourne le taux en équivalent carbone rejeté (en g/kg de kérosène consommé) pour la phase de croisière. 
        
        :return: Taux équivalent CO2 de la phase de croisière g/kg.
        :rtype: float
        '''    
    
        return taux_CO2_cruise
    
    def Equivalent_Carbone_Cruise(self): 
        '''
        Retourne la masse rejeté en équivalent carbone pendant la phase de croisière du moteur 
        en gramme par seconde (g/s). 
        
        :return: Masse équivalent CO2 de la phase cruise en gramme/s.
        :rtype: float
        ''' 
    
    