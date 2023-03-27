class Livre:
    def __init__(self,titre,auteur,nombre_page):
        self.__titre = titre
        self.__auteur = auteur
        self.__disponible = True
        try:
            nbr_page = int(nombre_page) 
            if(nbr_page < 0):
                print("Le nombre de page doit être un entier positif")
            else:
                self.__nombre_page = nbr_page 
        except Exception:
            print("seul les entiers sont acceptés comme nombre de page")
    
    def set_titre(self,titre):
        self.__titre = titre
    def get_titre(self):
        return self.__titre
    
    def set_auteur(self,auteur):
        self.__auteur = auteur
    def get_auteur(self):
        return self.__auteur

    def set_nombre_page(self,nombre_page):
        try:
            nbr_page = int(nombre_page) 
            if(nombre_page < 0):
                print("Le nombre de page doit être un entier positif")
            else:
                self.__nombre_page = nbr_page 
        except Exception:
            print("seul les entier sont prise en charge")
    def get_nombre_page(self):
        return self.__nombre_page
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if(self.verification()):
            self.__disponible = False
        else:
            print(self.verification())
    
    def rendre(self):
        if(not self.verification()):
            self.__disponible = True
        