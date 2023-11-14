import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt
import soundfile as sf 
import scipy as sp
from scipy import constants
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
import sys,os







data1 = pd.read_csv(r"C:\Users\diavo\OneDrive\Desktop\Università\Anno 3\Laboratorio 3\Laboratorio-3\Laboratorio\5°Esperimento\data_1.csv")
data2 = pd.read_csv(r"C:\Users\diavo\OneDrive\Desktop\Università\Anno 3\Laboratorio 3\Laboratorio-3\Laboratorio\5°Esperimento\data_2.csv")
data3 = pd.read_csv(r"C:\Users\diavo\OneDrive\Desktop\Università\Anno 3\Laboratorio 3\Laboratorio-3\Laboratorio\5°Esperimento\data_3.csv")


samplerate=44100
time1 = np.array(data1["Tempo"])
ampl1=np.array(data1["Ampiezza"])
time2 = np.array(data2["Tempo"])
ampl2=np.array(data2["Ampiezza"])
time3 = np.array(data3["Tempo"])
ampl3=np.array(data3["Ampiezza"])

"""
print("INFO:\n")
print("data_1\n")
print(data1.info)
print("\ndata_2\n")
print(data2.info)
print("\ndata_3\n")
print(data3.info)

"""
#GRAFICI SEGNALI REGISTRATI 


fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
fig.suptitle("Segnali registrati")  

ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel( 'Ampiezza (u.a) ')
ax1.plot(time1, ampl1, "g-")

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel( 'Ampiezza (u.a) ')
ax2.plot(time2, ampl2, "r-")

ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel( 'Ampiezza (u.a) ')
ax3.plot(time3, ampl3, "b-")

ax4.set_visible(False)

plt.show()


#PARTE TRASFROMATA SENZA MASCHERA
trasf1=pow(np.abs(fft(ampl1)),2)   #POTENZE 
trasf2=pow(np.abs(fft(ampl2)),2)
trasf3=pow(np.abs(fft(ampl3)),2)



fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
fig.suptitle("Segnali registrati trasformati")  

ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel( 'Ampiezza segnale (u.a) ')
ax1.plot(time1, trasf1, "g-")

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel( 'Ampiezza segnale (u.a) ')
ax2.plot(time2, trasf2, "r-")

ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel( 'Ampiezza segnale (u.a) ')
ax3.plot(time3, trasf3, "b-")

ax4.set_visible(False)

plt.show()


"""
#PARTE ANTITRASFROMATA SENZA MASCHERA
a_trasf1=ifft(ampl1)
a_trasf2=ifft(ampl2)
a_trasf3=ifft(ampl3)



fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
fig.suptitle("Segnali registrati trasformati")  

ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel( 'Ampiezza segnale (u.a) ')
ax1.plot(time1, a_trasf1, "g-")

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel( 'Ampiezza segnale (u.a) ')
ax2.plot(time2, a_trasf2, "r-")

ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel( 'Ampiezza segnale (u.a) ')
ax3.plot(time3, a_trasf3, "b-")

ax4.set_visible(False)

plt.show()
"""

#PARTE ANTITRASFROMATA SENZA MASCHERA
"""
mask1= trasf1>10
mask2= trasf2>2000
mask3= trasf3>2000
"""
mask1= trasf1>pow(10,10)
mask2= trasf2>pow(10,10)
mask3= trasf3>pow(10,10)



a_trasf1_mask=ifft(trasf1*mask1)
a_trasf2_mask=ifft(trasf2*mask2)
a_trasf3_mask=ifft(trasf3*mask3)



fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
fig.suptitle("Segnali registrati trasformati")  

ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel( 'Ampiezza segnale (u.a) ')
ax1.plot(time1, a_trasf1_mask, "g-")

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel( 'Ampiezza segnale (u.a) ')
ax2.plot(time2, a_trasf2_mask, "r-")

ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel( 'Ampiezza segnale (u.a) ')
ax3.plot(time3, a_trasf3_mask, "b-")
ax4.plot(time3, ampl3, "b-")
#ax4.set_visible(False)

plt.show()