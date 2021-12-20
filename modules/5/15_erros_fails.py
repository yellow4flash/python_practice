#Cualquier cosa que pueda salir mal, saldrá mal

#?Expepciones
#* python tiene herramientas que le permiten observar, identicar y manejar las exepciones
#! ValueError: math domain error
try:
    value= 1/0
    print(value)
except ZeroDivisionError:
    print('Error al dividir entre cero')
except:
    print('ingresa valores válidos')


#* se omite silenciosamente la instrucción print("2") depues que ocurre la exepción
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")

#* variante avanzada de try - except
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")
