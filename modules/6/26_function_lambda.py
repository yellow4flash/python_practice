# Los matemáticos usan el cálculo Lambda en sistemas formales conectados con: la lógica, 
# la recursividad o la demostrabilidad de teoremas. 
#* Los programadores usan la función lambda para simplificar el código, hacerlo más claro y fácil de entender.
#? lambda parámetros: expresión  # sintax
dos = lambda : 2
cuadrado = lambda x : x * x
potencia = lambda x, y : x ** y

for a in range(-2, 3):
    print(cuadrado(a), end=" ")
    print(potencia(a, dos()))

#* uso común de las funciones
def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

def poli(x):
	return 2 * x**2 - 4 * x + 2

imprimirfuncion([x for x in range(-2, 3)], poli)

#* usando la función lambda
def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)