class Animal:
    age = 0
    prenom = ""
    
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self,prenom):
        self.prenom = prenom
        
animal1 = Animal()
print("L'age de l'animal est ",animal1.age)

animal1.vieillir()
print("L'age de l'animal est ",animal1.age)

animal1.nommer("Dig")

print("L'animal se nomme ",animal1.prenom)