# Création de la classe animal
class Animal:
    def __init__(self, poids, taille) :
        self.animal_taille = taille
        self.animal_poids = poids

    def se_deplacer(*args):
        pass

# Création des sous classes Serpent et Oiseau
class Serpent(Animal) :
    def se_deplacer(*args):
        print("Je rampe")

# Utilisation de <super> pour modifier la fonction __init__ définie dans la classe Animal pour lui ajouter l'argument altitude_max
class Oiseau(Animal) :
    def __init__ (self, poids, taille, altitude_max) :
        super().__init__(poids,taille)
        self.oiseau_altitude_max = altitude_max

    def se_deplacer(*args):
        print("Je vole")

y = 1000
aigle = Oiseau (12, 18, y)
print(aigle.oiseau_altitude_max)

