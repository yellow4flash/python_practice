def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = [x for x in potenciasDe2(5)] #* lista de comprensión

print(t)

t = list(potenciasDe2(3)) #* conviete en una lista el resultado del iterador
print(t)
for i in range(20):
    if i in potenciasDe2(4): # el contexto creado por el operador in también te permite usar un generador.
        print(i)


# Ahora veamos un Generador de números de la serie Fibonacci implementando lo anterior
def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)