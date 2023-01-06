import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.signal import find_peaks    


def MakeSpectralPlot(y, Fs, fignum=1):
    
    yfft = fftpack.fft(y)
    N = len(y)
    xf = np.linspace(0, Fs/2, int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    PosicionPicos, IntensidadPicos = find_peaks(yf, height=yf[0])
    print(PosicionPicos)
    print(IntensidadPicos)
#    VectorFrecuenciaPicos = [xf[i] for i in PosicionPicos]
    plt.figure(fignum)
    plt.clf()
    plt.semilogx(xf, yf)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud (V)')
    plt.title('Descomposición espectral del ruido')
    return xf, yf


def MakeSpectralPlot2(y, Fs, fignum=1):
    
    yfft = fftpack.fft(y)
    N = len(y)
    xf = np.linspace(0, Fs/2, int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    
    
    plt.figure(fignum)
    plt.clf()
    plt.semilogx(xf, yf)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud (V)')
    plt.title('Descomposición espectral del ruido')
    return xf, yf

#%%

#Ejemplo de plot
    
t = np.linspace(0, 10, 10000)
tstep = max(t)/len(t)
fsamp = 1/tstep

f0 = 1
f1 = 20
V = np.sin(2*np.pi*f0*t) + np.sin(2*np.pi*f1*t) 

plt.figure(2)
plt.clf()
plt.plot(t, V)

MakeSpectralPlot(V, fsamp)
MakeSpectralPlot2(V, fsamp,3)

#%%
# análisis de datos experimentales adquiridos

t = np.loadtxt("clase2_L1_tiempo.txt")
tstep = max(t)/len(t)
fsamp = 1/tstep

V = np.loadtxt("clase2_L1_Volt.txt")

plt.figure(1)
plt.plot(t, V)
plt.xlabel('tiempo (s)')
plt.ylabel('voltaje (V)')
plt.title('L1 = 24.5 cm')

#hay que poner los límites del gráfico para enfocar la región de los picos
xf, yf = MakeSpectralPlot(V, fsamp)
MakeSpectralPlot2(V, fsamp,3)
plt.semilogx(xf, yf)
plt.xlim([20,400])
plt.ylim([0,1.2])
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud espectral (V)')
plt.title('análisis espectral L1 = 24.5 cm')

#%%
#hallar constante de amortiguamiento
from scipy.optimize import curve_fit
from scipy.optimize import curve_fit,least_squares

#el parámetro "height" hay que ponerlo donde está centrada la oscilacion o más arriba
#hay que ajustarla para hallar los picos que queremos
#en general hay que quitar "prominence", pero para L1 ayudó
xpeaks = []
for i in find_peaks(V,height=2.5,prominence=1)[0]:
    xpeaks.append(t[i])

ypeaks = []
for i in find_peaks(V,height=2.5,prominence=1)[0]:
    ypeaks.append(V[i])

#los puntos que aún no nos interesen se pueden sacar "corriendo" desde donde graficamos
plt.plot(xpeaks[1:],ypeaks[1:])

#nuestras funciones no están centradas en 0. Hay que summar el "offset"
#para que el ajuste sea bueno
def modelo(t,alfa,k):
    return 2.5+k*np.exp(-alfa*t)

#ajustamos la parte que nos interesa
opt, cov = curve_fit(modelo,xpeaks[1:],ypeaks[1:])

plt.figure()
plt.plot(xpeaks[1:],ypeaks[1:],label="picos medidos L1 = 24.5 cm")
plt.plot(xpeaks[1:],modelo(np.array(xpeaks[1:]),opt[0],opt[1]),label="ajuste envolvente")
plt.legend(loc="best")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud espectral (V)')

#para ver la bondad con R2
ss_res = np.sum( (np.array(ypeaks[1:]) - modelo(np.array(xpeaks[1:]),opt[0],opt[1]))**2  )
ss_tot = np.sum( (np.array(ypeaks[1:]) - np.mean(np.array(ypeaks[1:])))**2)
R = 1 - (ss_res / ss_tot)
