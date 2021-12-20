class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())

# La entidad definida después (en el sentido de herencia) 
# anula la misma entidad definida anteriormente.
class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2:
    var = 200
    def fun(self):
        return 201

class Nivel3(Nivel2):
    pass

obj = Nivel3()

print(obj.var, obj.fun()) # es por eso 200 201
#  overriding (anulación).