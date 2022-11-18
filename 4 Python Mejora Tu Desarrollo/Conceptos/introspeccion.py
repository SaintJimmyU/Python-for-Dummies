''' La instrospeccion es una habilitad que nos permite conocer a detalle un objeto 

    Para aquello podemos utilizar funciones de python como:
        dir()
        isinstance()
        hasattr()
'''

class Intro():
    Introver=6

    def __init__(self,valor):
        self.valor=valor

    def segundo(self):
        print("Segundo")

    def tercero(self):
        print("Tercero")

dato=Intro("Valor")

print(dir(dato))

print(isinstance(dato,Intro))

print(hasattr(dato,"Introver"))
