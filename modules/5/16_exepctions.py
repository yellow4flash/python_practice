#*Exepctions -Reglas
#*Si uno de los bloques except es ejecutado, ningún otro lo será.
#*Si ninguno de los bloques except especificados coincide con la excepción planteada, la excepción permanece sin manejar
#? ArithmeticError: es una exepción que incluye a ZeroDivisionError
# por lo tanto es ma general
try:
    y = 1 / 0
except ArithmeticError: 
    print("Uuuppsss...")

print("FIN.")

#* el codigo muestra una forma extravagante
#* de dejar el bucle
#? se muestra una forma de manejar una exepción
lista = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lista[ix])
        ix += 1
    except IndexError:
        doit = False

print('Listo')