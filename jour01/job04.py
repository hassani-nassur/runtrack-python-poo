class Personne:
    nom = ""
    prenom = ""
    
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def sePresenter(self):
        return "Je suis {} {}".format(self.nom,self.prenom)
    
personne1 = Personne("Nassur","Hassani")
personne2 = Personne("Pierre","dupond")

print(personne1.sePresenter())
print(personne2.sePresenter())