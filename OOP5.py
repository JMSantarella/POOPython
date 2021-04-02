# Création de la classe animal
class Animal:
    def __init__(self, poids, taille) :
        self.__taille = taille
        self.__poids = poids

    def get_taille(self) :
        return self.__taille
    
    def get_poids(self) : 
        return self.__poids
    

    def set_taille(self, taille) :
        if taille > 0 :
            self.__taille = taille
        else :    
            print("FalseValue")

    def set_poids(self, taille) : 
        if poids > 0 :
            self.__poids = poids
        else :
            print("FalseValue")


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

lion = Animal(250, 3.20)
renard = Animal (8, 0.60)
chien = Animal (25, 1)


print("lion : poids =", lion.get_poids())
print ("renard : taille =", renard.get_taille())
print(chien.get_poids())
