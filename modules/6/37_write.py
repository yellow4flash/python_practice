from os import strerror

try:
	fo = open('newtext.txt', 'wt') #un nuevo archivo (newtext.txt) es creado
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerr(e.errno))
fa=open('newtext.txt','r')
print(fa.read())
fa.close


#! escribir lineas enteras
from os import strerror

try:
	fo = open('newtext.txt', 'wt')
	for i in range(10):
		fo.write("line #" + str(i+1) + "\n")
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerr(e.errno))


#todo: Nota: puedes usar el mismo método para escribir en el stream stderr, pero no intentes abrirlo, 
# ya que siempre está abierto implícitamente.

# Por ejemplo, si deseas enviar un mensaje de tipo cadena a stderr para distinguirlo de la salida normal del programa, puede verse así:
# import sys
# sys.stderr.write("Mensaje de Error")