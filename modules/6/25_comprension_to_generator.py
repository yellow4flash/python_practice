listaUno = []

for ex in range(6):
    listaUno.append(10 ** ex)


listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)

#? Solo un cambio puede convertir cualquier comprensión en un generador.
lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()
# Son los paréntesis. Los corchetes hacen una comprensión, los paréntesis hacen un generador.
#todo: aplicar la funcion len() denotará cual es una lista y cual es un generador
#? la comprension o generador se puede crear donde se ocupe, sin necesidad de guardarlos
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

""" 
Nota: la misma apariencia de la salida no significa que ambos bucles funcionen de la misma manera. 
En el primer bucle, la lista se crea (y se itera) como un todo; en realidad, existe cuando se ejecuta el bucle.

En el segundo bucle, no hay ninguna lista, solo hay valores subsequentes producidos por el generador, 
uno por uno.
 """