class Rectangle:
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
    
    def set_longeur(self,longeur):
        self.__longeur = longeur
    def get_longeur(self):
        return self.__longeur
    
    def set_largeur(self,largeur):
        self.__largeur = largeur
    def get_largeur(self):
        return self.__largeur

mon_rectangle = Rectangle(10,5)
# affichage avant modification
print("Rectangle de longeur : {} et de largeur: {}".format(mon_rectangle.get_longeur(),mon_rectangle.get_largeur()))

mon_rectangle.set_longeur(6)
mon_rectangle.set_largeur(3)
# affichage apres modification
print("Rectangle de longeur : {} et de largeur: {}".format(mon_rectangle.get_longeur(),mon_rectangle.get_largeur()))

