class Livre:
    def __init__(self,titre,auteur,nombre_page):
        self.__titre = titre
        self.__auteur = auteur
        
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
    
livre1 = Livre("Le diable Boiteux","Alain-Réne Lesage",352)

print("le titre est ",livre1.get_titre())
print("l'auteur est ",livre1.get_auteur())
print("le nombre de page est ",livre1.get_nombre_page())

livre1.set_nombre_page(-112)
print("le nombre de page est ",livre1.get_nombre_page())