from doctest import Example


def calcular_promedio(lista1):
    assert len(lista1) > 0, "La Lista esta vacia"
    return sum(lista1) / len(lista1)

try:
    promedio = calcular_promedio(lista1=["texto"])
    print(promedio)
except AssertionError as assert_error: # Captura error con mensaje Personalizado segun condicion
    print(assert_error)
except Exception as e: # Captura error mensaje Personalizado segun condicion + Mensaje del sistema
    print(f"Funcion no calculo promedio Error: {e}")
