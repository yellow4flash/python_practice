#* Demonstrando el método index()
#* el método index muestra el número de indice del elemento, comenzando 
#* desde 0 y el total de elementos con decremento 1
print("aAbByYzZaA".index("b"))

# Demostrando la función list()
#* el método list convierte una cadena u otro iterable como tuplas, diccionarios en una lista
print(list("abcabc"))

# Demostrando el método count()
#* el método count cuenta cuantas veces aparece el elemento en la cadena
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demostración del método capitalize()
#* el método capitalize() convierte la primera letra(índice 0) en mayúscula y 
#* las demás en minúsculas

print('aBcD'.capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Demostración del método center()
#* genera espacios en blanco para centrar una cadena
print('[' + 'alfa'.center(10) + ']')
#* método center con segundo argumento
print('[' + 'gamma'.center(20, '*') + ']')

#? Demostración del método endswith()
#* determina si una cadena termina en el paramentro especificado, devuelve un 
#* booleano
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
#? Demostración del método startswith()
#*comprueba si una cadena dada comienza con la subcadena especificada. return bool
print("omega".startswith("meg"))
print("omega".startswith("om"))

#? Demostración del método find()
#* muestra el índice de la primera letra del parametro, en la cadena evaluada
#* El método find() es similar al método index(), el cual ya conoces - busca una 
#* subcadena y devuelve el índice de la primera aparición de esta subcadena
#* es más seguro que index() y solo se usa en cadenas
print("Eta".find("ta"))
print("Eta".find("mma"))
#* Nota: no se debe de emplear find() si deseas verificar si un solo carácter 
#* aparece dentro de una cadena - el operador in será significativamente más rápido.
# ! segunda variante
# * el segundo argumento se usa para decirle a find() desde que índice quiere que empiece
print('kappa'.find('a', 2))
# ! tercer variante
# * el tercer argumento apunta al primer índice que no se tendrá en cuenta durante la búsqueda 
# * el ta es el limite de indices a tomar por find(), no lo toca
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#? Demostración del método the isalnum()
#* El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y 
#* devuelve True (verdadero) o False (falso) de acuerdo al resultado.
# *útil para validar el campo (usuario)
print('lambda30'.isalnum()) #*True
print('lambda'.isalnum())   #*True
print('30'.isalnum())       #*True
print('@'.isalnum())        #*False
print('lambda_30'.isalnum())#*False
print(''.isalnum())         #*False
print('ΑβΓδ'.isalnum())     #*True

#? Ejemplo 1: Demostración del método isapha()
#*El método isalpha() es más especializado, se interesa en letras solamente.
print("Moooo".isalpha())    #*True
print('Mu40'.isalpha())     #*False

#? Ejemplo 2: Demostración del método isdigit()
#*Al contrario, el método isdigit() busca sólo dígitos - cualquier otra cosa produce False (falso) como resultado.
print('2018'.isdigit())     #*True
print("Año2019".isdigit())  #*False

#? Ejemplo 1: Demostración del método islower()
# *El método islower() es una variante de isalpha() - solo acepta letras minúsculas.
print("Moooo".islower())    #*False
print('moooo'.islower())    #*True

#? Ejemplo 2: Demostración del método isspace()
#*El método isspace() identifica espacios en blanco solamente - no tiene 
#*en cuenta ningún otro caracter (el resultado es entonces False)
print(' \n '.isspace())             #*True
print(" ".isspace())                #*True
print("mooo mooo mooo".isspace())   #*False

#? Ejemplo 3: Demostración del método isupper() 
#*El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.
print("Moooo".isupper())    #*False
print('moooo'.isupper())    #*False
print('MOOOO'.isupper())    #*True

#? Demostración del método join()
#* El método join() tiene como parametro una lista de cadenas
#* y se invoca desde una cadena que se toma como separador para las cadenas 
#* dentro de la lista
print(",".join(["omicron", "pi", "rho"]))

#? Demostración del método lower()
#* El método lower() genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus 
#* equivalentes en minúsculas, y devuelve la cadena como resultado. Nuevamente, la cadena original permanece intacta.
print("SiGmA=60".lower())       #*sigma=60
print("SiGm_A01-Ywer".lower())  #*sigm_a01-ywer

#? Demostración del método the lstrip()
#* El método sin parámetros lstrip() devuelve una cadena recién creada formada a partir de la original 
#* eliminando todos los espacios en blanco iniciales.
print("[" + " tau ".lstrip() + "]") #![tau ]
#* Un parametro en lstrip() elimina todos los caracteres incluidos en el argumento
print("www.cisco.com".lstrip("w.")) #!cisco.com
print("pythoninstitute.org".lstrip(".org")) #* no elimina el .org porque no está al inicio
#? Demostración del método rstrip()
#* hace lo mismo que lstrip() pero empieza en el orden opuesto
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
#? Demostración del método strip() 
#* crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
print("[" + "   aleph   ".strip() + "]")    #* [aleph]

#? Demostración del método replace()
#* todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#* emplea un tercer argumento (un número) para limitar el número de reemplazos.
print("This is it!".replace("is", "are", 1))    #*Thare is it!  -> solo una vez
print("This is it!".replace("is", "are", 2))    #*Thare are it! -> 2 veces

#? Demostración del método rfind()
#* hace lo mismo que find() pero con la diferencia que se evalua de derecha a izquerda
#* r viene de reserva
print("tau tau tau".rfind("ta"))        #*8
print("tau tau tau".rfind("ta", 9))     #*-1
print("tau tau tau".rfind("ta", 3, 9))  #*4

#* Demostración del método split()
#* crea una lista a partir de una cadena(esta con subcadenas que se separen con espacios en blanco)
#* split() asume que la cadena esta separa por espacios en blanco
print("phi       chi\npsi".split())
#! la operación inversa a split() se realiza con join() 

#? Demostración del método swapcase()
#* los caracteres en mayúscula se convierten en minúsculas y viceversa.
print("Yo sé que no sé nada.".swapcase())   #* yO SÉ QUE NO SÉ NADA.

#? Demostración del método title()
#* cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
print("Yo sé que no sé nada. Parte 1.".title()) #* Yo Sé Que No Sé Nada. Parte 1.

#? Demostración del método upper()
#* reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas.
print("Yo sé que no sé nada. Parte 2.".upper())
