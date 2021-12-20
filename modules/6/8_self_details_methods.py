# El nombre self sugiere el propósito del parámetro - identifica el objeto para el cual se invoca el método.
class conClase:
    def metodo(self, par):
        print("método:", par)

obj = conClase()
obj.metodo(1) # al invocar un método no se especifica el parametro self, python lo hará por tí
obj.metodo(2)
obj.metodo(3)

#* El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.
class conClase:
    varia = 2
    def metodo(self):
        print(self.varia, self.var)

obj = conClase()
obj.var = 3
obj.metodo()    # 2 3 //output

#* El parámetro self también se usa para invocar otros métodos desde dentro de la clase.
class conClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro() # se invoca el primer método

obj = conClase()
obj.metodo()
# * conClase
class conClase:
    def __init__(self, valor):
        self.var = valor

obj1 = conClase("objeto")

print(obj1.var)

# Ten en cuenta que el constructor:

    # No puede retornar un valor, ya que está diseñado para devolver un objeto recién creado y nada más.
    # No se puede invocar directamente desde el objeto o desde dentro de la clase (puedes invocar un 
    # constructor desde cualquiera de las superclases del objeto, pero discutiremos esto más adelante).
class conClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._conClase__oculto()

# constructor por parametros
class conClase:
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)
# * hey
class conClase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)