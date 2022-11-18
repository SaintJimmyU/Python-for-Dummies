''' Sumar 2 Numeros. Utilizando *args '''
# def sum_nums(*args):
#     total = 0
#     for n in args:
#         total += n

#         # print(n)
#         # print(total)
#     return total 

# print(sum_nums(3,-8))

''' Sumar N Cantidad de Numeros y Calcular su Promedio. Utilizando *args '''
def sum_nums(*args):
    return sum(args,00.0) / len(args)
    
print(sum_nums(1,2,3,4,5))