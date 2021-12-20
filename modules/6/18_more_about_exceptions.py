# Un código etiquetado de esta manera se ejecuta cuando (y solo cuando) 
# no se ha generado ninguna excepción dentro de la parte del try:.
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n

print(reciproco(2))
print(reciproco(0))
#! Nota: la rama else: debe ubicarse después de la última rama except.
# another variant
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))
""" 
#*Nota: estas dos variantes (else y finally) no son dependientes entre si, y pueden 
#*coexistir u ocurrir de manera independiente.

#*El bloque finally siempre se ejecuta (finaliza la ejecución del bloque try-except, de ahí su nombre), 
#*sin importar lo que sucedió antes, incluso cuando se genera o lanza una excepción, sin importar si esta 
#*se ha manejado o no. 
"""