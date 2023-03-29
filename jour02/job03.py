class Rectangle:
    def __init__(self,longeur,largeur):
        self.__longeur = longeur 
        self.__largeur = largeur
    
    def set_longeur(self,longeur):
        self.__longeur = longeur
        return self.__longeur
    def get_longeur(self):
        return self.__longeur
    
    def set_largeur(self,largeur):
        self.__largeur  = largeur
        return self.__largeur
    def get_largeur(self):
        return self.__largeur
    
    def perimetre(self):
        return 2*(self.__longeur+self.__largeur)

    def surface(self):
        return self.__longeur * self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longeur, largeur,hauteur):
        super().__init__(longeur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    def set_hauteur(self,hauteur):
        self.__hauteur = hauteur
        return self.__hauteur
    def get_hauteur(self):
        return self.__hauteur

figure1 = Rectangle(5,6) #instantiation de la classe Rectangle

# affichage du perimetre est de la surface du rectangle
print("le perimetre de ma figure est ",figure1.perimetre())
print("la surface de ma figure est ",figure1.surface())

# changement de la largeur et de la longeur du figure1
figure1.set_longeur(12)
figure1.set_largeur(10)

# affichae de la longeur et de la hauteur
print("la longeur de ma figure est ",figure1.get_longeur())
print("la largeur de ma figure est ",figure1.get_largeur())

# affichage du perimetre est de la surface du nouveau rectangle
print("le perimetre de ma figure est ",figure1.perimetre())
print("la surface de ma figure est ",figure1.surface())

# creation d'une parallelepipede 
figure2 = Parallelepipede(12,4,5)

print("le volume du parllelepipede est :",figure2.volume())