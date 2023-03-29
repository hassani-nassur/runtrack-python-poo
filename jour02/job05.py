from math import pi
class Form:
    
    def aire(self):
        return 0

class Cercle(Form):
    def __init__(self,radius) -> None:
        super().__init__()
        self.__radius = radius
    def aire(self):
        return pow(self.__radius,2) * pi

c1 = Cercle(12)

print(c1.aire())
