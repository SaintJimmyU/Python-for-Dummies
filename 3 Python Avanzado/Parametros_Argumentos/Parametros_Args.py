# def Calcular_Perimetro(Lado1,Lado2,Lado3,Lado4):
#     perimetro = Lado1+Lado2+Lado3+Lado4
#     return perimetro

# print(Calcular_Perimetro(1,2,3,4))


def Calcular_Perimetro(*args):
    perimetro = 0

    for lado in args:
        perimetro +=lado
    return perimetro

perimetro = Calcular_Perimetro(1,2,3,4)
print("Perimetro Cuadrado = " + str(perimetro))

triangulo = Calcular_Perimetro(1,2,3)
print("Perimetro Triangulo = " + str(triangulo))