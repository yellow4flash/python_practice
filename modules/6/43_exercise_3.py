# Objetivos

#     Mejorar las habilidades del alumno para operar con archivos en modo lectura.
#     Perfeccionar las habilidades del estudiante para definir y usar excepciones y diccionarios autodefinidos.

# Escenario

# El profesor Jekyll dirige clases con estudiantes y regularmente toma notas en un archivo de texto. Cada línea del archivo contiene 3 elementos: el nombre del alumno, el apellido del alumno y el número de puntos que el alumno recibió durante ciertas clases.

# Los elementos están separados con espacios en blanco. Cada estudiante puede aparecer más de una vez dentro del archivo del profesor Jekyll.

# El archivo puede tener el siguiente aspecto:
# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5

# Tu tarea es escribir un programa que:

#     Pida al usuario el nombre del archivo del profesor Jekyll.
#     Lea el contenido del archivo y cuenta la suma de los puntos recibidos para cada estudiante.
#     Imprima un informe simple (pero ordenado), como este:

# Andrew Cox 	 1.5
# Anna Boleyn 	 15.5
# John Smith 	 7.0

# Nota:

#     Tu programa debe estar completamente protegido contra todas las fallas posibles: la inexistencia del archivo, el vacío del archivo o cualquier falla en los datos de entrada; encontrar cualquier error de datos debería causar la terminación inmediata del programa, y lo erróneo deberá presentarse al usuario.
#     Implementa y usa tu propia jerarquía de excepciones: la presentamos en el editor; la segunda excepción se debe generar cuando se detecta una línea incorrecta y la tercera cuando el archivo fuente existe pero está vacío.

# Tip:

# Emplea un diccionario para almacenar los datos de los estudiantes.
class ExcepcionDatosAlumnos(Exception):
	def __init__(self, data='no hay', mensaje='Una Exception'):
		Exception.__init__(self, mensaje)
		self.data=data

	# def __str__(self):
	# 	return f'{self.datos_alumnos} -> {self.message}'

class LineaErronea(ExcepcionDatosAlumnos):
	def __init__(self, data='text.txt', error_line='La línea no cumple la sintaxis', mensaje='Error en línea'):
		ExcepcionDatosAlumnos.__init__(self, data, mensaje)
		self.error_line = error_line
	# coloca tu código aquí

class ArchivoVacio(ExcepcionDatosAlumnos):
	def __init__(self, data='text.txt', empty_file='El archivo está vacío', mensaje='Archivo vacío'):
		ExcepcionDatosAlumnos.__init__(self, data, mensaje)
		self.empty_file = empty_file

class OrderDates():
	def __init__(self, lista_nombres, lista_calificaciones):
		self.lista_names=lista_nombres
		self.lista_calificaciones=lista_calificaciones
	def listaNamesCalifications(self):
		_listupla=[]
		for i in range(len(self.lista_names)):
			_listupla.append((self.lista_names[i],self.lista_calificaciones[i]))
		return _listupla

# srctext = input('Ingresa el nombre del archivo: ')
try:
	dic = {}
	nombre = ''
	listname = []
	calif = ''
	ccnt = lcnt = 0
	s = open('text.txt', 'rt')
	lines = s.readlines(20)
	if len(lines) == 0:
		raise ArchivoVacio
	while len(lines) != 0:
		for line in lines:
			lcnt += 1
			for ch in line:
				if ch.isalpha():
					if ch==' ':
						continue
					nombre+=ch
				if ch.isspace():
					nombre+=' '
				if not ch.isalpha():
					if ch=='\n':
						continue
					calif+=ch
				# print(ch, end='')
				ccnt += 1
			nombre+=' - '
		lines = s.readlines(10)
	listnametemp = nombre.split('-')
	listname=listnametemp[:-1]
	listcalif = calif.split() 
	listanombre = []

	for i in range(len(listname)):
		listanombre.append(listname[i].strip())
	orderdates=OrderDates(listanombre,listcalif)
	# print(orderdates.listaNamesCalifications())
	lista=orderdates.listaNamesCalifications()
	lista2 = lista[:]
	unique = []
	long = len(lista)
	cont = 0
	for i in range(long):
		if (lista[i][0] not in unique):
			unique.append(lista[i][0])
	calificacion=0
	for i in range(len(unique)):
		for t in range(long):
			if (unique[i] == lista[t][0]):
				if lista[i]==lista[t]:
					calificacion+=float(lista[t][1])
				print(unique[i],lista[t][0],calificacion)


		# print(lista[i][0])
		# if 'Anna Boleyn'==lista2[i][0]:
		# 	cont+=1
		# print(clave,valor)
	# print(cont)		

	# para sumar los numero de las claves repetidas
	# for x in map(lambda x: x * x, lista):
	# 	print(x, end=' ')
	# print()
		
	# print(listuplas)
	# for c in listcalif:
	# 	print(c)
	# print(suma)
	# print(dic)
	# print("\n\nCaracteres en el archivo: ", ccnt)
	# print("Lineas en el archivo:     ", lcnt)
except ArchivoVacio as av:
	print(av,av.empty_file , sep=' : ')
	# s.__exit__
except LineaErronea as le:
	print(le, le.error_line, sep=" : ")
except ExcepcionDatosAlumnos as eda:
	print(eda,eda.data , sep=' : ')
	
s.close()
