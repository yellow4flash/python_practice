# El tamaño máximo del búfer de entrada aceptado se pasa al método como argumento.

#* Nota: cuando no hay nada que leer del archivo, el método devuelve una lista vacía.
#* Úsalo para detectar el final del archivo.
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

# Existen dos bucles anidados en el código: el exterior emplea el resultado de readlines() 
# para iterar a través de él, mientras que el interno imprime las líneas carácter por carácter.