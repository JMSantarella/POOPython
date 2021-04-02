from classAnimal import *
# Utilisation de <super> pour modifier la fonction __init__ définie dans la classe Animal pour lui ajouter l'argument altitude_max
class Oiseau(Animal) :
    def __init__ (self, poids, taille, altitude_max) :
        super().__init__(poids, taille)
        self.altitude_max = altitude_max

    def se_deplacer(self):
        print("Je vole")