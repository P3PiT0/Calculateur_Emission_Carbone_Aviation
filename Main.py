
import Modules
#Formatage des dataframe
#Dataframe contenant les émissions des moteurs
df = Modules.Emission_Data_Reader()
#Dataframe contenant les statistiques des compagnies aériennes
df_airline = Modules.Airline_Data_Reader()
#Dataframe contenant les informations sur les flottes des différentes compagnies 
df_fleet = Modules.Utilization_Data_Reader()

#fonction d'interface utilisateur, elle lit le yaml et demande à l'utilisateur de valider ses données
def interface_utilisateur():
    Entrees_yaml = Modules.lecteuryamel()
    Donnees_dict = Entrees_yaml.print_content()
    if input("\n Validez-vous ces données ? (OUI/NON)") == 'OUI':
        return Donnees_dict
    else:
        print("\n Veuillez remplir le fichier 'Donnees.yaml' comme vous le souhaiter et réessayer")
        #Sorti de la boucle recursive lorsque l'utilisateur valide le yaml
        return interface_utilisateur()


print('\n BIENVENUE, voici un programme de responsabilité écologique et sociale du voyageur aéronautique ')
print("\n Il vous permet de comparer l'impact écologique global par passager des différentes compagnies anglaises")
print("\n Si vous prévoyez un voyage en avion, vous pouvez également comparer l'impact écologique de différents vols")
print("\n Premièrement, veuillez remplir le fichier 'Donnees.yaml' afin de communiquer les entrées au programme.")
print("\n Le fichier se retrouve dans le dossier 'Modules', puis dans le dossier 'InterfaceYamel'.")
print(input("\n Une fois le fichier 'Donnees.yaml' bien remplis, appuyez sur la touche ENTRER de votre clavier"))
Donnees_dict = interface_utilisateur()

#COMPARAISON DES COMPAGNIES DE NOTRE BASE DE DONNEE 
if Donnees_dict['comparaison_compagnies']:
    print('\n\nMENU COMPARAISON DES COMPAGNIES')
    print('Voici un diagramme barre de comparaison des émissions de CO2/passager des différentes compagnies aériennes britanniques')
    Modules.Comparaison_Emission_Compagnie(df_airline, df, df_fleet,'Passenger')
    print('Voici un diagramme barre de comparaison des émissions totales des différentes compagnies aériennes britanniques')
    Modules.Comparaison_Emission_Compagnie(df_airline, df, df_fleet,'Global')
    print('Voici un diagramme barre de comparaison des émissions liées au transport de marchandises des différentes compagnies aériennes britanniques')
    Modules.Comparaison_Emission_Compagnie(df_airline, df, df_fleet,'Freighter')
    

#ANALYSE D'UNE COMPAGNIE SELECTIONNEE 
if Donnees_dict['analyse_compagnie_particuliere']:
    print('\n\nMENU ANALYSE DE COMPAGNIE')
    print(f"Voici une analyse plus précise de la compagnie {Donnees_dict['compagnie_particuliere']}")
    compagnie = Modules.Airline(Donnees_dict['compagnie_particuliere'], df_airline, df_fleet, df)
    print(f"Pollution compagnie : {round(compagnie.CO2_compagnie_total/1000000,3)} tonnes de CO2 en 2010")
    compagnie_segment_passager = Modules.AirlinePassenger(Donnees_dict['compagnie_particuliere'], df_airline, df_fleet, df)
    print(f"Pollution compagnie liée au transport de passagers : {round(compagnie_segment_passager.CO2_vol_passager/1000000,3)} tonnes de CO2 en 2010")
    print(f"Pollution compagnie / passager reel : {round(compagnie_segment_passager.CO2_par_passager_reel/1000,3)} kg de CO2 par personne")
    print(f"Pollution compagnie / passager optimal : {round(compagnie_segment_passager.CO2_par_passager_optimal/1000,3)} kg de CO2 par personne")
    compagnie_segment_cargo = Modules.AirlineFreighter(Donnees_dict['compagnie_particuliere'], df_airline, df_fleet, df)
    print(f"Pollution compagnie liée au transport de marchandises : {round(compagnie_segment_cargo.CO2_vol_cargo/1000000,3)} tonnes de CO2 en 2010")
    print(f"Voici un diagramme montrant la répartition des émissions de CO2 de la compagnie {Donnees_dict['compagnie_particuliere']} en fonction du type de vol effectué")
    compagnie.Repartition_Emission_Type_Vol(df)
    print("Voici un diagramme montrant la part d'utilisation des modèles d'avions de la flotte")
    compagnie.Repartition_Utilisation_Flotte()
    
