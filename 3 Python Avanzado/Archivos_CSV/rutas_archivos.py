import csv
import os

ruta = "csv_vacio.csv"

ruta_absoluta = "E:\\Python (Practica)\\csv_vacio.csv" # Seteado para un sistema operativo
ruta_absoluta_os = os.path.join(os.getcwd(),"csv_vacio.csv") # Setea Ruta de un archivo para cualquier S.O.

print(ruta_absoluta)
print(ruta_absoluta_os)

