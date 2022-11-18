class Persona():

    def __init__(self):
        pass

    def despedir(self):
        print("CHaoooo!")

    def sigue():
        print("Sigue conversando")

    @classmethod # Esto es un decorador que indica que el siguiente metodo es de clase
    def saludar(cls,nombre):
        print("Saludame " + nombre)

Persona.despedir("")
Persona.sigue()
Persona.saludar("Jimmy")
