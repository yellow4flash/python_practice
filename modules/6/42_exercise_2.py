from os import strerror
#  LABORATORIO

# Tiempo Estimado

# 15-20 minutos
# Nivel de dificultad

# Medio
# Prerrequisitos

# 05_9.15.1
# Objetivos

#     Mejorar las habilidades del estudiante para operar con archivos en modo (lectura/escritura).
#     Emplear lambdas para cambiar el ordenamiento.

# Escenario

# El código anterior necesita ser mejorado. Está bien, pero tiene que ser mejor.

# Tu tarea es hacer algunas enmiendas, que generen los siguientes resultados:

#     El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero).
#     El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión '.hist' (debe concatenarse con el nombre original).

# Suponiendo que el archivo de prueba contiene solo una línea con:
# cBabAa

# El resultado esperado debería verse de la siguiente manera:
# a -> 3
# b -> 2
# c -> 1

# Tip:

# Emplea una lambda para cambiar el ordenamiento.

srcname = input("¿Nombre del archivo fuente?: ")
tempname=''
try:
    if srcname.count('.')>1:
        raise Exception('Solo debe contener un punto')
    src = open(srcname, 'r')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)

for e in srcname:
    if e=='.':
        break
    tempname+=e
dstname = tempname+'.hist'

try:
    dic = {}
    cnt = lettercount = 0
    content = src.read()
    dst = open(dstname, 'wt')
    for ch in content:
        print(ch, end='')
        if ch.isspace():
            continue
        lettercount=content.count(ch)
        dic[ch]=lettercount
        cnt += 1

except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)
writes = ''
for k,v in sorted(dic.items(), key= lambda x:x[1], reverse=True):
    # print(k,'->',v)
    writes=k+' -> '+str(v)+'\n'
    dst.write(writes)
print()
c=0

src.close()
dst.close()