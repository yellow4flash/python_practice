# Los datos amorfos son datos que no tienen forma específica - son solo una serie de bytes.
# Python tiene más de un contenedor, uno de ellos es una clase especializada llamada bytearray - 
# como su nombre indica, es un arreglo que contiene bytes (amorfos).

# no debes establecer ningún elemento del arreglo de bytes con un valor que no sea un entero 
# (violar esta regla causará una excepción TypeError) y tampoco está permitido asignar un valor 
# fuera del rango de 0 a 255 (a menos que quieras provocar una excepción ValueError).

#! bytearray: son mutables, suceptibles a la función len(), casi como listas normales
#* cómo escribir un arreglo de bytes en un archivo binario
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))