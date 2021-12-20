# Nota: el atributo __name__ está ausente del objeto - existe solo dentro de las clases.
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)
# Si deseas encontrar la clase de un objeto en particular, puedes usar una función llamada type(), 
# la cual es capaz (entre otras cosas) de encontrar una clase que se haya utilizado para crear 
# instancias de cualquier objeto.
#! Nota: algo como esto print(obj.__name__) causará un error.
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__) # __main__
#* __main__ indica que no es un nódulo y que se está ejecutando en ese mismo archivo
#? __bases__ es una tupla. La tupla contiene clases (no nombres de clases) que son 
#? superclases directas para la clase.

class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperUno) #* ( object ) -> está clase no tiene superclase por lo que apunta a un objeto
printBases(SuperDos) #* ( object ) -> like this too
printBases(Sub)      #* ( SuperUno SuperDos ) esta tiene dos superclase SuperUno, SuperDos respectivamente
#* propierties
#? getattr() 
#* toma dos argumentos: un objeto y su nombre de propiedad (como una cadena) y 
#* devuelve el valor del atributo actual.
#? isinstance(val, int)
#* comprueba si el valor es de tipo entero, emplea la función 
#? setattr(obj, name, val + 1);
#* la función toma tres argumentos: un objeto, el nombre de la 
#* propiedad (como una cadena) y el nuevo valor de la propiedad.
class MiClase:
    pass

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3 # output: 4
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)