import requests

""" Siempre que se desee realizar una peticion a una API hay que revisar la documentacion """

response = requests.get("https://api.github.com") # Recibira la url o endpoint de GitHub
print(response) # Creado un tipo de Objeto respuesta con el estado 200
print("----------------------------------------")
print(response.headers) # Los headers relacionados a la peticion
print("----------------------------------------")
print(response.status_code) # Codigo de Estado de la respuesta (200 es OK, es decir que la peticion es satisfactoria)
print("----------------------------------------")
print(response.content) # Datos de la respuesta conocido como cuerpo o carga "payload" (viene en byte 'b')
print("----------------------------------------")
print(response.text) # Convertimos la respuesta en Text
print("----------------------------------------")
print(response.json()) # Tambien podemos obtener la respuesta en diccionario a traves de JSON
print("----------------------------------------")
print(response.json()["current_user_url"]) # Tambien podemos acceder a un valor mediante la llave
print("----------------------------------------")


""" Aqui utilizamos el get pero con parametros para acceder a la busqueda en un endpoint de GitHub
    params --> indicamos los parametros
    {"q","python"} --> "q" indica que se realizara una busqueda y "python" que sera la palabra
    como coicidencia en repositorios que tengan en el nombre, en la descripcion y en el readme
"""
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python"}
) 
print(response.status_code) # 200 indica que la Peticion fue OK
print("----------------------------------------")
print(response.json())
print("----------------------------------------")

data = response.json()
print(data.keys()) # Presentamos las llaves del diccionario a traves de la respuesta del JSON