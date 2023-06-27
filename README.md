# Calculateur_Emission_Carbone_Aviation
 Ce dépôt GitHub à pour but de proposer un outil développé en Python permettant de sélectionner un vol aérien en 
 fonction des émissions de carbones engendrés par la compagnie aérienne, l'avion choisie et les destinations de départ 
 et d'arrivée choisie.

 Ce projet a été développé sous forme d'application pouvant être facilement installée et désintallée de l'ordinateur du client.

## Contenu du dépôt 
Le dépôt est composé de XX dossiers et fichiers distinct :
1. build :
2. Data
3. Documentation (À effacer?)
4. Modules : Contient tous les packages, modules et scritps python nécessaires à l'utilisation et l'exécution du code
5. source
6. LICENSE.md : Contient la license utilisé pour ce projet, ainsi que toutes les autorisations et limitations engendrées 
avec l'usage de cette application.
7. Main.py : Script Python à éxécuter permettant de faire fonctionner l'application
8. README.md : Fichier contenant des informations générales sur l'application, les étapes d'installation et 
les instructions d'opération
9. requirements.txt : Fichier texte permettant l'utilisateur d'identifier et installer tous les modules nécessaires à l'application
10. setup.cfg : Fichier utiliser pour l'installation et l'initialisation de l'application
11. setup.py : Fichier utiliser pour l'installation et l'initialisation de l'application


Le code commence par l'importation du module "Aircraft" depuis un module local, ainsi que des modules "matplotlib.pyplot" et "numpy".

## Modules, classes et méthodes utilisées:
Tous les modules employés dans cette application ce retrouvent dans le dossier "Modules". Les modules sont regroupés dans des sous-dossiers.
Chacuns de ces sous-dossiers contient un script '__init__' qui est la méthode constructeur pour créé la classe. Le dossier principal 'Modules' contient lui aussi un script "__init__" qui importe les 3 modules créés.
### 1. Module Avion
### 1.1. Classe Aircraft
La classe "Aircraft" représente un avion. Voici un résumé des principales fonctionnalités du code :


La classe "Aircraft" est définie avec un constructeur "init" qui initialise les attributs spécifiques à un avion, tels que le modèle de moteur associé à l'avion, le nombre de moteurs, la vitesse de croisière, le nombre de places passager, l'altitude de croisière, et la consommation de carburant de l'avion pendant les phases LTO (décollage, atterrissage et montée) et de croisière.

La classe contient plusieurs méthodes pour effectuer des calculs liés à l'avion, notamment la consommation de carburant de l'avion pendant les phases LTO et de croisière, et la vitesse de croisière de l'avion.

La méthode "Consommation_Avion" calcule la masse de CO2 émise pendant la phase de croisière de l'avion en utilisant la consommation des moteurs associés à l'avion et en multipliant par le nombre de moteurs. Elle retourne la masse de CO2 émise pendant la phase LTO et le taux d'émission de CO2 pendant la phase de croisière.

La méthode "Vitesse_croisière" calcule la vitesse de croisière de l'avion en utilisant le modèle de l'avion et le nombre de mach de croisière. Elle crée un objet "Atmosphere" pour obtenir les données atmosphériques à l'altitude de croisière de l'avion, puis calcule la vitesse de croisière en utilisant la vitesse du son à cette altitude et le nombre de mach de croisière.

En résumé, le code définit une classe "Aircraft" avec des méthodes pour effectuer des calculs liés aux informations de l'avion, notamment la consommation de carburant et la vitesse de croisière, en utilisant les données spécifiques de l'avion et les données du moteur associé.

### 1.2. Classe Airline
Cette classe représente une compagnie aérienne et contient plusieurs méthodes pour analyser les données de la compagnie.

Le constructeur de la classe "Airline" prend en paramètres le nom de la compagnie, ainsi que trois DataFrames 
("df_airline", "df_fleet" et "df") contenant des informations sur les compagnies aériennes, les flottes et les 
consommations des moteurs respectivement.

