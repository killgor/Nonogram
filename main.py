import numpy as np

path = '/users/personal/documents/nonogram.txt'

file = open(path,'r')

def readFile(file):#reads the input from file nonogram.txt
    n = archivo.readline()
    m = archivo.readline()
    n = int(n)
    m = int(m)
    
    createNonogram(n,m)
    
    rowHints = np.array(n,10)
    columnHints = np.array(m,10)
    
    
    for i in range(n):
        
    
    for i in range(m):
        
    

def createNonogram(n,m):#n and m refers to lenght of matrix
    nonogram=np.zeros(n,m)
    return nonogram
def imprimirNonograma(state):

def leerPistas():
    listaIzquierda     
