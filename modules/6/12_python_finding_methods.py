class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        # Super.__init__(self, nombre)
        super().__init__(nombre)
#? super(), 
#* la cual accede a la superclase sin necesidad de conocer su nombre
#todo: Puedes usar este mecanismo no solo para invocar al constructor de la superclase, 
#* pero también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.
obj = Sub("Andy")
obj1 = Super('Budy')
print(obj)
print(obj1)
#* Como no existe el método __str__() dentro de la clase Sub
#* Esto significa que el método __str__() ha sido heredado por la clase Sub.
# Probando propiedades: variables de clase
class Super:
    supVar = 1
class Sub(Super):
    subVar = 2
obj = Sub()
print(obj.subVar)   #2
print(obj.supVar)   #1
#todo: Ambas variables son visibles dentro del objeto de clase Sub

# Probando propiedades: variables de instancia
class Super:
    def __init__(self):
        self.supVar = 11
class Sub(Super):
    def __init__(self):
        super().__init__() #omitirlo da una exception
        self.subVar = 12
obj = Sub()
print(obj.subVar)
print(obj.supVar)
#! La existencia de la variable supVar obviamente está condicionada por la invocación del 
#* constructor de la clase Super. Omitirlo daría como resultado la ausencia de la variable en el objeto creado 

#! Cuando intentes acceder a una entidad de cualquier objeto, Python intentará (en este orden):
# *    Encontrarla dentro del objeto mismo.
# *    Encontrarla en todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
#! Si ambos intentos fallan, una excepción (AttributeError) será lanzada