# raise: sirve para lanzar excepciones de manera intencional

def EvaluarNota(nota):
    if nota < 0:
        raise ZeroDivisionError("Como esta excepcion ZeroDivisionError me permite agregar un comentario la utilizo para explicar un mensaje, ya que no tiene nada que ver Division x Zero con el error")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        raise ValueError("Otro ejemplo de lanzamiento de excepcion y personalizar un mensaje")
    else:
        print("Reprobado")

EvaluarNota(12)