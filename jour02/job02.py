class Personne:
    def __init__(self):
        self._age = 14
    
    def afficheAge(self):
        print(self._age)
    def bonjour(self):
        print("Hello")
    def modifierAge(self,age):
        self._age = age
        
class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCour(self):
        print("je vais en cours")
    def afficheAge(self):
        print("j'ai {} ans".format(self._age))

class Proffesseur(Personne):
    def __init__(self,matierEnseigner="Systeme de gestion de base de donnée (SGBD)"):
        Personne.__init__(self)
        self.__matier_enseigner = matierEnseigner
    def enseigner(self):
        print('Le cour va commencer')
    def getMatierEnseigner(self):
        return self.__matier_enseigner   
    def setMatierEnseigner(self,matier_enseigner):
        self.__matier_enseigner = matier_enseigner
    
# objet eleve
eleve = Eleve()

eleve.bonjour()
eleve.allerEnCour()
eleve.modifierAge(15)
eleve.afficheAge()

# objet proffesseur

prof = Proffesseur()
prof.modifierAge(40)

prof.bonjour()
prof.enseigner()
print("j'enseigner le",prof.getMatierEnseigner())

prof.setMatierEnseigner("Python")

print("actuellement j'eseigne le :",prof.getMatierEnseigner())

