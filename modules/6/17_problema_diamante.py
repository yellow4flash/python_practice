#problema de diamantes

"""
  #  Existe la superclase superior nombrada A.
  #  Aquí hay dos subclases derivadas de A - B y C.
  #  Y también está la subclase inferior llamada D, derivada de B y C (o C y B, ya que estas 
  #  dos variantes significan cosas diferentes en Python).

"""
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A, B):
    pass

d = D()

# Cannot create a consistent method resolution
# order (MRO) for bases B, A

# Donde MRO significa Method Resolution Order. Este es el algoritmo que Python utiliza 
# para buscar el árbol de herencia y encontrar los métodos necesarios.