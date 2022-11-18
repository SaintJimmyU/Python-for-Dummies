def es_multiplo(numero, multiplo):
    return numero % multiplo == 0

if es_multiplo(9,3.3) == True:
    print("Es Multiplo")
else:
    print("NO es Multiplo")

def imprime_multiplos(numero):
    for i in range(1,numero+1):
        if es_multiplo(numero,i):
            print(f"{i},", end="")

numero = 66
print(f"Los Multiplos del numero {numero} son: ")
imprime_multiplos(numero)