import csv

ruta = "archivo_vacio.csv"

archivo_abierto = open(ruta,"w")

writer = csv.writer(archivo_abierto,delimiter=",")

archivo_abierto.close()

