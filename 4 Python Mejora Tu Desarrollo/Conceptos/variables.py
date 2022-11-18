class Persona():
    edad = 42 # --> Variables de Clase

    def __init__(self,nombre,nacionalidad) -> None:
        self.nombre = nombre # --> Variable de Instancia
        self.nacionalidad = nacionalidad # --> Variable de Instancia

    def nadar(self): # --> En los metodos de Instancia siempre debe de ir self cuando no se recibe parametro
        print("I'm swiming")

persona1 = Persona("Jimmy","Ecuatoriano")
print(persona1.nombre)

print(Persona.edad)

persona1.nadar()