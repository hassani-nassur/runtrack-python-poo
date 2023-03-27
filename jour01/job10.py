class Voiture:
    def __init__(self,marque,model,annee,kilometrage,reservoir = 50):
        self.__marque = marque
        self.__model = model
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__marche = False
        self.__reservoir = reservoir
    
    def set_marque(self,marque):
        self.__marque = marque
    def get_marque(self):
        return self.__marque
    
    def set_model(self,model):
        self.__model = model
    def get_model(self):
        return self.__model
    
    def set_annee(self,annee):
        self.__annee = annee
    def get_annee(self):
        return self.__annee
    
    def set_kilometrage(self,kilometrage):
        self.__kilometrage = kilometrage
    def get_kilometrage(self):
        return self.__kilometrage
    
    def demarre(self):
        
        if(self.__verifier_plein() >= 5):
            self.__marche = True
            return self.__marche
        else:
            self.__marche = False
            return self.__marche
        
    def arreter(self):
        if(self.__marche):
            self.__marche = False
            return self.__marche
    def set_reservoir(self,reservoir):
        self.__reservoir = reservoir
        
    def __verifier_plein(self):
        return self.__reservoir
    

voiture1 = Voiture("Renault","Clio 3",2022,120)
print("une {} de l'an {} avec {} kilometre au compteur".format(voiture1.get_model(),voiture1.get_annee(),voiture1.get_kilometrage()))
print(voiture1.demarre())

voiture1.set_reservoir(2)
print(voiture1.demarre())



