# Calculateur_Emission_Carbone_Aviation
 Cette application a pour but de proposer un outil développé en Python permettant de calculer l'émpreinte carbone de différentes compagnies aériennes ou les émissions d'un avions sur un trajet entre deux aéroports choisis.

 Ce projet a été développé sous forme d'application modulable pouvant être facilement installée et désintallée localement. 

## Sommaire 
[1. Contenu du paquet] (#Contenu)



## Contenu du paquet {#Contenu}
Le paquet est composé de 11 dossiers et fichiers distincts :
1. Data : Contient les fichiers .csv
2. Images : Dossier contenant les images
3. Modules : Contient tous les packages, modules et scritps python nécessaires à l'utilisation et l'exécution du code
4. build : Contient les fichiers .html pour la documentation de l'application, généré par Sphinx
5. source: Contient les fichiers nécessaires à la création de la documentation avec Sphinx
6. .gittatributes
7. .gitignore
8. EXEMPLE.md
9. LICENSE.md : Contient la license utilisé pour ce projet, ainsi que toutes les autorisations et limitations engendrées 
avec l'usage de cette application.
10. Main.py : Script Python à éxécuter permettant de faire fonctionner l'application
11. Makefile
12. README.md : Fichier contenant des informations générales sur l'application, les étapes d'installation et 
les instructions d'opération
13. make.bat
14. requirements.txt : Fichier texte permettant l'utilisateur d'identifier et installer tous les modules nécessaires à l'application
15. setup.cfg : Fichier utiliser pour l'installation et l'initialisation de l'application
16. setup.py : Fichier utiliser pour l'installation et l'initialisation de l'application


## Notice d'utilisation
### Installation 
1. Téléchargez le dossier compressé contenant l'application sur votre ordinateur.
2. Extraire le dossier compressé.
3. Sur votre logiciel de préférence supportant Python, ouvrez le dossier principal de l'application.
4. Ouvrez le dossier où se situe le fichier 'setup.py'.
5. Dans le terminal de votre logiciel, exécuter le fichier 'setup.py' à l'aide de la commande: `python setup.py install`.
6. L'application est maintenant prête à être utilisée.
7. Ouvrez une invite de commande ou un terminal et se rendre dans le répertoire de travail ou se trouve le fichier main.py.
8. Exécutez le programme .

### Avant d'exécuter l'application
Avant d'exécuter l'application, assurez-vous d'avoir fait vos sélections dans le fichier 'Données.yaml' situé dans le dossier 'Modules\Interfaceyaml'. Ce fichier regroupe les différents paramètres utilisateurs.

### Exécution de l'application
Pour exécuter l'application, ouvrez et exécutez le fichier 'Main.py'.

### Modification du code par l'utilisateur
La seule modification nécessaire du code fait par l'utilisateur, est la sélection des choix et paramètres dans le fichier 'Données.yaml' situé dans le dossier 'Modules\Interfaceyaml'.

## Modules, classes, méthodes et fonctions utilisées:
Tous les modules employés dans cette application se retrouvent dans le dossier "Modules". Les modules sont regroupés dans des sous-dossiers. A noter que des informations supplémentaires sont disponibles dans la documentation sphinx. 

### 1. Module Avion
#### 1.1. Classe Aircraft
Ce code représente plusieurs classes liées à la modélisation d'avions. Voici une description de chaque classe :

La classe __Aircraft__ représente un avion. Elle possède les attributs suivants :

1. moteur: un objet de la classe Moteur qui représente le moteur associé à l'avion.
2. nombre_moteur: le nombre de moteurs sur l'avion.
3. vitesse_croisiere: la vitesse de croisière de l'avion en mètres par seconde.
4. altitude_croisiere: l'altitude de croisière de l'avion en mètres.
5. consommation_moteur_LTO: la consommation du moteur de l'avion pendant la phase LTO (Landing, Take Off) en grammes.
5. consommation_moteur_cruise: la consommation du moteur de l'avion pendant la phase de croisière en grammes par seconde.

La classe __Aircraft__ possède également deux méthodes :

__Emission_Avion()__: retourne la masse de gaz rejeté en équivalent carbone pendant la phase de croisière de l'avion en grammes par seconde et la masse rejetée pendant la phase LTO en grammes.

__Vitesse_croisière(modele)__: retourne la vitesse de croisière de l'avion en mètres par seconde en fonction de son mach de croisière et de son altitude de croisière.

La classe __Freighter__ représente un avion transportant des marchandises. Elle hérite de la classe Aircraft et ajoute l'attribut 'payload' qui représente la capacité de transport de l'avion en livres.

La classe __Airliner__ représente un avion transportant des passagers. Elle hérite également de la classe Aircraft et ajoute l'attribut 'nombre_passager' qui représente le nombre de places passagers dans l'avion.

Ces classes utilisent un dictionnaire appelé 'correspondance_avions_moteurs' pour récupérer les informations sur les avions et leurs moteurs à partir du modèle de l'avion. De plus, elles utilisent un dataframe 'df_engine' contenant des informations sur tous les moteurs.

Ces classes permettent de modéliser différentes caractéristiques des avions, telles que leur moteur, leur vitesse de croisière, leur altitude de croisière, leur consommation de carburant, leur capacité de transport (pour les avions de fret), et le nombre de places passagers (pour les avions de ligne).

### 1.2. Classe Airline

Ce code est une implémentation d'un modèle de simulation pour analyser les émissions de CO2 des compagnies aériennes. Il utilise des données sur les compagnies aériennes, les flottes d'avions, et les émissions des moteurs.

La classe principale est "__Airline__", qui représente une compagnie aérienne composée d'une flotte d'avions. Elle possède un attribut compagnie pour stocker le nom de la compagnie. Le constructeur de cette classe prend en paramètre les informations sur la compagnie (nom, données sur la compagnie, la flotte, et les émissions des moteurs).

La méthode "__CO2_total_compagnie calcule__" les émissions totales de CO2 de la compagnie en fonction du segment spécifié (global, passager ou cargo). Elle itère sur les avions de la flotte de la compagnie et utilise la classe Aircraft pour obtenir les données de consommation des moteurs et calculer les émissions.

La méthode "__Repartition_Utilisation_Flotte__" affiche un graphique de type "pie chart" qui représente la répartition de l'utilisation de chaque modèle d'avion par rapport au temps de vol total de la compagnie.

La méthode "__Repartition_Emission_Type_Vol__" affiche un graphique de type "pie chart" qui illustre la répartition des émissions de CO2 de la compagnie entre le transport de marchandises et le transport de passagers.

Les classes "__AirlineFreighter__" et "__AirlinePassenger__" héritent de la classe Airline et représentent les segments de cargo et de passagers d'une compagnie aérienne respectivement. Elles utilisent des méthodes spécifiques pour calculer les émissions de CO2 liées à chaque segment.

Enfin, la fonction "__Comparaison_Emission_Compagnie__" utilise les classes Airline, AirlineFreighter et AirlinePassenger pour générer des graphiques de comparaison des émissions de CO2 entre les différentes compagnies aériennes et les segments (global, cargo, passagers).


### 1.3. Classe Moteur

Ce code définit une classe appelée "__Moteur__" qui représente un moteur d'avion et permet de calculer ses émissions de CO2. Voici un résumé du code :

La classe "__Moteur représente__" un moteur d'avion et contient plusieurs méthodes pour effectuer des calculs liés aux émissions de CO2.

Le constructeur __init__ prend deux paramètres : "__modele__" (le modèle du moteur) et "__df_engine__" (un DataFrame contenant les informations de tous les moteurs).
Dans le constructeur, les attributs de l'objet moteur sont initialisés en utilisant les informations du DataFrame df_engine.

La méthode "__Conversion_Equivalent_Carbone__" convertit les taux de différents gaz (HC, CO, NOx) en équivalent CO2 en utilisant les PRG (Potentiel Réchauffement Global) de chaque gaz.

La méthode "__Equivalent_Carbone_LTO__" calcule la masse de CO2 émise pendant la phase LTO (décollage, atterrissage et montée) du moteur.

La méthode "__Taux_Carbone_Cruise__" calcule le taux d'équivalent CO2 rejeté pendant la phase de croisière du moteur (en g/kg de kérosène consommé).

La méthode "__Equivalent_CarboneParSeconde_Cruise__" calcule la masse de CO2 émise par seconde pendant la phase de croisière du moteur (en g/s).

En cas d'erreur (par exemple, si le modèle du moteur n'est pas présent dans le DataFrame), un message d'erreur est affiché et le code s'arrête.
Le code utilise également le module Pandas pour manipuler les données sous forme de DataFrame.

