# La función map() aplica la función pasada por su primer argumento a todos los elementos 
# de su segundo argumento y devuelve un iterador que entrega todos los resultados de funciones posteriores. 
lista1 = [x for x in range(5)] #comprension
lista2 = list(map(lambda x: 2 ** x, lista1))# lista a partir de un map()

print(lista2)
# lo común
def alCuadrado(x):
    return x*x
for x in map(alCuadrado, lista2): # esta es la manera de invocar una funcion en map()
	print(x, end=' ')
print()
# con una función lambda
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()