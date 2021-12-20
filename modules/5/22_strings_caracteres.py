#Candenas y carácteres->aveces se gana, aveces se aprende
#?El denominado ASCII 
#*(por sus siglas en íngles American Standard Code for Information Interchange). 
#*El Código Estándar Americano para Intercambio de Información es el más utilizado
#? I18N internacionalización

#?Un punto de código es un numero que compone un caracter. 
# *Por ejemplo, 32 es un punto de código que compone un espacio en codificación ASCII. 
# *Podemos decir que el código ASCII estándar consta de 128 puntos de código.

#?paginas de punto de código
#*Por ejemplo, el punto de código 200 forma una Č 
# *(una letra usada por algunas lenguas eslavas) 
# *cuando lo utiliza la página de códigos ISO/IEC 8859-2, pero forma un Ш 
# *(una letra cirílica) cuando es usado por la página de códigos ISO/IEC 8859-5.

#? UNICODE
#*Unicode asigna caracteres únicos (letras, guiones, ideogramas, etc.) 
#* a más de un millón de puntos de código.

#? UCS-4
#*El nombre viene de Universal Character Set (Conjunto de Caracteres Universales).
#*UCS-4 emplea 32 bits (cuatro bytes) para almacenar cada caracter, y el código 
# *es solo el número único de los puntos de código Unicode

#?UTF-8
#*El nombre se deriva de Unicode Transformation Format (Formato de Transformación Unicode).
#*El concepto es muy inteligente. UTF-8 emplea tantos bits para cada uno de los puntos de 
# *código como realmente necesita para representarlos.

#?Python 3 es totalmente compatible con Unicode y UTF-8:

#* -> Puedes usar caracteres codificados Unicode / UTF-8 para nombrar variables y otras entidades.
#* -> Puedes usarlos durante todas las entradas y salidas.
#* Esto significa que Python3 está completamente Internacionalizado.
print('I\'m')#carácte de escape
#\n carácter de salto de línea

#todo:  La capacidad de usar el mismo operador en tipos de datos completamente 
#todo: diferentes (como números o cadenas) se llama overloading - sobrecarga 
#todo: (debido a que el operador está sobrecargado con diferentes tareas).
str1='hi'
str2='there'
# print(str1 + str2)
# print(str2 + str1)
# print(5 * 'a')
# print('b' * 4)
# la función ord('α') -> muestra los puntos de código de un caracter
print(ord('α'))
# Demostrando la función chr()
# la función chr(945) -> muestra el caracter al enviar un punto de código como parametro
print(chr(97))
print(chr(945))
#! experimentos
    #chr(ord(x)) == x -> el parametro x es igual a la salida
    #ord(chr(x)) == x -> el parametro x es igual a la salida

# Rodajas o rebanadas
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])#* el 2 es como el salto de linea(en este caso step o el número de pasos)
#* que debe dar en la cadena para tomar el elemento
print(alpha[1::2])#* empieza del indice 1 y va de dos en dos(b-e-g)

#* in and not in tambien se utilizan
#! Operaciones con cadenas
#* Es posible que desees preguntar si el crear una nueva copia de una cadena cada vez que 
#* se modifica su contenido empeora la efectividad del código.
#* Sí lo hace. Un poco. Sin embargo, no es un problema en absoluto
#! ->
alfabeto = "bcdefghijklmnopqrstuvwxy"

alfabeto = "a" + alfabeto
alfabeto = alfabeto + "z"

print(alfabeto)

#? la funcion min() en una cadena
#?la función max(): muestra el elemento máximo de una cadena

# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ")) #todo Output: A -> esto depende del orden en la tabla ASCII

# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')# toma el espacion como elemento mínimo de la cadena

t = [0, 1, 2]
print(min(t))