listaP = [
    [False,False,True,False,True,False,False,True,False,True,False,False,True],
    [True,True,True,False,True,True,True,True,True,False,True,True,True],
    [True,True,True,False,True,True,True,True,False,True,True,True,True],
    [True,False,True,True,True,True,True,True,False,True,False,False,True],
    [True,True,True,True,False,True,True,True,False,True,True,True,True],
    [True,True,True,True,False,True,True,True,True,True,True,True,True],
    [True,True,True,False,True,False,False,True,False,True,False,False,True],
    [True,True,True,True,True,True,True,True,True,True,True,True,True],
    [True,True,True,True,True,True,True,True,False,True,True,True,True],
    [True,True,True,True,True,True,False,True,True,True,True,True,True],
]
def enter(num):
    if(num==1):
        return listaP[0]
    elif(num==2):
        return listaP[1]
    elif(num==3):
        return listaP[2]
    elif(num==4):
        return listaP[3]
    elif(num==5):
        return listaP[4]
    elif(num==6):
        return listaP[5]
    elif(num==7):
        return listaP[6]
    elif(num==8):
        return listaP[7]
    elif(num==9):
        return listaP[8]
    elif(num==0):
        return listaP[9]
    else:
        print('Este no es un número del 0 al 9')

numero = input('Ingrese números del 0 al 9: ')
s=' '

# función para formar el patrón según los número ingresados
def patterForm(num):
    listOut = enter(num)
    aL = "#" if listOut[0] else s
    bL = "#" if listOut[1] else s
    cL = "#" if listOut[2] else s
    dL = "#" if listOut[3] else s
    eL = "#" if listOut[4] else s
    fL = "#" if listOut[5] else s
    gL = "#" if listOut[6] else s
    hL = "#" if listOut[7] else s
    iL = "#" if listOut[8] else s
    jL = "#" if listOut[9] else s
    kL = "#" if listOut[10] else s
    lL = "#" if listOut[11] else s
    mL = "#" if listOut[12] else s
    pattern = [
        [aL, bL, cL],
        [dL, s, eL],
        [fL, gL, hL],
        [iL, s, jL],
        [kL, lL, mL]
    ]
    return pattern

        # return show

def printHash(pattern):
    tupatt=''
    for p in range(len(pattern)):
        tupatt += "\n"+" ".join(pattern[p])
    return tupatt

def pattern():
    for i in range(len(numero)):
        pattern = patterForm(int(numero[i]))
        # función para mostrar los números en el display
        print(printHash(pattern))
    # return pattern


pattern()

# print( ' '+printHash(pattern())+'\f', end=" ")






# n=4
# for i in range(n+1):
#     print(' '*(n)+'* '*i)
#     n-=1


    # print(*('{} {} {} '.format(*r)*(i+1) for r in pattern), sep='\n')
    #* entendiendo el metodo format()
    # print('{0} {1} {2}'.format(p,p,p) )