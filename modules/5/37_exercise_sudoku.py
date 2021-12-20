from math import pi

textRange=[
'295743861',
'431865927',
'876192543',
'387459216',
'612387495',
'549216738',
'763524189',
'928671354',
'154938672'
]
textRangeT2=[
'195743862',
'431865927',
'876192543',
'387459216',
'612387495',
'549216738',
'763524189',
'928671354',
'254938671'
]
# textRange=[[],[],[],[],[],[],[],[],[]]
# for i in range(9):
#     textRange[i] = input("Ingrese las filas del sudoku: ")

def displayBoard(board):
    for item in board:
            print("+--"*9,"+")
            print(f"| {item[0]}|",f"{item[1]}|",f"{item[2]}|",f"{item[3]}|",f"{item[4]}|",f"{item[5]}|",f"{item[6]}|",f"{item[7]}|",f"{item[8]} |")
            print("+--"*9,"*")
# displayBoard(boardTest1)

def getColumn(board, nCol):
    column=[]
    for cadena in board:
        column.append(cadena[nCol])
    return column
def getRows(board,nRows):
    return list(board[nRows])
columns=[]
rows=[]
bloques=[]
for i in range(9):
    columns.append(getColumn(board=textRange, nCol=i))
    rows.append(getRows(board=textRange,nRows=i))
# creat mmatriz 3x3
def getMatriz3x3(iCol,fCol,iRow,fRow):
    matriz3x3=[]
    for i in range(iCol,fCol):
        matriz3x3.append(rows[i][iRow:fRow])
    return matriz3x3

def matrizInList():
    count=0
    itRow=0
    matrizList=[]
    for i in range(9):
        matrizList.append(getMatriz3x3(count, count+3, itRow,itRow+3))
        count+=3
        if count==9:
            count=0
            itRow+=3
    return matrizList
matrisList=matrizInList()
def getMatriz(board,nMatriz):
    obten=[]
    for i in range(3):
        for e in range(3):
            obten.append(board[nMatriz][i][e])
    return obten

for i in range(9):
    bloques.append(getMatriz(board=matrisList,nMatriz=i))

def ExistRepeatNumberIn(linea, nCol):
    equalNumber=False
    for i in range(9):
        if linea[nCol].count(linea[nCol][i])>1:
            equalNumber=True
    return equalNumber

repeat=False
for i in range(9):
    if ExistRepeatNumberIn(columns,i):
        repeat=True
    if ExistRepeatNumberIn(rows,i):
        repeat=True
    if ExistRepeatNumberIn(bloques,i):
        repeat=True
if repeat:
    print('No')
else:
    print('Yes')
