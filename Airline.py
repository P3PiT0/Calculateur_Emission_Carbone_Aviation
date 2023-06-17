import Aircraft
import matplotlib.pyplot as plt
import numpy as np
class Airline(): 
    '''
    Docstring
    '''
    
    #Attribut
    
    #Constructeur 
    def __init__(self, compagnie, df_airline, df_fleet, df):
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
            # Pourcentage d'occupation sur l'année 2010, on supprime le symbole %
            self.load_factor = float(self.df_airline.loc[0,'LoadFactor'][:-1])
            # Nombre total de passager sur l'année 2010
            self.total_passenger = self.df_airline.loc[0,'TotalPassenger']

            # Nombre d'heure de vol de la flotte sur l'année 
            self.total_hours = self.df_fleet['TotalHours'].sum()
            # Flotte de la compagnie [Avion,Passenger ou Freighter, Pourcentage d'utilisation sur le temps total]
            self.flotte = [self.df_fleet.loc[:, 'Name'],self.df_fleet.loc[:, 'Type'],(self.df_fleet.loc[:, 'TotalHours']/self.total_hours),self.df_fleet.loc[:,'Days']] 
            # CO2 total émis par la compagnie (vol avec passager, vol cargo et cumulé)
            self.CO2_vol_passager, self.CO2_vol_cargo = self.CO2_total_compagnie(df)
            self.CO2_compagnie_total = self.CO2_vol_passager+self.CO2_vol_cargo
            # CO2 émis par passager (réel = en prenant en compte le taux d'occupation des avions, optimal = remplissage 100%)
            self.CO2_par_passager_reel, self.CO2_par_passager_optimal = self.CO2_total_par_passager()

        except KeyError:
            # Met fin au code si le nom saisie n'est pas dans la base de donnée
            print("Le nom de la compagnie saisi n'est pas dans notre base de donnée ou est mal orthographié")
            exit()
            
    #Méthodes
    def CO2_total_compagnie(self,df): 
        CO2_total_cargo = 0 
        CO2_total_passager = 0 
        for i in range(0,len(self.flotte[0])) :
            modele_avion = Aircraft.Aircraft(self.flotte[0][i], df)
            if self.flotte[1][i] == 'Passenger': 
                #On fait l'hypothèse qu'un avion fait un cycle LTO une fois par jour
                CO2_total_passager += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_total_passager += modele_avion.consommation_moteur_cruise*3600*self.flotte[3][i]
            elif self.flotte[1][i] == 'Freighter':
                #On fait l'hypothèse qu'un avion fait un cycle LTO une fois par jour
                CO2_total_cargo += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_total_cargo += modele_avion.consommation_moteur_cruise*3600*self.flotte[3][i]
            
        return CO2_total_passager, CO2_total_cargo
    
    def CO2_total_par_passager(self) : 
        
        CO2_par_passager_optimal = self.CO2_vol_passager*((self.load_factor)/100) / int(self.total_passenger)
        CO2_par_passager_reel = self.CO2_vol_passager  / self.total_passenger
        return CO2_par_passager_reel, CO2_par_passager_optimal
    
    def Repartition_Emission_Type_Vol(self):
        plt.pie([self.CO2_vol_cargo,self.CO2_vol_passager],labels=['Cargo','Passenger'])
        plt.title(f'Répartition des émission de CO2 de la compagnie {self.compagnie}')
        plt.legend()
        plt.show() 
         
    
            
            
def Comparaison_Pollution_Compagnie(df_airline,df,df_fleet):
    pollution_reelle = [] 
    pollution_optimale = []
    for nom_compagnie in df_airline['Airline']:
        compagnie =Airline(nom_compagnie, df_airline, df_fleet, df)
        pollution_reelle.append(compagnie.CO2_par_passager_reel/1000) #EN KG
        pollution_optimale.append(compagnie.CO2_par_passager_optimal/1000) #EN KG
    
    #Paramètre du graphique pour redimensionner les barres et permettre de faire deux graphiques en un 
    bar_width = 0.35
    bar_reel_position = np.arange(len(df_airline['Airline']))
    bar_optimal_position = bar_reel_position+bar_width+0.02
    
    fig, ax = plt.subplots()
    #Graphe de la pollution réelle par passagers
    ax.barh(bar_reel_position, pollution_reelle, height=bar_width, color = 'orange',label='Emissions réelles')
    #Graphe de la pollution optimale (si avions pleins)
    ax.barh(bar_optimal_position, pollution_optimale, height=bar_width, color = 'green', label='Emissions optimales')
    #Rennomage des axes, titres
    ax.set_xlabel('Equivalent CO2 émis par passager (en kg)')
    ax.set_ylabel('Compagnies Aériennes')
    ax.set_title('Emission de CO2/passagers des compagnies britanniques en 2010')
    #Affichage et dimensionnement du nom des compagnies 
    ax.set_yticks(bar_reel_position + bar_width / 2)
    ax.set_yticklabels(df_airline['Airline'])
    ax.tick_params(axis='y', labelsize=8)
    ax.legend()
    plt.show()
    
    
    
        
    
