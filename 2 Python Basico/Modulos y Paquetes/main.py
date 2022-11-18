from cuadrado import area_cuadrado,perimetro

lado = 5

cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro(lado)
}

print(cuadrado)

perimetro = perimetro(lado)
print(perimetro)


# --------------------------------------------------------

from figuras.cuadrado2 import area_cuadrado,perimetro
from figuras.circulo import area_circulo,perimetro_circulo

lado = 4

cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro(lado)
}
print("CUADRADO : {cuadrado}")

radio = 5

circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}

print("CIRCULO : {circulo}")