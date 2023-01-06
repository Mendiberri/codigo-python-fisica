import numpy as np
import matplotlib.pyplot as plt


#%% Espectrograma
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy.io

#%%leo datos
fs, x = wavfile.read('My recording 2.wav')

#genero el espectrograma
f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.xlim([1,2.5])
plt.ylim([350,450])
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [seg]')
plt.show()

#%% leo datos
fs, x = wavfile.read('My recording 3.wav')

# genero el espectrograma
f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx, shading= 'gouraund')
plt.xlim([1,2.5])
plt.ylim([350,450])
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [seg]')
plt.show()
#%% leo datos
fs, x = wavfile.read('My recording 1.wav')

# genero el espectrograma
f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx, shading= 'gouraund')
plt.xlim([1,2.5])
plt.ylim([350,450])
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [seg]')
plt.show()

#%%

