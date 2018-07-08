import numpy as np
    
def createNonogram(n,m):#n and m refers to lenght of matrix
    nonogram=np.zeros(n,m)
    return nonogram

def imprimirNonograma(state):

def leerPistas():
    listaIzquierda     

path = '/users/personal/documents/nonogram.txt'

file = open(path,'r')
    
n = archivo.readline()
m = archivo.readline()
n = int(n)
m = int(m)
    
createNonogram(n,m)
    
rowHints = []
columnHints = []


for i in range(n):
    hints = archivo.readline() #se lee una linea del archivo con pistas 
    elementList = [] 
    for element in hints.split():
        elemntList.add(int(elemnt)) #se transforman los elementos en numero
        rowHints.add(elemntList)
    
for i in range(m):
    hints = archivo.readline() #se lee una linea del archivo con pistas 
    elementList = [] 
    for element in hints.split():
        elemntList.add(int(elemnt)) #se transforman los elementos en numero
        columnHints.add(elemntList)