### 2. Module InterfaceYaml
### 2.1. Classe Lecteuryaml
La classe "lecteuryamel" est utilisée pour lire et afficher le contenu d'un fichier YAML. Voici un résumé des principales fonctionnalités du code :

Le code commence par importer le module yaml, qui permet de travailler avec des fichiers YAML.

Ensuite, la classe "lecteuryamel" est définie avec un constructeur "init" qui ouvre le fichier YAML spécifié ("Modules/InterfaceYamel/Donnees.yaml") en mode lecture et charge le contenu du fichier dans l'attribut "content" à l'aide de la fonction "yaml.safe_load".

La classe contient une méthode "print_content" qui affiche le contenu du fichier YAML et le retourne sous la forme d'un dictionnaire. Cette méthode parcourt les clés et les valeurs du contenu chargé, les affiche à l'écran et les stocke dans un dictionnaire "Donnees_dict". Enfin, elle retourne ce dictionnaire à l'utilisateur.

En résumé, le code définit une classe "lecteuryamel" pour lire et afficher le contenu d'un fichier YAML. Il utilise le module yaml pour charger le contenu du fichier et fournit une méthode pour afficher ce contenu et le stocker dans un dictionnaire


### 3. Module Lecture_Calcus_Manipulations
### 3.1. Script Data_Reader
Ce code contient trois fonctions de lecture des données :

