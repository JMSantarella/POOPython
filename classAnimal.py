# création de la classe animal
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

    def __str__(self):
       return f"instance de la classe Animal ayant pour attributs {self.__poids} , {self.__taille} "

