from random import randrange # se importa del modulo externo random

board = [
    [1,2,3],[4,5,6],[7,8,9]
    ]
def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    for item in board:
        print("+-----"*3,"+")
        print("|     "*3,"|")
        print(f"|  {item[0]}  |",f" {item[1]}  |",f"  {item[2]}  |")
        print("|     "*3,"|")
        print("+-----"*3,"*")
            

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    inputSpace=int(input('Ingrese tu movimiento: '))
    # lista de opciones disponibles
    listaOpt = listaOptDisponible(board)
    # lista de espacios dispinibles
    listaTuplas=MakeListOfFreeFields(board)
    # se busca el número ingresado en la lista de disponibilidad
    if inputSpace in listaOpt:
        # un ciclo para comparar la opcion del usuario con los espacios aun disponibles
        for i in range(len(listaTuplas)):
            # se compara el valor ingresado conun valor de la lista
            if inputSpace==listaOpt[i]:
                # se descompone la tupla de pares en dos variables
                a,b=listaTuplas[i]
                # se agrega al tablero con el campo indicado el valor 'O' que representa al usuario
                board[a][b]='O'
    else:
        print('Ese espacio está ocupado, ingrese otro')
        # en caso de que el número no se encuantre en la lista de disponibles, se vuelve a ejecutar la función
        return EnterMove(board)

    


def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    listaAvailable=[]
    listaTemp=[]
    listaTuplas=[]
    for item in board:
        listaTemp=[n for n in item if not n=='X' and not n=='O'] # identifica los campos que estan disponibles
        listaAvailable.append(listaTemp)
    for opt in listaAvailable:
        for e in opt:
            if e==1:
                tup1=0,0
                listaTuplas.append(tup1)
            elif e==2:
                tup2=0,1
                listaTuplas.append(tup2)
            elif e==3:
                tup3=0,2
                listaTuplas.append(tup3)
            elif e==4:
                tup4=1,0
                listaTuplas.append(tup4)
            elif e==5:
                tup5=1,1
                listaTuplas.append(tup5)
            elif e==6:
                tup6=1,2
                listaTuplas.append(tup6)
            elif e==7:
                tup7=2,0
                listaTuplas.append(tup7)
            elif e==8:
                tup8=2,1
                listaTuplas.append(tup8)
            elif e==9:
                tup9=2,2
                listaTuplas.append(tup9)
            else:
                print('Opción no válida')
    
    return listaTuplas

        

def VictoryFor(board, sign='O'):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
#rows
    if (board[0][0]==board[0][1]==board[0][2]):
        sign=board[0][1],board[0][0],board[0][2]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
    elif(board[1][0]==board[1][1]==board[1][2]==sign):
        sign=board[1][0],board[1][1],board[1][2]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
    elif(board[2][0]==board[2][1]==board[2][2]):
        sign=board[2][0],board[2][1],board[2][2]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
#columns   
    elif(board[0][0]==board[1][0]==board[2][0]):
        sign=board[0][0],board[1][0],board[2][0]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
    elif(board[0][1]==board[1][1]==board[2][1]):
        sign=board[0][1],board[1][1],board[2][1]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
    elif(board[0][2]==board[1][2]==board[2][2]):
        sign=board[0][2],board[1][2],board[2][2]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
#diagonal
    elif(board[0][0]==board[1][1]==board[2][2]):
        sign=board[0][0],board[1][1],board[2][2]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
    elif(board[0][2]==board[1][1]==board[2][0]):
        sign=board[0][2],board[1][1],board[2][0]
        return 'Has perdido' if 'X' in sign else 'Has ganado'
    else:
        return 'Continua'

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    inputSpace=randrange(1,9)
    # lista de opciones disponibles
    listaOpt = listaOptDisponible(board)
    listaTuplas=MakeListOfFreeFields(board)
    if inputSpace in listaOpt:
        for i in range(len(listaTuplas)):
            if inputSpace==listaOpt[i]:
                a,b=listaTuplas[i]
                board[a][b]='X'
    else:
        return DrawMove(board)

def listaOptDisponible(board):
    #last
    listaTuplas=MakeListOfFreeFields(board)
    listaTempBoard=[]
    listaBoard=[]
    for i in range(len(listaTuplas)):
        a,b=listaTuplas[i]
        listaTempBoard=board[a][b]
        listaBoard.append(listaTempBoard)
    return listaBoard
    
# se asigna la X al espacio 5 primer movimiento por la maquina
board[1][1]='X'
# DisplayBoard(board)
word = ''
while (not word=='Has ganado' and not word=='Has perdido'):
    DisplayBoard(board)
    EnterMove(board)
    DrawMove(board)
    VictoryFor(board)
    word=VictoryFor(board)
DisplayBoard(board)
print(VictoryFor(board))
