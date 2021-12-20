from os import strerror

srcname = input("¿Nombre del archivo fuente?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)
dstname = input("¿Nombre del archivo de destino?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerr(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerr(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()

# La línea 17: prepara una parte de memoria para transferir datos del archivo fuente al destino; 
# Tal área de transferencia a menudo se llama un búfer, de ahí el nombre de la variable; el tamaño 
# del búfer es arbitrario; en este caso, decidimos usar 64 kilobytes; técnicamente, un búfer más 
# grande es más rápido al copiar elementos, ya que un búfer más grande significa menos operaciones 
# de E/S; en realidad, siempre hay un límite, cuyo cruce no genera más ventajas; pruébalo tú mismo si quieres.

# Línea 22: escribe el contenido del búfer en el archivo de salida (nota: hemos usado un segmento 
# para limitar la cantidad de bytes que se escriben, ya que write() siempre prefiere escribir todo el búfer).