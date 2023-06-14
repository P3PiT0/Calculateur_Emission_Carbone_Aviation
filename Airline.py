class Airline(): 
    '''
    Docstring
    '''
    
    #Attribut
    
    #Constructeur 
    def __init__(self, nom, df_airline, df_fleet):
        '''
        Constructeur pour initialisation des compagnies aériennes

        :param nom: Nom de la compagnie
        :type nom: string
        :param df_airline: Dataframe contenant les informations sur les compagnies
        :type constructeur: Pandas Dataframe
        '''
        try:
            print(df_fleet)
            self.nom = nom

            # Selectionne et retourne la ligne de notre dataframe contenant le modèle de notre moteur avec ses informations
            self.df_airline = df_airline.loc[df_airline['Airline'] == nom]
            self.df_fleet = df_fleet.loc[df_fleet['Airline'] == nom]
            # On réinitialise l'index à 1
            self.df_airline.reset_index(drop=True, inplace=True)
            # le pourcentage d'occupation

            self.loadfactor = self.df_airline.loc[0, 'Loadfactor']

            self.totalpassenger = self.df_airline.loc[0, 'totalpassenger']

            self.plane = self.defplane()

        except KeyError:
            # Met fin au code si le nom saisie n'est pas dans la base de donnée
            print("Le nom de la compagnie saisi n'est pas dans notre base de donnée ou est mal orthographié")
            exit()
    #Méthodes

    def defplane(self):

        planes = self.df_fleet
        print(planes)
        return planes