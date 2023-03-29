class Form:
    
    def aire(self):
        return 0
class Rectangle(Form):
    def __init__(self,largeur,hauteur) -> True:
        super().__init__()
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__hauteur * self.__largeur
    
    def set_largeur(self,largeur):
        self.__largeur = largeur
        return self.__largeur
    def get_largeur(self):
        return self.__largeur
    
    def set_hauteur(self,hauteur):
        self.__hauteur = hauteur
        return self.__hauteur
    def get_hauteur(self):
        return self.__hauteur
        
figure = Rectangle(3,5)
print("l'aire du rectangle est : ",figure.aire())
