import pandas as pd
import numpy as np
import airportsdata
import csv

def Emission_Data_Reader (): 
    """Cette fonction lit les donnees de la banque de données de l'OACI sur les émissions des moteurs d'avion 
    qui contient des informations sur les émissions de gaz d'échappement des moteurs d'avion. Par la suite
    ce cette fonction va nettoyer les données pour en faciliter l'analyse par la suite en conservant les colonnes
    désirées et en les renommant.
    
    :return: pandas dataframe
    """
    #Lecture du fichier CSV, selection des colonnes utiles
    df = pd.read_csv('Data/EmissionData.csv',delimiter=';',decimal=',',usecols=(2,3,14,17,28,30,41,43,59,78,81),encoding = 'unicode_escape')

    #On renomme les colonnes pour faciliter l'utilisation des données
    #LTO = donnée pour les phases de décollage, montée et atterrissage 
    #Cruise = donnée pour la phase de croisière
    #HC = Hydrocarbure, CO = Monoxyde de Carbone, NOx = Oxyde d'azote, Fuel = Kérosène
    df.columns = ['Fabricant','Modele','Statut','HC_cruise','HC_LTO','CO_cruise','CO_LTO','NOx_cruise','NOx_LTO','Fuel_cruise','Fuel_LTO']
    #print(f"Noms des colonne : {df.columns}, shape : {df.shape}")

    #Suppression des moteurs dont le statut est "Out of service"
    df = df[df['Statut'] != 'Out of service']

    #Dans le cas où un moteur est présent différente fois, on conserve seulement la première occurence
    df = df.drop_duplicates(subset=['Modele'], keep='first')
    
    #Conversion des colonnes numériques en float
    df[['HC_cruise', 'HC_LTO', 'CO_cruise', 'CO_LTO', 'NOx_cruise', 'NOx_LTO', 'Fuel_cruise','Fuel_LTO']] = df[['HC_cruise', 'HC_LTO', 'CO_cruise', 'CO_LTO', 'NOx_cruise', 'NOx_LTO', 'Fuel_cruise','Fuel_LTO']].astype(float)
    
    
    #Retourne le dataframe (contenant les données moteur) modifié et prêt à être exploité
    return df

'''
def Airport_Data_Reader():
    """Cette fonction lit les données du module airportsdata et récupère la latitude et la longitude et 
    le code iata des aeroports anglais. Par la suite on va renvoyer ce dictionnaire contenant la latitude,
    la longitude, le code iata et d'autres informations pour chaque aéroports anglais. 
    
    :return: dictionnaire
    """
    #Chargement des informations
    airports = airportsdata.load('IATA')
    airports_df = pd.DataFrame(airports)
    airports_df = airports_df.transpose()
    #Sélection des aeroports britanniques
    airports_gb_df = airports_df[airports_df.subd == 'England'].reset_index(drop=True)
    #Création du dictionnaire, l'index de notre dictionnaire correspond à l'indice iata
    airports_gb_df.index = airports_gb_df['iata']
    airports_gb = airports_gb_df.transpose().to_dict()
            
    return airports_gb
'''



def Airline_Data_Reader():
    """Cette fonction lit les données concernant le pourcentage d'occupation des avions pour les compagnies
    aeriennes étudiées.

    :return: pandas dataframe
    """
    # Lecture du fichier CSV, selection des colonnes utiles
    df = pd.read_csv('Data/AirCarrierData.csv', delimiter=';', decimal=',',
                     usecols=(1, 7, 9), encoding='unicode_escape')

    # On renomme les colonnes pour faciliter l'utilisation des données
    # Airline = nom des compagnies
    # Loadfactor = pourcentage d'occupation des vols
    # TotalPassenger = nombre total de passagers transportés
    df.columns = ['Airline', 'TotalPassenger', 'LoadFactor']

    # Retourne le dataframe (contenant les données moteur) modifié et prêt à être exploité
    return df

def Utilization_Data_Reader():
    """Cette fonction lit les donnees concernant les avions composant la flotte des compagnies
    aeriennes étudiées.

    :return: pandas dataframe
    """
    # Lecture du fichier CSV, selection des colonnes utiles
    df = pd.read_csv('Data/FleetUtilizationData.csv', delimiter=';', decimal=',',usecols=(0, 1, 2, 3, 4), encoding='unicode_escape')

    # On renomme les colonnes pour faciliter l'utilisation des données
    # Airline = nom des compagnies
    # Loadfactor = pourcentage d'occupation des vols
    df.columns = ['Airline', 'Name', 'Type','Days','TotalHours']
    # print(f"Noms des colonne : {df.columns}, shape : {df.shape}")

    # Conversion des colonnes numériques en float
    df[['Days','TotalHours']] = df[['Days','TotalHours']].astype(float)


    # Retourne le dataframe (contenant les données moteur) modifié et prêt à être exploité
    return df