#COMPARAISON DE DIFFERENTS VOLS
if Donnees_dict['comparaison_VOLS']:
    print('\n\nMENU COMPARAISON DE VOLS')
    print('Voici la comparaison des émissions de CO2 de deux vols')
    #Création de nos objets voyages et compagnies (seulement leur section "passager")
    voyage1 = Modules.Travel(Donnees_dict['arrive_airport1'], Donnees_dict['depart_airport1'], Donnees_dict['avion1'])
    voyage2 = Modules.Travel(Donnees_dict['arrive_airport2'], Donnees_dict['depart_airport2'], Donnees_dict['avion2'])
    compagnie_travel1 = Modules.AirlinePassenger(Donnees_dict['compagnie_travel1'], df_airline, df_fleet, df)
    compagnie_travel2 = Modules.AirlinePassenger(Donnees_dict['compagnie_travel2'], df_airline, df_fleet, df)
    
    #Trajet 1
    print(f"\nTrajet1 : {Donnees_dict['depart_airport1']}->{Donnees_dict['arrive_airport1']} à bord d'un {Donnees_dict['avion1']} opéré par la compagnie {Donnees_dict['compagnie_travel1']}")
    print(f"Pollution du trajet1 : {round(voyage1.pollution_trajet(),3)} tonnes de CO2")
    #ici, on prend en compte le nombre de places dans l'avion et le taux de remplissage des avions de la compagnie pour calculer la pollution par passager
    print(f"Pollution par passager en tenant compte de la compagnie: {round(voyage1.pollution_trajet()/(voyage1.aircraft.nombre_passager*compagnie_travel1.load_factor/100),3)} tonnes de CO2 par passager")
    #sans tenir compte de la compagnie 
    print(f"Pollution par passager sans tenir compte de la compagnie: {round(voyage1.pollution_trajet()/(voyage1.aircraft.nombre_passager),3)} tonnes de CO2 par passager")
    
    #Trajet 2
    print(f"\nTrajet2 : {Donnees_dict['depart_airport2']}->{Donnees_dict['arrive_airport2']} à bord d'un {Donnees_dict['avion2']} opéré par la compagnie {Donnees_dict['compagnie_travel2']}")
    print(f"Pollution du trajet2 : {round(voyage2.pollution_trajet(),3)} tonnes de CO2")
    #ici, on prend en compte le nombre de places dans l'avion et le taux de remplissage des avions de la compagnie pour calculer la pollution par passager
    print(f"Pollution par passager : {round(voyage2.pollution_trajet()/(voyage2.aircraft.nombre_passager*compagnie_travel2.load_factor/100),3)} tonnes de CO2 par passager")
    #sans tenir compte de la compagnie 
    print(f"Pollution par passager sans tenir compte de la compagnie: {round(voyage2.pollution_trajet()/(voyage2.aircraft.nombre_passager),3)} tonnes de CO2 par passager")

#AUCUNE FONCTIONNALITE SELECTIONNEE 
if (not Donnees_dict['comparaison_VOLS']) and (not Donnees_dict['comparaison_compagnies']) and (not Donnees_dict['analyse_compagnie_particuliere']):
    print("Veillez vous rendre sur le fichier 'Donnes.yaml' et y rentrer les donnees souhaitées")