La fonction "__Emission_Data_Reader__" lit les données de la banque de données de l'OACI sur les émissions des moteurs d'avion. Elle charge un fichier CSV contenant des informations sur les émissions de gaz d'échappement des moteurs d'avion, nettoie les données en sélectionnant les colonnes pertinentes et en les renommant, supprime les moteurs dont le statut est "Out of service", supprime les doublons basés sur le modèle de moteur, convertit certaines colonnes en type float et retourne un dataframe Pandas contenant les données moteur modifiées et prêtes à être exploitées.

La fonction "__Airline_Data_Reader__" lit les données concernant le pourcentage d'occupation des avions et le nombre de passagers des différentes compagnies aériennes étudiées. Elle charge un fichier CSV contenant ces informations, sélectionne les colonnes pertinentes et les renomme, puis retourne un dataframe Pandas contenant les données modifiées et prêtes à être exploitées.

La fonction "__Utilization_Data_Reader__" lit les données concernant les avions composant la flotte des compagnies aériennes étudiées et les informations sur leur utilisation. Elle charge un fichier CSV contenant ces informations, sélectionne les colonnes pertinentes et les renomme, convertit certaines colonnes en type float, puis retourne un dataframe Pandas contenant les données modifiées et prêtes à être exploitées.

Il y a également un commentaire pour une fonction supplémentaire "__Airport_Data_Reader__" qui n'est pas implémentée dans le code. Cette fonction était destinée à lire les données du module airportsdata et à récupérer les informations sur les aéroports anglais, mais elle est actuellement commentée.

### 3.2. Classe Travel
Ce code définit une classe appelée "__Travel__" qui représente un voyage entre deux aéroports pour un avion donné. Voici un résumé du code :

