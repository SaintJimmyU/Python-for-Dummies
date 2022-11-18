def calcular_promedio(lista1):
    assert len(lista1) > 0, "La Lista esta vacia"
    return sum(lista1) / len(lista1)

promedio = calcular_promedio(lista1=[1,2,3])
print(promedio)
