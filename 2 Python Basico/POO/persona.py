class Persona1:
    pass

jimmy = Persona1()
print(type(jimmy))


class Persona2:
    def __init__(self) -> None:
        print("Estoy en el constructor")

pauli = Persona2()


class Persona3:
    atributo = "123JULIAN123" # --> Atributo de la Clase
    def __init__(self,nombre,edad):
        self.nombre = nombre  # --> Atributo de Instancia
        self.edad = edad  # --> Atributo de Instancia

julian = Persona3("JULIAN",2)
print(julian.nombre)
print(julian.edad)

print(julian.atributo)

class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def cumplir_anio(self):
        self.edad += 1
        print(f"Feliz Cumpleaños # {self.edad} {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad, horas_totales) -> None:
        super().__init__(nombre, edad) # --> Heredamos los Atributos del Contructor (FORMA 1)
        # super(Empleado,self).__init__(nombre,edad) # --> Heredamos los Atributos del Contructor (FORMA 2)
        self.horas_totales = horas_totales

    def trabajar(self,horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas Totales Trabajadas: {self.horas_totales}")

Juanete = Persona("JUANETES",20)
Juanete.cumplir_anio()
Lola = Empleado(nombre="LOLA",edad=15,horas_totales=30)
Lola.trabajar(horas_trabajadas=8)
Lola.cumplir_anio()
