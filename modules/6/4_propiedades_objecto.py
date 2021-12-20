class ClaseEjemplo:
    def __init__(self, val = 1):
        self.primera = val

    def setSegunda(self, val):
        self.segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.tercera = 5


# print(objetoEjemplo1.__dict__)
# print(objetoEjemplo2.__dict__)
# print(objetoEjemplo3.__dict__)

#? __dic__ sirve para el siguente concepto
# Debe haber una manera de verificar con seguridad si un objeto específico posee la propiedad
# Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto de propiedades y 
# métodos predefinidos. 

#TODO: el modificar una variable de instancia de cualquier objeto no tiene impacto en todos los objetos restantes. 
#* Las variables de instancia están perfectamente aisladas unas de otras.
""" alt+shift+a:-> coment multilinea """ 

class ClaseEjemplo:
    def __init__(self, val = 1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5


# print(objetoEjemplo1.__dict__)
# print(objetoEjemplo2.__dict__)
# print(objetoEjemplo3.__dict__)
# El nombre ahora es completamente accesible desde fuera de la clase. de la siguente manera
print(objetoEjemplo1._ClaseEjemplo__primera)
# Como puedes ver, hacer que una propiedad sea privada es limitado.
# No funcionará si agregas una variable de instancia fuera del código de clase
#*Variables de clase
#*Variables de istancia
