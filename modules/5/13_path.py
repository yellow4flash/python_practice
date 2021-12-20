# C:\Users\user\py\progs
# se encuentra el archivo principal (main.py)
# main.py
from sys import path
# ruta relativa
path.append('..\\modules') # se usa doble diagonal invertida
# por el hecho de que una se usa para escapar de la cadena
# ruta absoluta
path.append('C:\\Users\\user\\py\\modules')
# Nota: tambien puedes usar insert() en lugar de append
import module
# se importa el modulo agregado a path

# C:\Users\user\py\modules .
# se encuentra el archivo module.py
# module.py
# source from module.py