firstString = input('Ingresa la palabra a encontrar: ').lower()
secondString = input('Ingresa el bosque de letras: ').lower()

finded=''
index = 0
for letter in firstString:
    index=secondString.find(letter,index)
    finded+=secondString[index]
# print(finded)
if finded!=firstString:
    print('No')
else:
    print('Si')

# donor
# Nabucodonosor