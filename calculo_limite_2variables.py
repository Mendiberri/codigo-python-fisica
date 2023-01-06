import numpy as np

#defino las funciones de las que busco el límite:
def f1(x,y):
    fun = (x**3)/((x**2)+(y**2))
    return(fun)

def f2(x,y):
    fun = x*(np.tan(y-3))/((y**2)-9)
    return(fun)

def f3(x,y):
    fun = (8+y**3)*(np.log(x**3))/np.sin((x**2)+x-2)
    return(fun)

#me acerco al límite arrancando a 1 de distancia en cada eje 
#divido la distancia a la mitad en cada paso
#x0, y0 son los puntos donde quiero evaluar el límite, div el número de pasos a realizar
#f es la función de 2 variables a estudiar
#puedo cambiar la dirección por la que me acerco multiplicando h por algún valor en líneas 28 o 29
def limite(f,x0,y0,div):
    h = 1
    im = []
    x = []
    y = []
    while div >= 0:
        im.append(f(x0+h,y0+h))
        x.append(x0+h)
        y.append(y0+h)
        h=h*0.5
        div=div-1
    return(im[-1])