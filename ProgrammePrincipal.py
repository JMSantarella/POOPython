#import classe
from classAnimal import *
from classOiseau import *
from classZoo2 import *
from classSerpent import *

#déclaration
pigeon = Oiseau(poids=10, taille =4, altitude_max=40)
aigle = Oiseau(poids=20, taille =10, altitude_max=400)

cochon = Animal(poids= 10, taille = 1)

anaconda = Serpent(poids = 100, taille =12)
vipere = Serpent(poids = 1, taille =1)
cobra = Serpent(poids = 6, taille = 4)


liste_serpent= [anaconda, vipere]
liste__parc_1 = [pigeon,cochon,aigle]

ani = Animal(25,3)

zoo_1 = Zoo(liste_serpent)

zoo_2 = Zoo(liste__parc_1)

zoo_3 = zoo_1 + zoo_2

zoo_1.ajout_animal(cobra)
print(zoo_1.get_listanimal())

print(ani)

print(str(ani))

print()

zoo_3.get_listanimal()
