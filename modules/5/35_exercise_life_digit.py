date = input('Ingrese su fecha de cumpleaños (1999-08-01): ')
def sumarDigits(numbers):
    suma=0
    for i in numbers:
        if not i.isdigit():
            continue
        suma+=int(i)
    return suma
sumatoria=sumarDigits(date) #se agrega la sumatoria de la fecha a sumatorua
cantDigits=len(str(sumatoria))#obetenemos la longitud de sumatoria
while cantDigits>1: #comprobamos si la longitud es mayou a 1 y procedemos a sumar
    sumatoria = sumarDigits(str(sumatoria))
    cantDigits=len(str(sumarDigits(str(sumatoria))))
print(sumatoria)