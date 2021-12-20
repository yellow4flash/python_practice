#Pilas
#* Una pila es una estructura desarrollada para almacenar datos de una manera muy específica..
#* El nombre alternativo para una pila (pero solo en la terminología de TI) es 
#? UEPS (LIFO son sus siglas en íngles)
#todo: Último en Entrar - Primero en Salir (Last In - First Out).
#? Pila al estilo procedimental (procedural approach)
pila = []
def push(val):
    pila.append(val)

def pop():
    val = pila[-1]
    del pila[-1]
    return val

# push(3)
# push(2)
# push(1)

# print(pop())
# print(pop())
# print(pop())

#? Encapsulamiento
#* La capacidad de ocultar (proteger) los valores seleccionados contra el acceso no autorizado 
#* se llama encapsulamiento; no se puede acceder a los valores encapsulados ni modificarlos si 
#* deseas utilizarlos exclusivamente.

#? Pila con el enfoque orientado a objetos (objective approach)
class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        print("¡Hola!")

objetoPila = Pila()    # instanciando el objeto

#todo: Nota: el parámetro obligatorio generalmente se denomina self - es solo una sugerencía, 
#todo: pero deberías seguirla - simplifica el proceso de lectura y comprensión de tu código.
class Pila:
    def __init__(self):
        self.listaPila = [] # se agrega la propiedad al nuevo objeto

objetoPila = Pila()
# print(len(objetoPila.listaPila))
#? Encapsulamiento
#* Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), 
#* se vuelve privado - esto significa que solo se puede acceder desde la clase.
class Pila:
    def __init__(self):
        self.__listaPila = []#* se encapsula la variable para ser reconocida solo en la clase
    def push(self, val):
        self.__listaPila.append(val)
    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()
objetoPila2 = Pila() #* se crea una segunda pila y se utiliza con los mismos métodos
objetoPila.push(1)
objetoPila.push(2)#metodo push desde afuera no requiere el parametro self
objetoPila.push(3)#lifo
objetoPila2.push(5)
objetoPila2.push(4)#lifo
print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila2.pop())

#? Se debe señalar al objeto (la instancia de la clase) que debe ser inicializado por el constructor; 
#* es por eso que se debe especificar el argumento y utilizar la variable self aquí; recuerda: invocar 
#* cualquier método (incluidos los constructores) desde fuera de la clase nunca requiere colocar el argumento 
#* self en la lista de argumentos - invocar un método desde dentro de la clase exige el uso explícito del 
#* argumento self, y tiene que ser el primero en la lista.
class SumarPila(Pila):
    def __init__(self):
        super().__init__()
        self.__sum=0

#todo: generalmente es una práctica recomendada invocar al constructor de la superclase 
#* antes de cualquier otra inicialización que desees realizar dentro de la subclase. 
#* Esta es la regla que hemos seguido en el código.