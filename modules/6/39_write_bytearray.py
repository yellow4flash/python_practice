from os import strerror

# Primero, inicializamos bytearray con valores a partir de 10; si deseas que 
# el contenido del archivo sea claramente legible, reemplaza el 10con algo como ord('a'), 
# esto producirá bytes que contienen valores correspondientes a la parte alfabética del código ASCII 
# (no pienses que harás que el archivo sea un archivo de texto; sigue siendo binario, ya que se creó 
# con un indicador - bandera wb).
#! Escritura del bytearray
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

#! lectura del bytearray
from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

# af=open('file.bin', 'rb')
# print(af.read())
# af.close


# ingresa aquí el código que lee los bytes del stream

#! leer un archivo de un objeto de bytes
# ntenta leer todo el contenido del archivo en la memoria, haciéndolo parte 
# de un objeto recién creado de la clase bytes.
from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

# Ten cuidado - no utilices este tipo de lectura si no estás seguro de que el 
# contenido del archivo se ajuste a la memoria disponible.

#! read() al usar argumentos, especifica el número de bytes
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5)) #! acá se especifica el número de bytes en el mpetodo read()
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerr(e.errno))
