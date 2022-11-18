import re

''' 
    Con la funcion match() buscamos en el segundo argumento de la funcion
    lo que establezcamos de filtro en el primer argumento de la funcion
'''

def matcheo():
    if re.match("Python","Python"): # --> Busca Exactamente lo especificado en el primer argumento
        print("Encontro")
matcheo()

def matcheo():
    if re.match(".ython","Cython"):  # --> Busca Exactitud a partir del "."
        print("Encontro *ython")
matcheo()

def matcheo():
    if re.match("...\.","abc."):  # --> Busca Exactitud a partir del "." saltando caracteres anteriores al "."
        print("Encontro el punto")
matcheo()

def matcheo():
    if re.match("(M|i|X|J)immy","Jimmy"):  # --> Busca Exactitud cualquier palabra que comience con 
                                        # los caracteres especificados de entre los |
        print("Encontro Caracteres entre (|)")
matcheo()

def matcheo():
    if re.match("[Jim]immy","Jimmy"):  # --> Busca Exactitud caracteres que comiencen con 
                                    # cualquier caracter de entre [] como "Jim" y
                                    # terminen con caracteres especificados como restantes
        print("Encontro Caracteres entre []")
matcheo()

def matcheo():
    if re.match("Python[0-9]","Python91"):  # --> Busca Exactitud caracteres que comiencen con "Python" y 
                                            # terminen con cualquier digito de entre los [] con un rango
        print("Encontro Caracteres con rango")
matcheo()

def matcheo():
    if re.match("Python\d","Python12"):  # --> \d Equivale a [0-9]
        print("Encontro Caracteres con rango utilizando \d")
matcheo()

def matcheo():
    if re.match("Python[0-9a-zA-Z]","PythonX"):  # --> Busca Exactitud caracteres que comiencen con "Python" y 
                                                # terminen con cualquier digito o caracter en minuscula
                                                # o mayuscula de entre los [] con un rango
        print("Encontro Caracteres con rango numerico y rango de caracter")
matcheo()

def matcheo():
    if re.match(r"Python[\\.,/]","Python.\\"):  # --> Busca Exactitud caracteres que comiencen con "Python"
                                                # y terminen con cualquier caracter especial como la ","" o el "." o "\"
        ''' Cuando uno quiere igualar una barra inversa literal, debe escaparse en la expresión regular.
            Con la notación de cadena raw, esto significa r"\\". Sin la notación de cadena, 
            uno debe usar "\\\\", haciendo que las siguientes líneas de código sean funcionalmente idénticas: 
        '''
        print("Encontro Caracteres Especiales")
matcheo()

def matcheo():
    if re.match("Python[^0-9a-z]","Python+"):  # --> Busca Exactitud cualquier palabra que comiencen con 
                                            # "Python" y que como ultimo caracter no tenga numeros 
                                            # ni letras minusculas. Esto Gracias al simbolo "^" Circunflejo
        print("Encontro Caracteres que no esten dentro del rango ^")
matcheo()

def matcheo():
    if re.match("Python\D","Python+"):  # --> \D Equivale a [^0-9] 
        print("Encontro Caracteres que no esten dentro del rango ^ utilizando \D")
matcheo()

def matcheo():
    if re.match("Python\w","Python5X12"):  # --> \w Equivale a [a-zA-Z0-9_] 
        print("Encontro Caracteres que no esten dentro del rango utilizando \w")
matcheo()

def matcheo():
    if re.match("Python\w","Python+"):  # --> \W Equivale a [^a-zA-Z0-9_] 
        print("Encontro Caracteres que no esten dentro del rango ^ utilizando \W")
matcheo()

def matcheo():
    if re.match("Python\s","Python Espacio"):  # --> \s Equivale a [ \t\n\r\f\v] 
        print("Encontro Caracteres que no esten dentro del rango utilizando \s")
matcheo()

def matcheo():
    if re.match("Python\S","PythonEspacio"):  # --> \S Equivale a [^ \t\n\r\f\v] 
        print("Encontro Caracteres que no esten dentro del rango ^ utilizando \S")
matcheo()