La méthode "init" initialise les attributs de la classe en récupérant les informations spécifiques à la compagnie à 
partir des DataFrames fournis en entrés. Elle extrait les informations sur la compagnie, la flotte, le facteur de charge,
le nombre total de passagers, le nombre total d'heures de vol, la répartition de la flotte et calcule les émissions 
totales de CO2 de la compagnie.

La méthode "CO2_total_compagnie" calcule les quantités de CO2 émises par la compagnie, en distinguant les avions de 
transport cargo et les avions de transport de passagers. Elle utilise les informations sur la consommation des moteurs 
pour calculer les émissions de CO2 pour les phases de LTO (Takeoff and Landing Cycle) et de croisière. Les émissions sont 
calculées en fonction du nombre de jours de vol et du nombre d'heures de vol total de la flotte.

La méthode "Repartition_Utilisation_Flotte" affiche un graphique en secteurs (pie chart) illustrant la répartition de l'utilisation de chaque modèle d'avion par rapport au temps de vol total de la compagnie.

La méthode "CO2_total_par_passager" calcule les quantités de CO2 émises par passager, à la fois de manière réelle (en prenant en compte le facteur de charge) et optimale (en considérant un taux de remplissage de 100%). Les émissions sont calculées en fonction des émissions totales de CO2 de la compagnie et du nombre total de passagers.

La méthode "Repartition_Emission_Type_Vol" affiche un graphique en secteurs (pie chart) illustrant la répartition des émissions de CO2 de la compagnie entre le transport de marchandises et le transport de passagers.

La fonction "Comparaison_Pollution_Compagnie_Passager" prend en paramètres les DataFrames contenant les informations sur les compagnies aériennes, les consommations des moteurs et les flottes. Elle crée des objets "Airline" pour chaque compagnie aérienne et affiche un graphique en barres (bar chart) horizontal comparant les émissions de CO2 par passager réelles et optimales pour chaque compagnie.

La fonction "Comparaison_Pollution_Compagnie" fait la même chose que la fonction précédente, mais elle compare les émissions totales de CO2 de chaque compagnie.

Ces méthodes et fonctions permettent d'analyser les émissions de CO2 des compagnies aériennes et de visualiser les données à l'aide de graphiques.

### 1.3. Classe Moteur
La classe 'Moteur' est établie dans le module 'Engine'. Elle représente un moteur d'avion. Voici un résumé des principales fonctionnalités du code :

Le code commence par importer le module pandas sous l'alias "pd".

Ensuite, la classe "Moteur" est définie avec un constructeur "init" qui initialise les attributs spécifiques à un moteur d'avion, tels que le modèle du moteur et les données du moteur à partir d'un DataFrame global.

La classe contient plusieurs méthodes pour effectuer des calculs liés aux émissions de CO2 du moteur et aux conversions de gaz en équivalents de CO2.

La méthode "Conversion_Equivalent_Carbone" prend en paramètre les taux de différents gaz (HC, CO, NOx) et retourne une liste des taux équivalents en CO2 en fonction de leur potentiel de réchauffement global (PRG) sur 100 ans.

La méthode "Equivalent_Carbone_LTO" calcule la masse de CO2 émise pendant la phase de décollage, d'atterrissage et de montée du moteur (LTO) en utilisant les données spécifiques du moteur et la méthode de conversion en équivalent carbone.

La méthode "Taux_Carbone_Cruise" calcule le taux d'émission de CO2 pendant la phase de croisière du moteur en grammes par kilogramme de kérosène consommé.

La méthode "Equivalent_CarboneParSeconde_Cruise" calcule la masse de CO2 émise par seconde pendant la phase de croisière du moteur en utilisant le taux d'émission de CO2 et la consommation de carburant du moteur.

En résumé, le code définit une classe "Moteur" avec des méthodes pour effectuer des calculs et des conversions liés aux émissions de CO2 d'un moteur d'avion, en se basant sur les données spécifiques du moteur fournies dans un DataFrame.

