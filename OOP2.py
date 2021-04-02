# création de la classe animal
class Animal:
    poids = 0
    taille = 0

    def se_deplacer(*args):
        pass


class Serpent(Animal) :
    def se_deplacer(*args):
        print("Je rampe")


class Oiseau(Animal) :
    def se_deplacer(*args):
        print("Je vole")


aigle = Oiseau
aigle.se_deplacer()

naja = Serpent
naja.taille = 2
print (naja.taille)

naja.se_deplacer ()