class Vehicule:
    def __init__(self,marque,model,annee,prix):
        self._marque = marque
        self._model = model
        self._annee = annee
        self._prix = prix
    def informationVehicule(self):
        print("Marque = {}\nModel = {}\nAnnee = {}\nPrix = {} €".format(self._marque, self._model, self._annee, self._prix))
    def demarrer(self):
        print("Attention je roule")
class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix,porte = 4):
        super().__init__(marque, model, annee, prix)
        self.__porte = porte
    def informationVehicule(self):
        print("Marque = {}\nModel = {}\nAnnee = {}\nPrix = {} €\nPortes = {}".format(self._marque, self._model, self._annee, self._prix, self.__porte,))
    def demarrer(self):
        print("demarage de la voiture enclencher")

class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix,nombre_roues = 2):
        super().__init__(marque, model, annee, prix)
        self.__nombre_roues = nombre_roues
    def informationVehicule(self):
        print("Marque = {}\nModel = {}\nAnnee = {}\nPrix = {} €\nNombre de roues = {}".format(self._marque, self._model, self._annee, self._prix,self.__nombre_roues))
    def demarrer(self):
        print("Bou bou boummmm!!!")
# instanciation de voiture
voiture1 = Voiture("Renault","clio 3","2023",3000)
voiture1.informationVehicule()
voiture1.demarrer()

# instanciation de moto
moto1 = Moto("YAMAHA","T-max 530","2023",2000,2)
moto1.informationVehicule()
moto1.demarrer()