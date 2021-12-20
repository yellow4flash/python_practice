from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo: ", ccnt)
	print("Lineas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerr(e.errno))

# el objeto es una instancia de la clase iterable.

# El protocolo de iteración definido para el objeto del archivo es muy simple: 
# su método __next__ solo devuelve la siguiente línea leída del archivo.