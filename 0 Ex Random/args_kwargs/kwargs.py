'''
    *args --> En Python, el parámetro especial *args en una función se usa para pasar, de forma
                opcional, un número variable de argumentos posicionales.

            ▪ Es un parámetro opcional. Se puede invocar a la función haciendo uso del mismo, o no.
            ▪ El número de argumentos al invocar a la función es variable.
            ▪ Son parámetros posicionales, por lo que, a diferencia de los parámetros con nombre, su
                valor depende de la posición en la que se pasen a la función.

    *kwargs --> En Python, el parámetro especial **kwargs en una función se usa para pasar, de forma
                opcional, un número variable de argumentos con nombre.

            Las principales diferencias con respecto *args son:
                ▪ Lo que realmente indica que el parámetro es de este tipo es el símbolo **, el nombre
                    kwargs se usa por convención.
                ▪ El parámetro recibe los argumentos como un diccionario.
                ▪ Al tratarse de un diccionario, el orden de los parámetros no importa. Los parámetros se
                    asocian en función de las claves del diccionario.
'''


def filter(**kwargs):
    query = "SELECT * FROM CLIENTES"
    i=0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE"
        else:
            query += " AND "
        
        query += " {}='{}'".format(key,value)
        i += 1
    query += ";"
    return query


print(filter())
print(filter(ciudad="Guayaquil"))
print(filter(ciudad="GuayaKILL", fecha_alta="23-08-1980"))