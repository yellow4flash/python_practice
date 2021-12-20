# nuevo y práctico mecanismo utilizado por las clases y los objetos de Python: 
# es la forma en que el objeto puede presentarse a si mismo.
class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia
    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)
print(sol.__str__())
#* el método __str__() por defecto devuel la siguente cadena
# <__main__.Estrella object at 0x000001ABB71D7CA0>
#* al crear nuestra propio método __str__() nos imprime lo siguente
# Sol en la Vía Láctea

#? inheritance
# La herencia es una práctica común (en la programación de objetos) de 
# pasar atributos y métodos de la superclase (definida y existente) a una 
# clase recién creada, llamada subclase.
class Vehiculo:
    pass
class VehiculoTerrestre(Vehiculo):
    pass
class VehiculoOruga(VehiculoTerrestre):
    pass
for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()
# Existe una observación importante que hacer: 
# cada clase se considera una subclase de sí misma.
#todo: isinstance(nombreObjeto, nombreClase)
#* isinstance es booleano e informa si un objeto pertenece a determida clase
#* en la alegoría de un pastel te informa cual ha sido la receta utilizada

#* Ser una instancia de una clase significa que el objeto (el pastel) se ha 
#* preparado utilizando una receta contenida en la clase o en una de sus superclases.


#! verificamos todos los pares posibles de clase de objeto para averiguar si los objetos 
#* son instancias de las clases.
miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()
#* los siguentes bucles sirven para 
for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()