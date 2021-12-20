class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("__iter__")		
		return self

	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

for i in Fib(10):
	print(i)

# El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse 
# a las reglas impuestas por el contexto de las sentencias for e in. Un objeto conforme 
# al protocolo iterador se llama iterador.

#! El ejemplo muestra una solución donde el objeto iterador es parte de una clase más compleja.
class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter;

object = Class(8)

for i in object: # objeto iterador
	print(i)

#* El protocolo iterador no es difícil de entender y usar, pero también es indiscutible que el 
#* protocolo es bastante inconveniente.

#* La principal molestia que tiene es que necesita guardar el estado de la iteración en las invocaciones 
#* subsequentes de __iter__

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)    # 0, 1, 2, 3, 4
# Hay una limitación importante: dicha función no debe invocarse explícitamente ya que 
# no es una función; es un objeto generador.