# Création de la classe Zoo
class Zoo :
   
   # listanimal est une liste contenant des éléments appartenant à la classe animal
    def __init__(self, listanimal) :
        self.__listanimal = listanimal
       

    def get_listanimal(self) :
        return self.__listanimal
    
    def set_listanimal(self, listanimal) :
        self.__listanimal = listanimal


    def ajout_animal(self,y) :
        if  isinstance (y,str) :
            self.__listanimal.append(y)
        elif isinstance (y,list) :
            self.__listanimal = self.__listanimal + y
            return self.__listanimal
        else :
            return "erreur"
  
  

x = ["lion", "renard", "gazelle"]
a = Zoo(x)
y = "écureuil"
a.ajout_animal(y)

print("les animaux présents dans notre zoo :", a.get_listanimal())