### 2. Module InterfaceYaml
### 2.1. Classe Lecteuryaml
La classe "lecteuryamel" est utilisée pour lire et afficher le contenu d'un fichier YAML. Voici un résumé des principales fonctionnalités du code :

Le code commence par importer le module yaml, qui permet de travailler avec des fichiers YAML.

Ensuite, la classe "lecteuryamel" est définie avec un constructeur "init" qui ouvre le fichier YAML spécifié ("Modules/InterfaceYamel/Donnees.yaml") en mode lecture et charge le contenu du fichier dans l'attribut "content" à l'aide de la fonction "yaml.safe_load".

La classe contient une méthode "print_content" qui affiche le contenu du fichier YAML et le retourne sous la forme d'un dictionnaire. Cette méthode parcourt les clés et les valeurs du contenu chargé, les affiche à l'écran et les stocke dans un dictionnaire "Donnees_dict". Enfin, elle retourne ce dictionnaire à l'utilisateur.

En résumé, le code définit une classe "lecteuryamel" pour lire et afficher le contenu d'un fichier YAML. Il utilise le module yaml pour charger le contenu du fichier et fournit une méthode pour afficher ce contenu et le stocker dans un dictionnaire


### 3. Module Lecture_Calcus_Manipulations
### 3.1. Script Data_Reader
Le code fourni comprend trois fonctions distinctes pour lire et traiter différentes données liées aux émissions d'avions, aux compagnies aériennes et à l'utilisation de la flotte. Voici un résumé des principales fonctionnalités de chaque fonction :

La fonction Emission_Data_Reader lit les données de la banque de données de l'OACI sur les émissions des moteurs d'avion à partir d'un fichier CSV.
Elle sélectionne les colonnes pertinentes et les renomme pour faciliter l'utilisation des données.
Les moteurs hors service sont supprimés du dataframe.
Les duplications basées sur le modèle de moteur sont supprimées, en conservant uniquement la première occurrence.
Les colonnes numériques du dataframe sont converties en type float.
Finalement, le dataframe modifié est retourné.

Fonction Airline_Data_Reader lit les données sur le pourcentage d'occupation des avions pour les compagnies aériennes à partir d'un fichier CSV.
Elle sélectionne les colonnes pertinentes et les renomme.
Le dataframe modifié est retourné.

Fonction Utilization_Data_Reader lit les données sur l'utilisation de la flotte des compagnies aériennes à partir d'un fichier CSV.
Elle sélectionne les colonnes pertinentes et les renomme.
Les colonnes numériques du dataframe sont converties en type float.
Finalement, le dataframe modifié est retourné.

En résumé, les trois fonctions fournissent des mécanismes pour lire et prétraiter différentes données liées aux émissions d'avions, aux compagnies aériennes et à l'utilisation de la flotte

### 3.2. Classe Travel
La classe 'travel' permet de calculer la distance de croisière d'un voyage entre deux aéroports et d'estimer les émissions de CO2 du trajet en utilisant les données sur l'avion et ses moteurs.

Le chargement des données est effectué en utilisant le paquet Pytohn 'airportsdata', afin d'obtenir des informations sur les aéroports, ainsi que la méthode 'Emission_Data_Reader' du module 'Data_Reader' pour lire les données sur les émissions de gaz à effet de serre et stocker ces données dans le dataframe df.

La classe travel contient une fonction d'initialisation __init__ qui initialise les attributs de la classe avec les codes IATA des aéroports d'arrivée et de départ, ainsi qu'un objet Aircraft qui représente l'avion utilisé pour le vol.

La méthode distance_croisiere calcule la distance de croisière du voyage en utilisant les latitudes et longitudes des aéroports. La distance est retournée en kilomètres.

La méthode pollution_trajet calcule et renvoie les émissions de CO2 du trajet en utilisant les données disponibles sur l'avion et ses moteurs. Les émissions sont retournées en tonnes de CO2.

En résumé, le script représente une classe travel qui permet de calculer la distance de croisière d'un voyage entre deux aéroports et d'estimer les émissions de CO2 du trajet en utilisant les données sur l'avion et ses moteurs.

