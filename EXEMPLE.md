# Exemple d'éxécution de l'application:
## Sélection de données dans le fichier 'Donnees.yaml'

Dans un premier temps, l'utilisateur doit saisir les informations désirées dans le fichier 'Donnees.yaml' (Modules > InterfaceYaml). Pour connaître les modèles d'avions et les compagnies aériennes présentent dans nos données ainsi que l'orthographe exacte, il est conseillé d'aller se référer aux bases de données présente dans Data. Si l'orthographe ne corresponds pas aux données, le code renverra une erreur et prendra fin. 

![img.png](Images/img.png)

Pour le remplissage du fichier YAML, suivez les instructions en commentaire. 

## Ajout ou modification de données 

Si vous souhaitez avoir des informations sur un avion ou une compagnie qui ne se trouve pas dans la base de donnée, vous devez compléter celles-ci mais également ajouter l'avion à la table de correspondance présente dans Modules > Avion > Aircraft.py. Il est égalment possible de modifier les données des avions (moteur, altitude de vol, mach etc...) en modifiant cette table. Cependant, si vous souhaitez changer le modèle du moteur, vérifiez bien que celui-ci est bien dans Data > EmissionData.csv avec le bon orthograhe. 

## Éxécution du fichier 'Main.py'
### Validation des saisies utilisateur
Premièrement, lorsque que vous exécutez le script, vous obtenez le message suivant dans votre console:
![img_1.png](Images/img_1.png)

Après avoir appuyé sur la touche 'ENTRER' de votre clavier, l'application vous affiche les sélections que vous avez saisie dans le fichier 'Donnees.yaml' et vous demande de valider celles-ci.

![img_2.png](Images/img_2.png)

Si vous entrez NON, ou tout autres messages autre que 'OUI', il vous sera demandé de modifier la saisie dans le fichier yaml (), d'appuyer de nouveau sur 'ENTRER'. Les nouvelles données saisies seront alors affichées et vous pourrez les valider.
**Après avoir modifié vos données yaml, n'oubliez pas de sauvegarder avant d'appuyer sur ENTRER dans le terminal**

Si vous entrez OUI, le programme poursuit son éxécution. 

### Comparaison des compagnies aériennes:
Si le mode comparaison des compagnies est activé (true dans le yaml):

1. Le programme affiche le message 'Voici un diagramme barre de comparaison des émissions de CO2/passager des différentes compagnies aériennes britanniques' et le graphique suivant:
![img_4.png](Images/img_4.png)
Fermez la fenêtre du grahique en appuyant sur le bouton X dans le coin en haut à droite.

2. Le programme affiche le message 'Voici un diagramme barre de comparaison des émissions totales des différentes compagnies aériennes britanniques' et le graphique suivant:
![img_5.png](Images/img_5.png)
Fermez la fenêtre du grahique en appuyant sur le bouton X dans le coin en haut à droite.

3. Le programme affiche le message 'Voici un diagramme barre de comparaison des émissions liées au transport de marchandises des différentes compagnies aériennes britanniques' et le graphique suivant:

![img_6.png](Images/img_6.png)
Fermez la fenêtre du grahique en appuyant sur la croix dans le coin en haut à droite.

### Analyse des compagnies aériennes:
Si le mode analyse des compagnies aériennes est activé (true dans le yaml):

1. Le programme affiche le message suivant:
![img_7.png](Images/img_7.png)
Le pie chart suivant est affiché:
![img_8.png](Images/img_8.png)

Fermez la fenêtre du grahique en appuyant sur le bouton X dans le coin en haut à droite.

2. Le programme affiche le message 'Voici un diagramme montrant la part d'utilisation des modèles d'avions de la flotte' et affiche le graphe ci-dessous:
![img_9.png](Images/img_9.png)

Fermez la fenêtre du grahique en appuyant sur le bouton X dans le coin en haut à droite.

### Menu de comparaison de vols
Si le mode comparaison de vols est activé (true dans le yaml)

Le programme affiche les données suivantes:
![img_10.png](Images/img_10.png)

Ceci marque la fin de l'éxécution du programme.