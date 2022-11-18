from logging import exception

lista = [2,4]

try: 
    print(lista[0])
except IndexError:
    print("Error en el Indice")
else:
    print("No hay Error")
finally:
    print("Llego al Final")

''' 
try:
    # aquí ponemos el código que puede lanzar excepciones
except IOError:
    # entrará aquí en caso que se haya producido
    # una excepción IOError
except ZeroDivisionError:
    # entrará aquí en caso que se haya producido
    # una excepción ZeroDivisionError
except:
    # entrará aquí en caso que se haya producido
    # una excepción que no corresponda a ninguno
    # de los tipos especificados en los except previos 
else:
    # Esta es la parte del programa que creemos que está libre de excepciones
finally:
    # Ocurra lo que ocurra, esta parte la ejecutamos siempre 
'''