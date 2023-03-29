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
        super().__init__()
        __matierEnseigner = matierEnseigner
    def enseigner(self):
        print('Le cour va commencer')


pers = Personne()
pers.afficheAge()

eleve = Eleve()
eleve.afficheAge()