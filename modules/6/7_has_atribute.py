class ClaseEjemplo:
    a = 1
    def __init__(self):
        self.b = 2 # atributo objeto, no se lee como atributo de clase(hasattr(ClaseEjemplo, 'b')=>False)

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'b'))  # True
print(hasattr(objetoEjemplo, 'a'))  # True
print(hasattr(ClaseEjemplo, 'b'))   # False
print(hasattr(ClaseEjemplo, 'a'))   # True