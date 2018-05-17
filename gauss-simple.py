#Resolucion de ecuaciones lineales por metodo de gauss
#@Autor : Cordero Ariano

import numpy as np
np.set_printoptions(formatter={"float": lambda x:"%0.5f"%(x)})

def inputMatrix() :

    n = 4
    A = np.array([[ 0 for x in range(n)]  for y in range(n)], dtype =  float)
    A[0][0] = 2
    A[0][1] = 1
    A[0][2] = 1
    A[0][3] = 0
    A[1][0] = 4
    A[1][1] = 3
    A[1][2] = 3
    A[1][3] = 1
    A[2][0] = 8
    A[2][1] = 7
    A[2][2] = 9
    A[2][3] = 5
    A[3][0] = 6
    A[3][1] = 7
    A[3][2] = 9
    A[3][3] = 8

    return A

def inputMatrixb() :

    n = 4
    b = np.array([0 for x in range(n)], dtype =  float)
    b[0] = 1
    b[1] = 8
    b[2] = 30
    b[3] = 41

    return b

def aumentada( A, b) :

    M = np.c_[ A, b]
    return M

def printMatrix( A ) :

    print A,"\n"

def gauss( A, b) :

    n = len(A)
    a = aumentada(A, b)
    m = np.array([0 for x in range(n)], dtype =  float)
    #eliminacion
    for k in range( 0, n-1 ) :
        for i in range( k+1, n) :
            m[i] = a[i][k]/float( a[k][k])
            for j in range( k, len( a[i])) :
                a[i][j] = a[i][j] - m[i]*a[k][j]
        printMatrix(a)

    #sustitucion
    x =  np.array([0 for x in range(n)], dtype =  float)
    x[n-1] = a[n-1][n]/float( a[n-1][n-1])
    for i  in range( n - 2, -1, -1) :
        x[i] = a[i][n]
        for j in range( i + 1, n) :
            x[i] = x[i] -   a[i][j]*x[j]
        x[i] = x[i]/float( a[i][i])
    print x

def main() :

    A = inputMatrix()
    b = inputMatrixb()
    printMatrix(A)
    printMatrix(b)
    M = aumentada(A, b)
    printMatrix(M)
    gauss(A,b)
main()
