import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [ 
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]

datos_dict = [
    {"nombre": "Paco", "apellido": "Boteroáá", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

# '''Para Escribir una fila provenientes de una lista'''
# with open("datos.csv","w",newline="") as archivo:
#     writer = csv.writer(archivo, delimiter=",")
#     writer.writerow(columnas)
#     writer.writerow(dato) # Para escribir una fila

# '''Para escribir varias filas provenientes de una lista'''
# with open("datos.csv","w",newline="") as archivo:
#     writer = csv.writer(archivo, delimiter=",")
#     writer.writerow(columnas)
#     writer.writerows(datos_lista) # Para escribir varias filas 

'''Para escribir varias filas provenientes de un diccionario'''
with open("datos.csv","w",newline="") as archivo:
    writer = csv.DictWriter(archivo,fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict) # Para escribir varias filas 
