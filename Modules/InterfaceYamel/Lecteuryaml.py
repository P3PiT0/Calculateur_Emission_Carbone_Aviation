import yaml

class lecteuryamel():
    '''
    Cette classe représente un lecteur de fichier YAML nous permettant de traiter les paramètres utilisateurs
    '''
    # Constructeur de la classe
    def __init__(self):
        """
        Constructeur pour l'interface utilisateur de type yaml.
        Le constructeur charge le fichier 'Donnees.yaml' rempli au préalable par l'utilisateur.
        """
        self.file = open("Modules/InterfaceYamel/Donnees.yaml", 'r')
        self.content = yaml.safe_load(self.file)

    def print_content(self):
        """
        Méthode qui construit et retourne un dictionnaire contenant les entrées de l'utilisateurs, spécifiées dans le fichier 
        'Donnees.yaml' rempli au préalable par l'utilisateur.
        
        :return: Dictionnaire contennant les différents paramètres utilisateurs
        :rtype : Dictionnaire 
        """
        Donnees_dict = {}
        print("Voici les donnees entrées")
        for key, value in self.content.items():
            Donnees_dict[key] = value
            print(f"{key}: {value}")

        return Donnees_dict
        

   
