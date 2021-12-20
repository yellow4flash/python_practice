# este código no puede ser terminado
# presionando Ctrl-C

# from time import sleep
# seconds = 0
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("¡No hagas eso!")

#!MemoryError
#Ubicación:
#BaseException ← Exception ← MemoryError

# este código causa la excepción MemoryError
# advertencia: ejecutar este código puede ser crucial
# para tu sistema operativo
# ¡no lo ejecutes en entornos de producción!
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')