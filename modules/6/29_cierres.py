# cierres es una técnica que permite almacenar valores a pesar de que el contexto 
# en el que se crearon ya no existe.
def exterior(par):
	loc = par
	def interior():
		return loc
	return interior #! acá se retorna una función

var = 1
fun = exterior(var)
print(fun()) #! por lo que acá se imprime  en manera de función

# La función devuelta durante la invocación de exterior() es un cierre.

# la función congelada contiene su entorno completo, incluido el estado de 
# todas las variables locales, lo que también significa que el valor de loc se retiene 
# con éxito, aunque exterior() ya ha dejado de existir.
def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2) # primer cierre para elebar un elemento al cuadrado
fcub = crearcierre(3) # segundo cierre para elebar un elemento al cubo
for i in range(5):
	print(i, fsqr(i), fcub(i))