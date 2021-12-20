
#*una forma de usar assert: si las excepciones y validación de datos
#*son como conducir con cuidado
#*assert representa el papel de una bolsa de aire
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0     #assert se ejecuta si no se cumple la condición

x = math.sqrt(x)

print(x)