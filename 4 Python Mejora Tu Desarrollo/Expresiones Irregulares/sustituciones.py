import  re
'''
    la funcion sub toma como parametros un patron a sustituir una cadena que usar como reemplazo
'''
# Reemplazo de numeros por "*" que encuentre en la cadena
print(re.sub(r"\d","*","REEEmplaza los numero 123 por los ***")) 

# Reemplazo de 2 numeros por "**" pero solo a los 2 primeros numeros que encuentre en la cadena
print(re.sub(r"\d","*","REEEmplaza los numero 123 por los **",2))


