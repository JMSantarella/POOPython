# création de la classe animal
class Animal:
    def __init__(self, poids, taille) :
        self.__taille = taille
        self.__poids = poids
        

    def get_taille(self) :
        return self.__taille
    
    def get_poids(self) : 
        return self.__poids
    
    def se_deplacer(self) :
        pass

    def set_taille(self, taille) :
        if taille > 0 :
            self.__taille = taille
        else :    
            raise ValueError()

    def set_poids(self, taille) : 
        if taille > 0 :
            self.__taille = taille
        else :
            raise ValueError()

    def __str__(self):
       return f"instance de la classe Animal ayant pour attributs {self.__poids} , {self.__taille} "