Le code importe les modules nécessaires, y compris airportsdata, math, Airliner (une classe définie dans un autre module) et Data_Reader (un module contenant une fonction Emission_Data_Reader).
Il charge les données des aéroports et des émissions de gaz à effet de serre à partir de fichiers.
La classe Travel représente un voyage entre deux aéroports pour un avion spécifié.
Le constructeur __init__ prend trois paramètres en entrée : 
1. "__arrivee_airport__" (le code IATA de l'aéroport d'arrivée)
2. "__depart_airport__" (le code IATA de l'aéroport de départ)
3. "__aircraft__" (le modèle de l'avion réalisant le vol)

Dans le constructeur, les attributs de l'objet Travel sont initialisés avec les valeurs passées en paramètre.

La méthode "__distance_croisiere__" calcule la distance de vol en croisière du voyage en utilisant les latitudes et longitudes des aéroports.

La méthode "__pollution_trajet__" calcule et renvoie l'émission de CO2 du trajet en utilisant les données disponibles sur l'avion et ses moteurs. L'émission est renvoyée en tonnes de CO2.

Le code utilise également des fonctions et des constantes mathématiques du module math pour effectuer les calculs géographiques et mathématiques nécessaires.

## Pour les utilisateurs : 

## Pour les développeur :
Le code est développer de façon modulaire et sous forme de programmation orientée objet. Il est ainsi plus facile d'apporter des modifications au code. 
 
### Améliorations potentielles 
- L'une des principale amélioration possible est d'abord de trouver une base de donnée plus exhaustive, notamment concernant les compagnies aériennes. En effet, lors de notre développement nous nous sommes contenté de mettre au point des fonctionnalités pour exploiter notre dataset restreint.
- Afin de simplifier l'implémentation, nous avons traité les informations des avions manuellement (modèle de moteurs unique, mach de croisière, passager etc...). Il peut être intéressant de trouver une autre base de donnée contenant ces informations, et ne pas limiter un modèle d'avion à un seul moteur. 
- Dans le cas ou un avion/moteur/compagnie n'est pas dans notre base de donnée, il peut être intéressant d'inviter l'utilisateur à saisir les informations manquantes. 
- Les calculs sont également fait à partir d'estimation (distance de trajet, ne prends pas en compte le vent, la rotation de la terre, etc...). Ces facteurs peuvent être pris en considération pour obtenir des données plus précises.

## Ressources utilisées
### Données :
1. Base de donnée sur les compagnies aériennes britanniques (nécessite de créer un compte démo): https://data.icao.int/newDataPlus/Tools (consulté le 2/06/2023).
2. Base de donnée contenant les informations sur les différents moteurs : https://www.easa.europa.eu/en/domains/environment/easa-aeroplane-co2-emissions-database-0 (consulté le 2/06/2023).
### Paquets pythons:
1. __airportsdata__ : Package permettant d'obtenir les coordonnées des aéroports : https://pypi.org/project/airportsdata/
2. __Package__ : permettant d'obtenir les informations sur les conditions atmosphériques : https://pypi.org/project/ambiance/

## Références
1. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Programmation Orientée Objet: Classes et Objets*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 43 p.
2. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Modules: Documentation*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 20 p.
3. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Modules: Introduction aux modules*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 25 p.
4. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Analyse numérique*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 31 p.
5. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Introduction à l'analyse de données*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 25 p.
6. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Programmation scientifique avec NumPy*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 39 p.
7. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Git: Gestion de version*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 24 p.
8. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Fonctions: Introduction aux fonctions*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 34 p.
9. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Scriptage: Scripts*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 50 p.
10. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Environnement de travail: Installation de Python*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 38 p.
11. Sanjosé, Marlène. Tabiai, Ilyass. 2023. MGA802 (Été 2023). *Notions de base: Module 1.b*. Notes du cours MGA802 - Introduction à la programmation avec Python. Programme de maîtrise en génie aérospatial. Montréal: École de technologie supérieure. 72 p.
12. Morency, François. 2023. MEC672 (Hiver 2023). Notes du cours MEC672. Programme de maîtrise en génie mécanique. Montréal: École de technologie supérieure.
