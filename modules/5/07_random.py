from random import random, seed, randrange, randint

seed(0)# establece la semilla con el valor entero 0

for i in range(5):
    print(random())

randrange(1)# randrange(fin)x
randrange(0, 1)# randrange(inico, fin)
randrange(0, 1, 1)# randrange(inicio, fin, incremento)
randint(0, 1)# randint(izquierda, derecha)
