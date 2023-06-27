from . import Aircraft
import matplotlib.pyplot as plt
import numpy as np
class Airline(): 
    '''
    Docstring
    '''
    #Constructeur 
    def __init__(self, compagnie, df_airline, df_fleet, df):
        '''
        Constructeur pour initialisation des compagnies aériennes

        :param nom: Nom de la compagnie
        :type nom: string
        :param df_airline: Dataframe contenant les informations sur les compagnies
        :type constructeur: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les compagnies
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
        '''
        Renvoi les quantités de CO2 émises par la compagnie en différenciant les avions de transport cargo et 
        les avions de transport de passagers. 
        Pour cela, on se réfère au nombre de jour de vol  en considérant qu'un jour égal à une phase LTO. 
        De plus, on utilise le nombre d'heure de vol pour la phase de croisière : 
        
        CO2 du cycle LTO = CO2 pour 1 cycle * Nombre de jours de vol (tout avions)
        CO2 du cycle Croisière = Taux pollution * Heures totales de vol (tout avions) converties en seconde  
        
        :param df: Dataframe contenant les informations sur les consommations des moteurs
        :type df: Pandas Dataframe
        :return: Masse de CO2 rejeté par la compagnie en gramme pour la branche cargo et pour la branche passager.
        :rtype: float
        '''
        CO2_total_cargo = 0 
        CO2_total_passager = 0 
        for i in range(0,len(self.flotte[0])) :
            modele_avion = Aircraft(self.flotte[0][i], df)
            #Si l'avion transporte des passagers
            if self.flotte[1][i] == 'Passenger': 
                #On fait l'hypothèse qu'un avion fait un cycle LTO une fois par jour
                CO2_total_passager += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_total_passager += modele_avion.consommation_moteur_cruise*3600*self.flotte[2][i]*self.total_hours
            #Si l'avion est un transport Cargo
            elif self.flotte[1][i] == 'Freighter':
                #On fait l'hypothèse qu'un avion fait un cycle LTO une fois par jour
                CO2_total_cargo += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_total_cargo += modele_avion.consommation_moteur_cruise*3600*self.flotte[2][i]*self.total_hours
        return CO2_total_passager, CO2_total_cargo
    
    def Repartition_Utilisation_Flotte(self):
        '''
        Affiche un graphique de type pie chart illustrant l'utilisation de chaque modèle d'avion par rapport
        au temps de vol total de la compagnie.
        ''' 
        plt.pie(self.flotte[2],labels=self.flotte[0])
        plt.title(f'Répartition du temps de vol de la flotte de la compagnie {self.compagnie}')
        plt.legend(fontsize='small')
        plt.show()
                  
    def CO2_total_par_passager(self) : 
        '''
        Renvoi les quantités de CO2/passagers optimale (en considèrant un taux de remplissage de 100%) et 
        réelle (en prennant en compte le load factor de la compagnie sur l'année 2010). 
        
        :return: Masse de CO2/passagers (optimale et réelle) en gramme/passagers.
        :rtype: float
        '''
        CO2_par_passager_optimal = self.CO2_vol_passager*((self.load_factor)/100) / int(self.total_passenger)
        CO2_par_passager_reel = self.CO2_vol_passager  / self.total_passenger
        return CO2_par_passager_reel, CO2_par_passager_optimal
    
    def Repartition_Emission_Type_Vol(self):
        '''
        Affiche un graphique de type pie chart illustrant la répartition des émissions en CO2 de la 
        compagnie en kg entre le transports de marchandises et de passagers.
        '''
        plt.pie([self.CO2_vol_cargo,self.CO2_vol_passager],labels=['Cargo','Passenger'])
        plt.title(f'Répartition des émission de CO2 de la compagnie {self.compagnie}')
        plt.legend()
        plt.show() 
                    
def Comparaison_Pollution_Compagnie_Passager(df_airline,df,df_fleet):
    '''
        Affiche un graphique de type bar chart horizontal illustrant les émissions en CO2/passagers de 
        chaques compagnies aériennes étudiées. On affiche sur le même graphique et pour chaque compagnie
        la quantité de CO2/passager réelle et la quantité de CO2/passager optimale (en considérant 
        un taux de remplissage de 100%). Les valeurs affichées sont en kg/passagers

        :param df_airline: Dataframe contenant les informations des compagnies aériennes
        :type nom: Pandas Dataframe
        :param df: Dataframe contenant les informations sur les consommations des moteurs
        :type df: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les flottes des compagnies aériennes
        :type df_fleet: Pandas Dataframe
        '''
    pollution_reelle = [] 
    pollution_optimale = []
    #Création d'un objet compagnie pour chaque compagnie de df_Airline 
    for nom_compagnie in df_airline['Airline']:
        compagnie =Airline(nom_compagnie, df_airline, df_fleet, df)
        #Stockage des valeurs (en kg)
        pollution_reelle.append(compagnie.CO2_par_passager_reel/1000)
        pollution_optimale.append(compagnie.CO2_par_passager_optimal/1000) 
    
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

def Comparaison_Pollution_Compagnie(df_airline,df,df_fleet):
    '''
        Affiche un graphique de type bar chart horizontal illustrant les émissions totales de 
        chaques compagnies aériennes étudiées. Les valeurs affichées sont en kg.

        :param df_airline: Dataframe contenant les informations des compagnies aériennes
        :type nom: Pandas Dataframe
        :param df: Dataframe contenant les informations sur les consommations des moteurs
        :type df: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les flottes des compagnies aériennes
        :type df_fleet: Pandas Dataframe
        '''
    pollution_totale = []
    #Création d'un objet compagnie pour chaque compagnie de df_Airline 
    for nom_compagnie in df_airline['Airline']:
        compagnie =Airline(nom_compagnie, df_airline, df_fleet, df)
        #Stockage des valeurs (en kg)
        pollution_totale.append(compagnie.CO2_compagnie_total/1000) 
        
    #Paramètre du graphique pour redimensionner les barres et permettre de faire deux graphiques en un 
    fig, ax = plt.subplots()
    #Graphe de la pollution totale des compagnies
    ax.barh(df_airline['Airline'], pollution_totale, color = 'red',label='Emissions totale')
    #Rennomage des axes, titres
    ax.set_xlabel('Equivalent CO2 total émis (en kg)')
    ax.set_ylabel('Compagnies Aériennes')
    ax.set_title('Emission de CO2 totales de chaques compagnies en 2010')
    #Affichage et dimensionnement du nom des compagnies 
    ax.tick_params(axis='y', labelsize=8)
    ax.legend()
    plt.show()
    
    
    
    
    
        
    

    
    
    
    
        
    
