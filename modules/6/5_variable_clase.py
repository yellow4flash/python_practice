class ClaseEjemplo:
    contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

# print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
# print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
# print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)
#* Las variables de clase no se muestran en el diccionario de un objeto __dict__ 
#* Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).
class ClaseEjemplo:
    __contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.__contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)
    
print(objetoEjemplo1.__dict__, objetoEjemplo1._ClaseEjemplo__contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2._ClaseEjemplo__contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3._ClaseEjemplo__contador)

# output

# {'_ClaseEjemplo__primera': 1} 3 

# {'_ClaseEjemplo__primera': 2} 3 

# {'_ClaseEjemplo__primera': 4} 3
class ClaseEjemplo:
    varia = 1 #variable de clase
    def __init__(self, val):
        self.varia=val         # variable de instancia
        varia=val              # variable local del método
        ClaseEjemplo.varia=val # usando la variable de clase
        

print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)
#* Nota que el __dict__ del objeto está vacío - el objeto no tiene variables de instancia.