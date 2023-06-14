import Aircraft
class Airline(): 
    '''
    Docstring
    '''
    
    #Attribut
    
    #Constructeur 
    def __init__(self, compagnie, df_airline, df_fleet):
        '''
        Constructeur pour initialisation des compagnies aériennes

        :param nom: Nom de la compagnie
        :type nom: string
        :param df_airline: Dataframe contenant les informations sur les compagnies
        :type constructeur: Pandas Dataframe
        '''
        try:
            self.compagnie = compagnie
            # Selectionne et retourne la ligne de notre dataframe contenant les informations sur notre compagnie
            # Réinitialisation de l'index à 1
            self.df_airline = df_airline.loc[df_airline['Airline'] == compagnie]
            self.df_airline.reset_index(drop=True, inplace=True)
            # Selectionne et retourne les informations sur la flotte de la compagnie
            # Réinitialisation de l'index à 1
            self.df_fleet = df_fleet.loc[df_fleet['Airline'] == compagnie]
            self.df_fleet.reset_index(drop=True, inplace=True)
            # Pourcentage d'occupation sur l'année 2010
            self.load_factor = self.df_airline.loc[0,'LoadFactor']
            # Nombre total de passager sur l'année 2010
            self.total_passenger = self.df_airline.loc[0,'TotalPassenger']
            # Nombre d'heure de vol de la flotte sur l'année
            self.total_hours = self.df_fleet['TotalHours'].sum()
            # Flotte de la compagnie [Avion,Passenger ou Freighter, Pourcentage d'utilisation sur le temps total]
            self.flotte = [self.df_fleet.loc[:, 'Name'],self.df_fleet.loc[:, 'Type'],self.df_fleet.loc[:, 'Days'],(self.df_fleet.loc[:, 'TotalHours']/self.total_hours)]

        except KeyError:
            # Met fin au code si le nom saisie n'est pas dans la base de donnée
            print("Le nom de la compagnie saisi n'est pas dans notre base de donnée ou est mal orthographié")
            exit()
            
    #Méthodes
    def CO2_total_compagnie(self,nombre_jour,df): 
        CO2_total = 0 
        for avion in self.flotte[0] :
            modele_avion = Aircraft.Aircraft(avion, df)
            #On fait l'hypothèse 
            CO2_total = modele_avion.consommation_moteur_LTO()*nombre_jour*2
            
   

