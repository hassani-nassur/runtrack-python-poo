class Student:
    def __init__(self,nom,prenom,numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def add_credits(self,credits):
        
        if(credits >= 0):
            self.__credits += credits
        else:
            print("les credit à ajouter doit être positif")
    
    def get_credits(self):
        return self.__credits
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        self.__nom = nom
    def set_prenom(self,prenom):
        self.__prenom = prenom
    def get_prenom(self):
        return self.__prenom
    def set_numero_etudiant(self,numero_etudiant):
        self.__numero_etudiant = numero_etudiant
    def get_numero_etudiant(self):
        return self.__numero_etudiant
    
    def __studentEval(self):
        
        if(self.__credits >= 90):
            return "Excelente"
        elif(self.__credits >= 80):
            return "Très bien"
        elif(self.__credits >=70):
            return "Bien"
        elif(self.__credits >= 60):
            return "Passable"
        else:
            return "Insuffisant"
    def infoStudent(self):
        self.__level = self.__studentEval()
        print("Nom = {} \nPrenom = {} \nid = {} \nNiveau = {}".format(self.__nom,self.__prenom,self.__numero_etudiant,self.__level)) 
        
etudiant = Student("John",'Doe',145)
etudiant.add_credits(30)
etudiant.add_credits(5)
etudiant.add_credits(50)

etudiant.infoStudent()