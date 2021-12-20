# filter()
# filtra su segundo argumento mientras es guiado por direcciones que fluyen desde 
# la función especificada en el primer argumento (la función se invoca para cada 
# elemento de la lista, al igual que en map() ).
from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)

"""#todo: Nota: hemos hecho uso del módulo random para inicializar el generador de números aleatorios 
 (que no debe confundirse con los generadores de los que acabamos de hablar) con la #? función seed()
"""