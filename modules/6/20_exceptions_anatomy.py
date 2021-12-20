""" 
La clase BaseException introduce una propiedad llamada args. 
Es una tupla diseñada para reunir todos los argumentos pasados al constructor de la clase.
 """

def printargs(args):
	lng = len(args)
	if lng == 0:
		print("")
	elif lng == 1:
		print(args[0])
	else:
		print(str(args))

try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=' : ' ,end=' : ')
	printargs(e.args)

try:
	raise Exception("mi excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

try:
	raise Exception("mi", "excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

"""
    El segundo y el tercer caso pueden parecer un poco extraños a primera vista, 
    pero no hay nada extraño, son solo las invocaciones del constructor. En la segunda 
    sentencia raise, el constructor se invoca con un argumento, y en el tercero, con dos.
 """