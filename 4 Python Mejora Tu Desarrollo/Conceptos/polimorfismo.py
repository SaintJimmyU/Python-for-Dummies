class Perro():
    def avanzar(self):
        print("en 4 Patas")

class Perico():
    def avanzar(self):
        print("volando")

def movimiento(animal):
    animal.avanzar()

perro=Perro()
# perro.avanzar()

perico=Perico()
# perico.avanzar()

movimiento(perro)
movimiento(perico)

