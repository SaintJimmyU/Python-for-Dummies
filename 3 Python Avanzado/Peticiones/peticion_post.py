import requests

""" La peticion POST permite enviar informacion a un servicio 
la cual se almacena a una base de datos propia del servicio"""

url = "https://webhook.site/d197e149-af35-40be-916a-6840fb29ae0c" # endpoint

payload = {"plato": "pasta", "cantidad": 2} # Datos enviados (Cuerpo o payload) en forma de diccionario de python porque es compatible con JSON
queryparams = {"nombre":"Jimmy"} # Opcional Podemos enviar parametros

response = requests.post(url, data=payload,params=queryparams)
print(response.status_code) # 200 Peticion OK
print(response.text) # No trae nada porque la respuesta no tiene contenido
print(response.json()) # No trae nada porque al no tener contenido no devuelve un objeto convertido en JSON