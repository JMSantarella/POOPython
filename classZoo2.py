#import classe
from classAnimal import *

# Création de la classe Zoo
class Zoo :
   
   # listanimal est une liste contenant des éléments appartenant à la classe animal
    def __init__(self, listanimal) :
        self.set_listanimal(listanimal)
       

    def get_listanimal(self) :
        for elm in self.__listanimal:
            print(elm)
        return self.__listanimal
    
    def set_listanimal(self, listanimaux) :
        self.__listanimal = list()
        for elm in listanimaux :
            if isinstance(elm, Animal):
                self.__listanimal.append(elm)  
            else :
                print("erreur type")  

    def ajout_animal(self,y) :
        if  isinstance (y, Animal) :
            self.__listanimal.append(y)
        
        
    def __add__(self, other) :
        listanimal_total = self.__listanimal + other.__listanimal
        return Zoo(listanimal_total)

  


