
#! OverflowError
# Ubicación:
# BaseException ← Exception ← ArithmeticError ← OverflowError
# el código imprime los valores subsequentes 
# de exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')

#!ImportError
#*BaseException ← Exception ← StandardError ← ImportError
#*se genera esta execpción cuando se comete un error al momento de importar

#!KeyError
#*BaseException ← Exception ← LookupError ← KeyError
#*Esta exepcion se genera cuando se intenta ingresar a una clave no existente de un diccionario
#*for example
# como abusar del diccionario
# y cómo lidiar con ello

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)