class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
print(objetoEjemplo.b) # acceder a un atributo de objeto no existente provoca una excepción
# Como puedes ver, acceder a un atributo de objeto (clase) no existente provoca una excepción AttributeError.
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

try:
    print(objetoEjemplo.b)
except AttributeError:
    pass # esta instrucción te permite pasar sin realizar operaciones innecesarias

#* Python proporciona una función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica.
#* La función se llama hasattr, y espera que le pasen dos argumentos:

    #* La clase o el objeto que se verifica.
    #* El nombre de la propiedad cuya existencia se debe informar (Nota: debe ser una cadena que contenga el nombre del atributo).
# se usa del siguente modo
if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)