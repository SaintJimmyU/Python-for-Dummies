def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

lado_cuadrados = [1,3,4]
areas_cuadrados = []

for lado in lado_cuadrados:
    area = calcular_area_cuadrado(lado)

    areas_cuadrados.append(area)

""" Para Debugear:

    Necesitamos entrar mediante consola al modo debug denotado por las letras 'Pdb'
    esto lo hacemos con la instruccion 'python -m pdb nombre_del_archivo.py'
    
    --> python -m pdb '.\Python Avanzado\Debugging\debug.py' 
    
    --> con la instruccion 'l' enlistamos el contenido del debug el cual indica el archivo.py 
    que esta en modo depuracion, la linea en la que esta ubicado la instancia del debug y 
    las restantes lineas del codigo.

    --> con la instruccion 'q' salimos del modo debug

    --> con la instruccion 'break' ó 'b' + #linea del codigo para indicar un punto de debug

    --> con la instruccion 'continue' volvemos ejecutar el break

    --> con la instruccion 'next' se debagea linea por linea sin necesidad de utilizar un breakpoint

    --> con la instruccion 'display' + nombre de la variable se muestra el valor de esa variable

    --> con la instruccion 'undisplay' + nombre de la variable se deja de mostrar el valor de esa variable

    --> con la instruccion 'restar' reiniciamos el debug """
