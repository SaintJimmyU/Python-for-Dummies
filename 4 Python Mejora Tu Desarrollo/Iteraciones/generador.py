# EJEMPLO 1

def Numeros():
    n = 1

    while True:
        yield n # --> yield devuelve el siguiente valor(generador) sobre el que iterar en lugar de usar return
        n = n+1

i = Numeros()
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__()) 
print(i.__next__())


# EJEMPLO 2

def mi_generador(n,m,s):
    while (n<=m):
        yield n
        n+=s

x = mi_generador(0,5,1)
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())