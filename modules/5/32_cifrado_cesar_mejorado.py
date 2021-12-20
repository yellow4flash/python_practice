text = input("Ingresa tu mensaje: ")
display = input("Ingrese un número desplazamiento entre 1 y 25: ")
cifrado = ''
def cesarCompare(char, fl, il):
    code = ord(char) + int(display)
    if code>ord(fl):
        code = ord(il)+(code-ord(fl)-1)       
    return code
for char in text:
    if char.isalpha():
        if char.islower():
            char = char.lower()
            code=cesarCompare(char, 'z', 'a')
        elif char.isupper():
            char = char.upper()
            code=cesarCompare(char, 'Z', 'A')
    else:
        code = ord(char)
    cifrado += chr(code)

print(cifrado)
#*65->A , 90->Z
#*97->a , 122->z


#
# Entrada Muestra:
# abcxyzABCxyz 123
# 2

# Salida Muestra:
# cdezabCDEzab 123

# Entrada Muestra:
# The die is cast
# 25

# Salida Muestra:
# Sgd chd hr bzrs

# char = char.upper()#primero se asegura de convertir en mayuscual
# code = ord(char) + 1 # luego obtiene el punto de código sumado en uno
# if code > ord('Z'):
#     code = ord('A')
# cifrado += chr(code)