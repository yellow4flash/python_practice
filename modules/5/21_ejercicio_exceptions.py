def readint(prompt, min, max):
    try:
        num=int(input(prompt))
        if(not(num>=min) or not(num<=max)):
            raise Exception# creamos una excepción
        else:
            return num
    except ValueError:
        print("Este dato es invalido, ingrese otro")
        return readint(prompt, min, max)
    except:
            print("Error: el valor no está dentro del rango permitido","(",min,"..",max,")")
            return readint(prompt, min, max)

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)