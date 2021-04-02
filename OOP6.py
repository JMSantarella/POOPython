# Création de la classe Zoo
class Zoo :
   
    def __init__(self, x) :
        self.__x = x
        

    def get_x(self) :
        return self.__x
    
    def set_x(self) :
        self.__x = x


    def ajout_animal(self,y) :
        if y == str :
            self.__x.append(y)
        elif y == list :
            self__x = self__x + y
            return self__x
        else :
            return "erreur"
        

x = ["lion", "renard", "gazelle"]
a = Zoo(x)
y = "écureuil"
a.ajout_animal(y)

print("les animaux présents dans notre zoo :", x)

