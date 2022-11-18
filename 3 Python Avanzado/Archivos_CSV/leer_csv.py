import csv

""" UTF-8 es un codificador popular por su compatible con los codigos ASCII 
 with open("datos.csv","r",encoding="UTF-8") as archivo: """

"""" "UTF-8" me daba un error dado que el archivo contenia un caracter "ñ" al codificarlo en Windows era incompatible.
Por lo tanto tuve que utilizar otro codificador como lo es "latin-1" el soporta caracteres como la "ñ"
with open("datos.csv","r",encoding="latin-1") as archivo: """

""" Si no especificamos parametro de encoding. Pueden ocurrir 2 cosas:
1. Podria leerse todo el contenido pero sin extraer el caracter original
2. Podria Leer los caracteres originales con normalidad. 
with open("datos.csv","r") as archivo: """

with open("datos.csv","r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)


""" Podemos Obviar la lectura de la primera linea del archivo utilizando la funcion "Next"

        with open("datos.csv","r") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            for fila in reader:
                print(fila)

    O tambien almacenarla en una variable e incluso utilizar para presentarla mientras la salta.

        with open("datos.csv","r") as archivo:
            reader = csv.reader(archivo)
            columnas = next(reader)
            print("Columnas, columnas)
            for fila in reader:
                print(fila)

    Tambien podriamos leerla como si fuera un diccionario utilizando la funcion "DictReader" en lugar de "Reader"
"""
with open("datos.csv","r") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print("----------------------------------------")
        print(fila)
        print("----------------------------------------")
        print(fila["nombre"])

