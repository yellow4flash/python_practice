from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst)) # choise elige un elemento aleatorio
print(sample(lst, 5))#  sample crea una lista muestra y quita las repeticiones
print(sample(lst, 10))#(lst,arg):lst es la lista muestra, arg es la cantidad de elementos a extraer