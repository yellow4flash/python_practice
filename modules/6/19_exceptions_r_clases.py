# try:
#     i = int("Hola!")
# except Exception as e:
#     print(e)
#     print(e.__str__())

"""
El identificador está diseñado para capturar la excepción con el fin de analizar su naturaleza y sacar conclusiones adecuadas.

Nota: el alcance del identificador solo es dentro del except, y no va más allá. 

"""
""" 
#!Este programa muestra todas las clases de las excepciónes predefinidas en forma de árbol.

#*Como un árbol es un ejemplo perfecto de una estructura de datos recursiva,
 """
def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

printExcTree(BaseException)