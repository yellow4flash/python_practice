text = input("Ingrese el políndromo: ")

poli=''
poliI=''
count=0
try:
    if text=='':
        raise
    for l in text:
        if not l.isalpha():
            if l.isspace():
                continue
            else:
                raise
        poli+=l
    for i in range(len(text)):
        count-=1
        if not text[count].isalpha():
            continue
        poliI+=text[count]
    if(poli.capitalize()==poliI.capitalize()):
        print('Es un políndromo')
    else:
        print('No es un políndromo')
except:
    print('Ingresó un caracter no válido, favor de ingresar solo texto')
