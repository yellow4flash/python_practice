import time
#! The single-responsibility principle (SRP)
#? La composición es el proceso de componer un objeto usando otros objetos diferentes.
class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)

"""
   #* La herencia extiende las capacidades de una clase agregando nuevos componentes y 
   #* modificando los existentes; en otras palabras, la receta completa está contenida dentro 
   #* de la clase misma y todos sus ancestros; el objeto toma todas las pertenencias de la clase y las usa.
   #* La composición proyecta una clase como contenedor capaz de almacenar y usar otros objetos 
   #* (derivados de otras clases) donde cada uno de los objetos implementa una parte del comportamiento 
   #* de una clase.
"""

#! Herencia simple versus herencia múltiple
""" 

#*    Una sola clase de herencia siempre es más simple, segura y fácil de entender y mantener.

#*    La herencia múltiple siempre es arriesgada, ya que tienes muchas más oportunidades de cometer un error 
#*    al identificar estas partes de las superclases que influirán efectivamente en la nueva clase.

    La herencia múltiple puede hacer que la anulación sea extremadamente difícil; además, el emplear 
    la función super() se vuelve ambiguo.

    La herencia múltiple viola el principio de responsabilidad única (mas detalles aquí: 
    https://en.wikipedia.org/wiki/Single_responsibility_principle) ya que forma una nueva clase de dos 
    (o más) clases que no saben nada una de la otra.

    #!Sugerimos encarecidamente la herencia múltiple como la última de todas las posibles soluciones: 
    si realmente necesitas las diferentes funcionalidades que ofrecen las diferentes clases, la 
    composición puede ser una mejor alternativa.

 """