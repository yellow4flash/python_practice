class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0
    def push(self, val):
        self.__sum += val
        Pila.push(self, val) #* invocamos el método push de la superclase
    def getSuma(self):
        return self.__sum
    def pop(self):
        val = Pila.pop(self) #* invocamos el método pop
        self.__sum-=val
        return val
# ingresa código aquí
objSuma = SumarPila()
objSuma.push(2)
objSuma.push(3)

for i in range(5):
    objSuma.push(i)

print(objSuma.getSuma())

for i in range(5):
    print(objSuma.pop())