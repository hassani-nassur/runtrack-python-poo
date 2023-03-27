class Operation:
    nombre1 = 0
    nombre2 = 0
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
mon_operation = Operation(12,3)

print("Le nombre1 est ",mon_operation.nombre1)
print("Le nombre2 est ",mon_operation.nombre2)