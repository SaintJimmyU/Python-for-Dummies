def mi_decorador(funcion):
    def nueva_funcion(*args,**kwargs):
        print("Llamada a la funcion :",funcion.__name__)
        retorna = funcion(*args,*kwargs)
        return retorna
    return nueva_funcion

@mi_decorador
def funcion_normalete(s):
    print(s)

funcion_normalete("El dia vivire vistiendo la Amarilla")
