class MyZeroDivisionError(ZeroDivisionError):	
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("peores noticias")
	else:		
		raise ZeroDivisionError("malas noticias")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('División entre cero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('Mi división entre cero')
	except ZeroDivisionError:
		print('División entre cero original')

""" 
La función doTheDivision() lanza una excepción MyZeroDivisionError o 
ZeroDivisionError, dependiendo del valor del argumento. 

 """

#  La función se invoca cuatro veces en total, mientras que las dos primeras 
# invocaciones se manejan utilizando solo una rama except (la más general), las 
# dos últimas invocan dos ramas diferentes, capaces de distinguir las excepciones 
# (no lo olvides: el orden de las ramas hace una diferencia fundamental).

#! crear mi propia excepción parte 2
class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(mensaje)
        self.pizza = pizza	


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError._init__(self, pizza, mensaje)
        self.queso = queso

""" 
    Uno que especifica una pizza como tema del proceso.
    Otro que contiene una descripción más o menos precisa del problema.

 """

""" 
La excepción DemasiadoQuesoError necesita más información que la excepción regular PizzaError, 
así que lo agregamos al constructor, el nombre queso es entonces almacenado para su posterior procesamiento. 
"""
#! Eliminaremos la debilidad agregando parametros opcionales
class PizzaError(Exception):
    def __init__(self, pizza='desconocida', mensaje=''):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza='desconocida', queso='>100', mensaje=''):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def hacerPizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError
	if queso > 100:
		raise DemasiadoQuesoError
	print("¡Pizza lista!")
#? con parametros
#* def makePizza(pizza, queso):
#* 	if pizza not in ['margherita', 'capricciosa', 'calzone']:
#* 		raise PizzaError(pizza, "no hay tal pizza en el menú")
#* 	if queso > 100:
#* 		raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
#* 	print("¡Pizza lista!")



for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		hacerPizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)