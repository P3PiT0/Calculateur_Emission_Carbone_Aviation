import yaml

class lecteuryamel():

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
