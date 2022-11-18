class Clase():
    def __new__(cls): # Metodo que crea la instacia y llama al __init__
        print("Imprimir new")
        return super().__new__(cls) # --> en esta linea hay que regresar la instancia para que se ejecute el metodo  __init__

    def __init__(self): # Metodo de Inicializacion cuando la clase es creada
        print("Imprimir init")

c=Clase()