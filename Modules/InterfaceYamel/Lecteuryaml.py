import yaml

class lecteuryamel():

    # Constructeur de la classe
    def __init__(self):
        self.file = open("Modules/InterfaceYamel/Donnees.yaml", 'r')
        self.content = yaml.safe_load(self.file)



    def print_content(self):
        Donnees_dict = {}
        print("Voici les donnees entrées")
        for key, value in self.content.items():
            Donnees_dict[key] = value
            print(f"{key}: {value}")

        return Donnees_dict
        """
        Constructeur pour l'interface utilisateur de type yaml.
        Le constructeur charge le fichier 'Donnees.yaml' rempli au préalable par l'utilisateur.
        """

    """
    Méthode qui construit et retourne un dictionnaire contenant les entrées de l'utilisateurs, spécifiées dans le fichier 
    'Donnees.yaml' rempli au préalable par l'utilisateur.
    """
