def validar_x(x):
    if x < 1:
        raise Exception("La variable X debe de ser mayor a 1")
    else:
        print("X es mayor a 1")

x = 0.3
validar_x(x)