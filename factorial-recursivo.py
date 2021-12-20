def fac(n):
    if n<0:
        return
    if n<2:
        return 1
    return n*fac(n-1)
a=int(input('Ingrese un numero: '))
print(fac(a))
# In situ del latín: significa del lugar o momento
# dos tipos de datos en python, (mutables e inmutables)
# Una tupla es una secuencia inmutable