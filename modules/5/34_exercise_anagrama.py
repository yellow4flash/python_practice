text = input("Enter the first word of the anagrama: ").lower()
textSecond = input("Enter the Second word of the anagrama: ").lower()

try:
    existDifference=False
    for i in range(len(text)):
            if text[i].isalpha():
                if text[i] not in textSecond:
                    existDifference=True
                # si la letra de la cadena 1 es igual a la letra de la segunda cadena
                # y la cantidad de letras en la primera cadena difiere de la segunda
                if text[i]==textSecond[i] and text.count(text[i]) != textSecond.count(textSecond[i]):
                    existDifference=True
            else:
                continue
    if existDifference:
        print('No es un anagrama ') 
    else:
        print('Es un anagrama')
except IndexError:
    print('Una palabra es más grande que otra, no puede ser una anagrama')