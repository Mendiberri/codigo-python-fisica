import numpy as np
import numpy.linalg as npl

def jacobi(A,b,x0,max_iter,tol):
    ite=0
    xn=x0
    resto = npl.norm(b-np.dot(A,xn))
    D=npl.inv(np.diag(np.diag(A)))
    L=np.tril(A,k=-1)
    U=np.triu(A,k=1)
    B=-np.dot(D,L+U)
    while ite<=max_iter and tol<resto:
        ite=ite+1
        xn = np.dot(D,b) + np.dot(B,xn)
        resto = npl.norm(b-np.dot(A,xn))
    if ite == max_iter:
        print("máximo de iteraciones alcanzado")
    return([xn,ite])

def G_S(A,b,x0,max_iter,tol):
    ite=0
    xn=x0
    resto = npl.norm(b-np.dot(A,xn))
    D=np.diag(np.diag(A))
    L=np.tril(A,k=-1)
    U=np.triu(A,k=1)
    B=-(np.dot(npl.inv(D+L),U))
    C=np.dot(npl.inv(D+L),b)
    while ite<=max_iter and tol<resto:
        ite=ite+1
        xn = C + np.dot(B,xn)
        resto = npl.norm(b-np.dot(A,xn))
    if ite == max_iter:
        print("máximo de iteraciones alcanzado")
    return([xn,ite])

A1 = np.array([[1,0],[0,2]])
A2 = np.array([[1,1],[0,2]])
b = np.array([[1],[1]])
#las soluciones son (1, 1/2) y (1/2, 1/2) respectivamente
x0 = np.array([[0],[0]])

#ambos métodos tomaron 1 iteración para A1 y 2 iteraciones para A2