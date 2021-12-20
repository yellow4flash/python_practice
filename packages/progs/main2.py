
#* importar un paquete
from sys import path
#?ruta relativa
#path.append('..\\packages')#TODO: esta importación falla, por lo que da una exepción
# No module named 'extra'

#?ruta absoluta
path.append('D:\\SoftwareDev\\Python\\course-cisco-python\\packages\\packages')
#! import extra.iota
from extra.iota import FunI

print(FunI())
#! print(path,end="\t")