import yaml

class Lecteuryamel():

    def __init__(self):
        self.file = open("Donnees.yaml", 'r')
        self.content = yaml.load(self.file)
    
    def print_content(self):
        print("Voici les donnees entrées")
        for key, value in self.content.items():
            print(f"{key}: {value}")
