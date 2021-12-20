# al manejar excepciones comunmente
import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Has abierto demasiados archivos.")
    else:
        printf("El número de error es:", exc.errno)

#! para simplificar el manejo de excepciones usar strerror()
# simplificar el código de manejo de errores. Su nombre es strerror(), y 
# proviene del módulo os y espera solo un argumento: un número de error.
from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    print("El archivo no se pudo abrir:", strerror(exc.errno));