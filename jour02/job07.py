import random

class Cart:
    
    _valeur = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    _name_carte= ["as","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","valet","dame","roi"]
    _signe = ["coeur","pique","carreau","trefle"]
    
    def __init__(self):
        pass
    
class Jeu(Cart):
   
    __carteServie = []
    __packet = []
    __player_servie = []
    
    def __init__(self):
        for i in range(len(self._name_carte)):
            for j in super()._signe:
                self.__packet.append(
                    {
                        "nom":self._name_carte[i] +" "+ j,
                        'valeur':self._valeur[i]
                    }
                )
    
    def get_packet(self):
        return self.__packet
    
    def piochet (self):
        
        not_choise= []
        for j in self.__packet:
            if j not in self.__carteServie:
                not_choise.append(j)
            
        choix = random.choice(not_choise)
            
        self.__player_servie.append(choix)
        self.__carteServie = self.__carteServie + self.__player_servie
        
        for k in self.__player_servie :
            if k in self.__packet:
                self.__packet.remove(k)
        return self.__player_servie   
    
    def jouer(self):
        
        i = 0
        nombre_service = 1
        
        while i < nombre_service:
            
            servie = self.piochet()
            _point_player = 0
            _point_croupier = 0
            
            i += 1            
            
            for cart in servie:
                _point_player += cart["valeur"]    
            
            if(_point_player <= 21 ):
                rep = input("le nombre de point servie est : {} Voulez vous piocher encore? o:(oui) n:(non) : ".format(_point_player))
                
                if rep.lower() =='o':
                    i = 0
                    nombre_service = 1
                else:
                    while _point_croupier < 17:
                        service = self.piochet()
                        for cart in service:
                            _point_croupier += cart["valeur"]
                    
                    if(_point_croupier > _point_player and _point_croupier < 21):
                        print("le joueur a perdu avec {} face à {}".format(_point_player,_point_croupier))
                    else:
                        print("le joueur gagne avec {} face à {}".format(_point_player,_point_croupier))
                    
                    i = 0
                    nombre_service = -1
            else:
                print("Vous avez perdu vous avez {} ce qui depasse 21".format(_point_player))
                i = 0
                nombre_service = -1

# debut du jeu
mon_packet = Jeu()
mon_packet.jouer()