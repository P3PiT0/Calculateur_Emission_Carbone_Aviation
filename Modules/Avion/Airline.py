# Importation de paquets, bibliothèques et modules
from . import Aircraft
import matplotlib.pyplot as plt
import numpy as np
class Airline(): 
    '''
    Classe représentant une compagnie aérienne composée d'une flotte d'avions. 
    Airline est composé d'un segment 'Transport de passagers' et d'un segment 'Cargo' ou des deux.
    '''
    #Constructeur 
    def __init__(self, compagnie, df_airline, df_fleet, df_engine):
        '''
        Constructeur pour initialisation des compagnies aériennes

        :param compagnie: Nom de la compagnie
        :type compagnie: string
        :param df_airline: Dataframe contenant les informations sur les compagnies
        :type df_airline: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les compagnies
        :type df_fleet: Pandas Dataframe
        :param df_engine: Dataframe contenant les informations sur les emissions des moteurs
        :type df_engine: Pandas Dataframe
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
            # Nombre d'heure de vol de la flotte sur l'année 
            self.total_hours = self.df_fleet['TotalHours'].sum()
            # Flotte de la compagnie [Avion,Passenger ou Freighter, Pourcentage d'utilisation sur le temps total]
            self.flotte = [self.df_fleet.loc[:, 'Name'],self.df_fleet.loc[:, 'Type'],(self.df_fleet.loc[:, 'TotalHours']/self.total_hours),self.df_fleet.loc[:,'Days']] 
            # CO2 total émis par la compagnie (vol avec passager, vol cargo et cumulé)
            self.CO2_compagnie_total = self.CO2_total_compagnie(df_engine,'Global')

        except KeyError:
            # Met fin au code si le nom saisie n'est pas dans la base de donnée
            print("Le nom de la compagnie saisi n'est pas dans notre base de donnée ou est mal orthographié")
            exit()
            
    #Méthodes
    def CO2_total_compagnie(self,df_engine,segment): 
        '''
        Renvoi les quantités de CO2 émises par la compagnie en différenciant les avions de transport cargo et 
        les avions de transport de passagers. 
        Pour cela, on se réfère au nombre de jour de vol  en considérant qu'un jour égal à une phase LTO. 
        De plus, on utilise le nombre d'heure de vol pour la phase de croisière : 
        
        CO2 du cycle LTO = CO2 pour 1 cycle * Nombre de jours de vol (tout avions)
        CO2 du cycle Croisière = Taux pollution * Heures totales de vol (tout avions) converties en seconde  
        
        :param df_engine: Dataframe contenant les informations sur les emissions des moteurs
        :type df_engine: Pandas Dataframe
        :parm segment: 'Freighter' = CO2 de la partie fret, 'Passenger' = CO2 de la partie transport de passager, 'Global' = CO2 total
        :type segment: string
        
        :return: Masse de CO2 rejeté par la compagnie en gramme pour le segment spécifié 
        :rtype: float
        '''
        CO2_segment = 0 
        for i in range(0,len(self.flotte[0])) :
            #On ne différencie pas les avions
            if segment == 'Global' :
                modele_avion = Aircraft(self.flotte[0][i], df_engine)
                CO2_segment += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_segment += modele_avion.consommation_moteur_cruise*3600*self.flotte[2][i]*self.total_hours
            #On souhaite avoir les émissions du segment transport de passager
            elif segment == 'Passenger' and self.flotte[1][i] == 'Passenger':
                modele_avion = Aircraft(self.flotte[0][i], df_engine)
                CO2_segment += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_segment += modele_avion.consommation_moteur_cruise*3600*self.flotte[2][i]*self.total_hours
            #On souhaite avoir les émissions du segment transport de marchandise
            elif segment == 'Freighter' and self.flotte[1][i] == 'Freighter':
                modele_avion = Aircraft(self.flotte[0][i], df_engine)
                CO2_segment += modele_avion.consommation_moteur_LTO*self.flotte[3][i]
                CO2_segment += modele_avion.consommation_moteur_cruise*3600*self.flotte[2][i]*self.total_hours
        return CO2_segment
    
    def Repartition_Utilisation_Flotte(self):
        '''
        Affiche un graphique de type pie chart illustrant l'utilisation de chaque modèle d'avion par rapport
        au temps de vol total de la compagnie.
        ''' 
        plt.pie(self.flotte[2],labels=self.flotte[0])
        plt.title(f'Répartition du temps de vol de la flotte de la compagnie {self.compagnie}')
        plt.legend(fontsize='small')
        plt.show()
    
    def Repartition_Emission_Type_Vol(self, df_engine):
        '''
        Affiche un graphique de type pie chart illustrant la répartition des émissions en CO2 de la 
        compagnie en kilogramme (kg) entre le transports de marchandises et de passagers.
        
        :param df_engine: Dataframe contenant les informations sur les emissions des moteurs
        :type df_engine: Pandas Dataframe
        '''
        #Creation des différents segments de la compagnie : Cargo et Passenger
        segment_cargo = AirlineFreighter(self.compagnie, self.df_airline, self.df_fleet, df_engine)
        segment_passenger = AirlinePassenger(self.compagnie, self.df_airline, self.df_fleet, df_engine) 
        plt.pie([segment_cargo.CO2_vol_cargo,segment_passenger.CO2_vol_passager],labels=['Cargo','Passenger'])
        plt.title(f'Répartition des émission de CO2 de la compagnie {self.compagnie} par segment')
        plt.legend()
        plt.show() 
              
class AirlineFreighter(Airline):
    '''
    Classe représentant le segment 'Cargo' ou 'Transport de marchandise' d'une compagnie aérienne.
    Cette classe hérite de la classe Airline.
    '''
    def __init__(self, compagnie, df_airline, df_fleet, df_engine):
        '''
        Constructeur pour initialisation de la branche cargo d'une compagnie aérienne. 

        :param compagnie: Nom de la compagnie
        :type compagnie: string
        :param df_airline: Dataframe contenant les informations sur les compagnies
        :type df_airline: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les compagnies
        :type df_fleet: Pandas Dataframe
        :param df_engine: Dataframe contenant les informations sur les emissions des moteurs
        :type df_engine: Pandas Dataframe
        '''
        #Appel au constructeur de Airline
        super().__init__(compagnie, df_airline, df_fleet, df_engine)
        #Emission de CO2 lié au transport de marchandises
        self.CO2_vol_cargo = super().CO2_total_compagnie(df_engine,'Freighter')
        
class AirlinePassenger(Airline):
    '''
    Classe représentant le segment 'Transport de passagers' ou 'Avion de ligne' d'une compagnie aérienne.
    Cette classe hérite de la classe Airline.
    '''
    def __init__(self, compagnie, df_airline, df_fleet, df_engine):
        '''
        Constructeur pour initialisation de la branche passager d'une compagnie aérienne. 

        :param compagnie: Nom de la compagnie
        :type compagnie: string
        :param df_airline: Dataframe contenant les informations sur les compagnies
        :type df_airline: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les compagnies
        :type df_fleet: Pandas Dataframe
        :param df_engine: Dataframe contenant les informations sur les emissions des moteurs
        :type df_engine: Pandas Dataframe
        '''
        #Appel au constructeur de Airline
        super().__init__(compagnie, df_airline, df_fleet, df_engine)
        # Pourcentage d'occupation sur l'année 2010, on supprime le symbole %
        self.load_factor = float(self.df_airline.loc[0,'LoadFactor'][:-1])
        # Nombre total de passager sur l'année 2010
        self.total_passenger = self.df_airline.loc[0,'TotalPassenger']
        # Emission de CO2 lié au transport de passagers
        self.CO2_vol_passager = super().CO2_total_compagnie(df_engine,'Passenger')
        # CO2 émis par passager (réel = en prenant en compte le taux d'occupation des avions, optimal = remplissage 100%)
        self.CO2_par_passager_reel, self.CO2_par_passager_optimal = self.CO2_total_par_passager()
    
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
    
def Comparaison_Emission_Compagnie(df_airline,df_engine,df_fleet,segment):
    '''
        Affiche un graphique de type bar chart horizontal illustrant les émissions en CO2 des différents
        segments des compagnies. 
        
        Dans le cas ou segment = 'Passenger', on affiche sur le même graphique et pour chaque compagnie
        la quantité de CO2/passager réelle et la quantité de CO2/passager optimale (en considérant 
        un taux de remplissage de 100%). Les valeurs affichées sont en kg/passagers
        
        Dans le cas ou segment = 'Global', on affiche un graphique contenant les émissions totales de 
        chaques compagnies aériennes étudiées. Les valeurs affichées sont en kg. 
        A noter que l'on prends en compte seulement les compagnies possédant au moins un segment passager.
        
        Dans le cas ou segment = 'Freighter', on affiche un graphique contenant les émissions des compagnies 
        liées au transport de marchandises. Les valeurs affichées sont en kg

        :param df_airline: Dataframe contenant les informations des compagnies aériennes
        :type nom: Pandas Dataframe
        :param df_engine: Dataframe contenant les informations sur les emissions des moteurs
        :type df_engine: Pandas Dataframe
        :param df_fleet: Dataframe contenant les informations sur les flottes des compagnies aériennes
        :type df_fleet: Pandas Dataframe
        :param segment: Emission totale de la compagnie ='Global', Cargo uniquement = 'Freighter', Passagers uniquement = "Passenger")
        :type segment: string
        '''
    if segment == 'Global' : 
        emission_totale = []
        #Création d'un objet compagnie pour chaque compagnie de df_Airline 
        for nom_compagnie in df_airline['Airline']:
            compagnie =Airline(nom_compagnie, df_airline, df_fleet, df_engine)
            #Stockage des valeurs (en kg)
            emission_totale.append(compagnie.CO2_compagnie_total/1000) 
            
        #Paramètre du graphique pour redimensionner les barres et permettre de faire deux graphiques en un 
        fig, ax = plt.subplots()
        #Graphe de la emission totale des compagnies
        ax.barh(df_airline['Airline'], emission_totale, color = 'red',label='Emissions totale')
        #Rennomage des axes, titres
        ax.set_xlabel('Equivalent CO2 total émis (en kg)')
        ax.set_ylabel('Compagnies Aériennes')
        ax.set_title("Emission de CO2 totales de chaques compagnies possédant au moins un segment 'Passager'' en 2010")
        #Affichage et dimensionnement du nom des compagnies 
        ax.tick_params(axis='y', labelsize=8)
        ax.legend()
        plt.show()
        
    elif segment == 'Passenger': 
        emission_reelle = [] 
        emission_optimale = []
        #Création d'un objet AirlinePassenger pour chaque compagnie de df_Airline 
        for nom_compagnie in df_airline['Airline']:
            compagnie =AirlinePassenger(nom_compagnie, df_airline, df_fleet, df_engine)
            #Stockage des valeurs (en kg)
            emission_reelle.append(compagnie.CO2_par_passager_reel/1000)
            emission_optimale.append(compagnie.CO2_par_passager_optimal/1000) 
        
        #Paramètre du graphique pour redimensionner les barres et permettre de faire deux graphiques en un 
        bar_width = 0.35
        bar_reel_position = np.arange(len(df_airline['Airline']))
        bar_optimal_position = bar_reel_position+bar_width+0.02
        
        fig, ax = plt.subplots()
        #Graphe de la pollution réelle par passagers
        ax.barh(bar_reel_position, emission_reelle, height=bar_width, color = 'orange',label='Emissions réelles')
        #Graphe de la pollution optimale (si avions pleins)
        ax.barh(bar_optimal_position, emission_optimale, height=bar_width, color = 'green', label='Emissions optimales')
        #Rennomage des axes, titres
        ax.set_xlabel('Equivalent CO2 émis par passager (en kg)')
        ax.set_ylabel('Compagnies Aériennes')
        ax.set_title("Emission de CO2/passagers des compagnies britanniques possédant un segment 'Passager' en 2010")
        #Affichage et dimensionnement du nom des compagnies 
        ax.set_yticks(bar_reel_position + bar_width / 2)
        ax.set_yticklabels(df_airline['Airline'])
        #Affichage et dimensionnement du nom des compagnies 
        ax.tick_params(axis='y', labelsize=8)
        ax.legend()
        plt.show()
    
    elif segment == 'Freighter': 
        emission_cargo = []
        liste_compagnie_cargo = []
        #Création d'un objet AirlineFreighter pour chaque compagnie de df_Fleet car les compagnies CARGO ne sont pas référencés dans df_Airline 
        for nom_compagnie in df_fleet['Airline'].unique():
            compagnie =AirlineFreighter(nom_compagnie, df_airline, df_fleet, df_engine)
            #Stockage des emissions (en kg), et du nom des companies possédant des avions cargos
            if compagnie.CO2_vol_cargo != 0 :  
                emission_cargo.append(compagnie.CO2_vol_cargo/1000)
                liste_compagnie_cargo.append(nom_compagnie)
            
        #Paramètre du graphique pour redimensionner les barres et permettre de faire deux graphiques en un 
        fig, ax = plt.subplots()
        #Graphe de la emission totale des compagnies
        ax.barh(liste_compagnie_cargo, emission_cargo, color = 'red',label='Emissions Cargo')
        #Rennomage des axes, titres
        ax.set_xlabel('Equivalent CO2 total émis (en kg)')
        ax.set_ylabel('Compagnies Aériennes')
        ax.set_title("Emission de CO2 des vols cargo de chaques compagnies possédant un segment 'Cargo' en 2010")
        #Affichage et dimensionnement du nom des compagnies 
        ax.tick_params(axis='y', labelsize=8)
        ax.legend()
        plt.show()
    else :
        print("Erreur: Argument 'segment' dans l'affichage des graphes comparatif de compagnies")
        exit()