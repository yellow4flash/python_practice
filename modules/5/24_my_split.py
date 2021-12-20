def misplit(strng):
#
# coloca tu código aquí
#
    lista = []
    mstring=strng.strip()
    e=0
    if(not mstring.isspace() and not mstring==""): # validación de las cadenas
        for i in range(len(mstring)):
            if(mstring[i]==" "):
                # el indice de espacio viene a ser el valor final de la rodaja
                lista.append(mstring[e:i])
                e=i+1# valor inicial de la rodaja es el indice de los espacios más uno pero debe empezar en cero
        l=mstring.rfind(" ")
        lista.append(mstring[l+1:])
        return lista
    else:
        return []

print(misplit("hola como estas"))
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))