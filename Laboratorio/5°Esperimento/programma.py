import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt
import soundfile as sf 
import scipy as sp
from scipy import constants
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
import sys,os


def antitrasformata_fourier_seno_coseno2(ampiezze, frequenze_mask, samplerate):
<<<<<<< HEAD
    N=len(ampiezze)
    y=np.empty(N, dtype = 'complex')
    mask= ampiezze!=0
    for i in range(0,N):    #DA METTERE len(freq) al posto di n
        
        y[i]=np.sum( np.real(np.array(ampiezze[mask]))
                    *np.cos(2*np.pi*i*frequenze_mask[mask]/samplerate)
                    -np.imag(np.array(ampiezze[mask]))
                    *np.sin(2*np.pi*i*frequenze_mask[mask]/samplerate))
    return y/N

data, samplerate = sf.read(r'C:\Users\diavo\OneDrive\Desktop\Università\Anno 3\Laboratorio 3\Laboratorio-3\Laboratorio\5°Esperimento\distorta_pezzo.wav')


time = np.linspace(0,len(data)/samplerate,len(data))

# creiamo un array in cui sia contenuta solo una colonna di data, ad esempio la destra. E' possibile che le colonne rappresentino le ampiezze che vengono
# mostrate con i diversi colori 

colonna_destra = np.empty(len(data))
colonna_sinistra = np.empty(len(data))
for i in range(0,len(data)):
        colonna_destra[i] = data[i][1]
        colonna_sinistra[i]=data[i][0]


b=input("\nVuoi vedere il grafico dei canali?\n(1 se si altrimenti altro)\n")
if (int(b)==1):

    fig, (ax1,ax2)= plt.subplots(1,2)
    ax1.plot(time, colonna_sinistra, label ='Primo canale', c='mediumblue')
    ax1.legend(loc='upper right')
    ax2.plot(time, colonna_destra, label='Secondo canale', c='mediumblue')
    ax2.legend(loc='upper right')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Andamento primo canale')
    ax2.set_title('Andamento secondo canale')
    plt.legend()
    plt.show()

    # plt.title('Grafico delle due colonne insieme')
    # plt.plot(time, colonna_destra, label='Colonna destra', c='blue')
    # plt.plot(time, colonna_sinistra, label='Colonna sinistra', c='red', alpha=0.5)
    # plt.xlabel('Time(s)')
    # plt.ylabel('Ampiezza (u.a)')
    # plt.legend(loc='upper right')
    # plt.show()


# selezioniamo allora uno dei due segnali (canale)
fft_colonna_destra = fft(colonna_destra)
n = len(fft_colonna_destra)
freq_dx = fftfreq(n,1/samplerate)
module_dx = pow(np.abs(fft_colonna_destra),2)




fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
plt.title("Trasformate Fourier")     

#----------------------------------------------------------------
#Ax1= POTENZA

ax1.set_xlabel('Frequenza (Hz)')
ax1.set_ylabel( 'Potenza (u.a) ')
ax1.set_xlim(0,5e3)
ax1.plot(freq_dx[:len(module_dx)], module_dx[:len(module_dx)], "g-")
ax1.set_title('Andamento coefficienti in modulo secondo canale')
#----------------------------------------------------------------
#Ax2= Reale

ax2.set_xlabel('Frequenza (Hz)')
ax2.set_ylabel( 'Ampiezza(u.a) ')
ax2.plot(freq_dx[:len(np.real(fft_colonna_destra))], np.real(fft_colonna_destra)[:len(np.real(fft_colonna_destra))], "b-")
ax2.set_title('Andamento parte reale coefficienti secondo canale')
ax2.set_xlim(-5e3,5e3)

#----------------------------------------------------------------
#Ax3= Immaginaria

ax3.set_xlabel('Frequenza (Hz)')
ax3.set_ylabel( 'Ampiezza (u.a) ')
ax3.plot(freq_dx[:len(np.imag(fft_colonna_destra))], np.imag(fft_colonna_destra)[:len(np.imag(fft_colonna_destra))], "m-")
ax3.set_title('Andamento parte immaginaria coefficienti secondo canale')
ax3.set_xlim(-5e3,5e3)


ax4.set_visible(False) #non ti fa vedere il grafico 
=======
    """
    The function transforms frequency spectrum of a signal with a 
    Fourier transormation to original signal (function of time), that is combination of cos+i*sin.

    N= lenght of Amplitude(of Fourier transformation)
    y= value of Fourier anti-transformation
    ampiezze=value of Amplitude of Fourier transformation
    frequenze_mask=value of frequence of Fourier transformation
    samplerate= frequency of cpu measurement


    We take, to make faster the calculation, just values of amplitudes and frequence 
    different from zero.

    
    y=Sum_{0}^{N} (real_part(np.array(ampiezze))*np.cos(2*np.pi*i*frequenze_mask/samplerate)   -   imag_part(np.array(ampiezze))*np.sin(2*np.pi*i*frequenze_mask/samplerate))
    """


    N=len(ampiezze)
    y=np.empty(N, dtype = 'complex')
    mask= ampiezze!=0

    for i in range(0,N):    #DA METTERE len(freq) al posto di n
        
        y[i]=np.sum( np.real(np.array(ampiezze[mask]))*np.cos(2*np.pi*i*frequenze_mask[mask]/samplerate)-np.imag(np.array(ampiezze[mask]))*np.sin(2*np.pi*i*frequenze_mask[mask]/samplerate))
        
    return y/N





#----------------------------------------------------------------------------------------------------
#COLLECTING DATA AND DIVIDING LEFT AND RIGHT CHANNELS

data, samplerate = sf.read(r"/home/alessandro/Laboratorio-3/Laboratorio/5°Esperimento/diapason.wav")
time = np.linspace(0,len(data)/samplerate,len(data))
colonna_destra = np.empty(len(data))
colonna_sinistra = np.empty(len(data))
for i in range(0,len(data)):
        colonna_destra[i] = data[i][1]
        colonna_sinistra[i]=data[i][0]



#---------------------------------------------------------------------------------
#GRAPH THE DATA

b=input("\nVuoi vedere il grafico dei canali?\n(1 se si altrimenti altro)\n")
if (int(b)==1):

    fig, (ax1,ax2)= plt.subplots(1,2)
    ax1.plot(time, colonna_sinistra, label ='Colonna sinistra', c='red')
    ax1.legend(loc='upper right')
    ax2.plot(time, colonna_destra, label='Colonna destra', c='blue')
    ax2.legend(loc='upper right')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Andamento primo canale')
    ax2.set_title('Andamento secondo canale')
    plt.legend()
    plt.show()

    plt.title('Grafico delle due colonne insieme')
    plt.plot(time, colonna_destra, label='Colonna destra', c='blue')
    plt.plot(time, colonna_sinistra, label='Colonna sinistra', c='red', alpha=0.5)
    plt.xlabel('Time(s)')
    plt.ylabel('Ampiezza (u.a)')
    plt.legend(loc='upper right')
    plt.show()




#--------------------------------------------------------------------------------------
#FOURIER TRASFORMATION OF DATA OF DX CHANNEL AND GRAPHICS RESULTS
fft_colonna_destra = fft(colonna_destra)
n = len(fft_colonna_destra)
freq_dx = fftfreq(n,1/samplerate)
module_dx = pow(np.abs(fft_colonna_destra),2)




fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
plt.title("Trasformate Fourier")     


#Ax1= POTENZA

ax1.set_xlabel('Frequenza (hz)')
ax1.set_ylabel( 'Potenza (u.a) ')
ax1.set_xlim(0,5e3)
ax1.plot(freq_dx[:len(module_dx)], module_dx[:len(module_dx)], "g-")
ax1.set_title('Andamento coefficienti in modulo colonna dx')


#Ax2= Reale

ax2.set_xlabel('Frequenza (hz)')
ax2.set_ylabel( 'Ampiezza(u.a) ')
ax2.plot(freq_dx[:len(np.real(fft_colonna_destra))], np.real(fft_colonna_destra)[:len(np.real(fft_colonna_destra))], "b-")
ax2.set_title('Andamento parte reale coefficienti colonna dx')
ax2.set_xlim(-5e3,5e3)


#Ax3= Immaginaria

ax3.set_xlabel('Frequenza (hz)')
ax3.set_ylabel( 'Ampiezza (u.a) ')
ax3.plot(freq_dx[:len(np.imag(fft_colonna_destra))], np.imag(fft_colonna_destra)[:len(np.imag(fft_colonna_destra))], "m-")
ax3.set_title('Andamento parte immaginaria coefficienti colonna dx')
ax3.set_xlim(-5e3,5e3)
ax4.set_visible(False) #non ti fa vedere il grafico 

>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
plt.show()




<<<<<<< HEAD
"""
#IDEM PER PARTE SINISTRA


fft_colonna_sinistra = fft(colonna_sinistra)
n = len(fft_colonna_sinistra)
freq_sx = fftfreq(n,1/samplerate)
module_sx = pow(np.abs(fft_colonna_sinistra),2)
=======
#-------------------------------------------------------------------------------------------------------------------
#LET'S FIND THE NOTES 


# calcolo dei picchi (valore della potenza y)
max1_dx = np.max(module_dx)
max2_dx= np.max(module_dx[1000:50000])
max3_dx = np.max(module_dx[2000:50000])

# codice per trovare le frequenze relative
f1_dx ,f2_dx, f3_dx = 0,0,0
for i in range(0,len(module_dx)):
    if module_dx[i]==max1_dx:
        f1_dx=freq_dx[i]
    if module_dx[i]==max2_dx:
        f2_dx=freq_dx[i]
    if module_dx[i]==max3_dx:
        f3_dx=freq_dx[i]

print("Modulo del canale destro: {:} \nFrequenza canale destro: {:}".format(len(module_dx), len(freq_dx)))
print("F1: {:}\nF2: {:}\nF3: {:}\n".format(f1_dx, f2_dx, f3_dx))


plt.figure(figsize=[8,8])
plt.title('Frequenze in corrispondenza dei picchi')
plt.plot(freq_dx, module_dx, label='Potenza dx',c='royalblue')
plt.xlabel('Frequenza(hz)')
plt.ylabel('Ampiezza(u.a)')
plt.axvline(-f1_dx, linestyle='--', color='limegreen',label='f1=110 Hz')
plt.axvline(-f2_dx,linestyle='--', color='orange',label='f2=880 Hz')
plt.axvline(-f3_dx,linestyle='--', color='violet',label='f3=1980 Hz')
plt.xlim(0,2500)
plt.legend(loc='upper right')
plt.show()
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a

fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
fig.set_size_inches(10, 8)
plt.title("Trasformate Fourier")     

#----------------------------------------------------------------
#Ax1= POTENZA

<<<<<<< HEAD
ax1.set_xlabel('Frequenza (hz)')
ax1.set_ylabel( 'Potenza (u.a) ')
ax1.set_xlim(0,5e3)
ax1.plot(freq_sx[:len(module_sx)], module_sx[:len(module_sx)], "g-")
ax1.set_title('Andamento coefficienti in modulo colonna sx')
#----------------------------------------------------------------
#Ax2= Reale

ax2.set_xlabel('Frequenza (hz)')
ax2.set_ylabel( 'Ampiezza(u.a) ')
ax2.plot(freq_sx[:len(np.real(fft_colonna_sinistra))], np.real(fft_colonna_sinistra)[:len(np.real(fft_colonna_sinistra))], "b-")
ax2.set_title('Andamento parte reale coefficienti colonna sx')
ax2.set_xlim(-5e3,5e3)

#----------------------------------------------------------------
#Ax3= Immaginaria

ax3.set_xlabel('Frequenza (hz)')
ax3.set_ylabel( 'Ampiezza (u.a) ')
ax3.plot(freq_sx[:len(np.imag(fft_colonna_sinistra))], np.imag(fft_colonna_sinistra)[:len(np.imag(fft_colonna_sinistra))], "m-")
ax3.set_title('Andamento parte immaginaria coefficienti colonna sx')
ax3.set_xlim(-5e3,5e3)

ax4.set_visible(False) #non ti fa vedere il grafico 
plt.show()

"""

# calcolo dei picchi (valore della potenza y)
max1_dx = np.max(module_dx)
max2_dx= np.max(module_dx[1000:50000])
max3_dx = np.max(module_dx[2000:50000])

# codice per trovare le frequenze relative
f1_dx ,f2_dx, f3_dx = 0,0,0
for i in range(0,len(module_dx)):
    if module_dx[i]==max1_dx:
        f1_dx=freq_dx[i]
    if module_dx[i]==max2_dx:
        f2_dx=freq_dx[i]
    if module_dx[i]==max3_dx:
        f3_dx=freq_dx[i]

print("Modulo del canale destro: {:} \nFrequenza canale destro: {:}".format(len(module_dx), len(freq_dx)))
print("F1: {:}\nF2: {:}\nF3: {:}\n".format(f1_dx, f2_dx, f3_dx))
# da questi valori si ricavano le note corrispondenti ad ogni picco

plt.figure(figsize=[6,4])
plt.title('Frequenze in corrispondenza dei picchi')
plt.plot(freq_dx, module_dx, label='Potenza dx',c='mediumblue')
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Ampiezza(u.a)')
plt.axvline(-f1_dx, linestyle='--', color='limegreen',label='f1=110 Hz')
plt.axvline(-f2_dx,linestyle='--', color='orange',label='f2=880 Hz')
plt.axvline(-f3_dx,linestyle='--', color='violet',label='f3=1980 Hz')
plt.xlim(0,2500)
plt.legend(loc='upper right')
plt.show()

=======
#--------------------------------------------------------------------------------------
#THIS PART LOOKS LIKE BLOODY HELL
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
b=input("Vuoi vedere tutte le note possibili?\n(1 se si altrimenti altro)\n")
if int(b)==1:
     #NOTA:
    
<<<<<<< HEAD
    plt.figure(figsize=[6,4])
=======
    plt.figure(figsize=[8,8])
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    plt.title('Frequenze in corrispondenza dei picchi')
    plt.xlabel('Frequenza(hz)')
    plt.ylabel('Ampiezza(u.a)')
    #0________________________________________________________________
    #do0
    plt.text(16.35,0,'Do_0',rotation=90)
    plt.axvline(x=16.35, linestyle="--")
    
    #re0
    plt.text(18.35	,0,'Re_0',rotation=90)
    plt.axvline(x=18.35	, linestyle="--")

    #mi0
    plt.text(20.60,0,'Mi_0',rotation=90)
    plt.axvline(x=20.60 ,linestyle="--")

    #fa0
    plt.text(21.83,0,'Fa_0',rotation=90)
    plt.axvline(x=21.83, linestyle="--")
    
    #sol0
    plt.text(24.50,0,'Sol_0',rotation=90)
    plt.axvline(x=24.50,linestyle="--")
    
    #la0
    plt.text(27.50,0,'La_0',rotation=90)
    plt.axvline(x=27.50, linestyle="--")   

    #si0
    plt.text(30.87,0,'Si_0',rotation=90)
    plt.axvline(x=30.87, linestyle="--")


    #1________________________________________________________________

    # do1
    plt.text(32.70, 0, 'Do_1', rotation=90)
    plt.axvline(x=32.70, linestyle="--")

    # re1
    plt.text(36.71, 0, 'Re_1', rotation=90)
    plt.axvline(x=36.71, linestyle="--")

    # mi1
    plt.text(41.20, 0, 'Mi_1', rotation=90)
    plt.axvline(x=41.20, linestyle="--")

    # fa1
    plt.text(43.65, 0, 'Fa_1', rotation=90)
    plt.axvline(x=43.65, linestyle="--")

    # sol1
    plt.text(49.00, 0, 'Sol_1', rotation=90)
    plt.axvline(x=49.00, linestyle="--")

    # la1
    plt.text(55.00, 0, 'La_1', rotation=90)
    plt.axvline(x=55.00, linestyle="--")

    # si1
    plt.text(61.74, 0, 'Si_1', rotation=90)
    plt.axvline(x=61.74, linestyle="--")


    #2________________________________________________________________

    # do2
    plt.text(65.41, 0, 'Do_2', rotation=90)
    plt.axvline(x=65.41, linestyle="--")

    # re2
    plt.text(73.42, 0, 'Re_2', rotation=90)
    plt.axvline(x=73.42, linestyle="--")

    # mi2
    plt.text(82.41, 0, 'Mi_2', rotation=90)
    plt.axvline(x=82.41, linestyle="--")

    # fa2
    plt.text(87.31, 0, 'Fa_2', rotation=90)
    plt.axvline(x=87.31, linestyle="--")

    # sol2
    plt.text(98.00, 0, 'Sol_2', rotation=90)
    plt.axvline(x=98.00, linestyle="--")

    # la2
    plt.text(110.00, 0, 'La_2', rotation=90)
    plt.axvline(x=110.00, linestyle="--")

    # si2
    plt.text(123.47, 0, 'Si_2', rotation=90)
    plt.axvline(x=123.47, linestyle="--")

    #3________________________________________________________________
    # do3
    plt.text(130.81, 0, 'Do_3', rotation=90)
    plt.axvline(x=130.81, linestyle="--")

    # re3
    plt.text(146.83, 0, 'Re_3', rotation=90)
    plt.axvline(x=146.83, linestyle="--")

    # mi3
    plt.text(164.81, 0, 'Mi_3', rotation=90)
    plt.axvline(x=164.81, linestyle="--")

    # fa3
    plt.text(174.61, 0, 'Fa_3', rotation=90)
    plt.axvline(x=174.61, linestyle="--")

    # sol3
    plt.text(196.00, 0, 'Sol_3', rotation=90)
    plt.axvline(x=196.00, linestyle="--")

    # la3
    plt.text(220.00, 0, 'La_3', rotation=90)
    plt.axvline(x=220.00, linestyle="--")

    # si3
    plt.text(246.94, 0, 'Si_3', rotation=90)
    plt.axvline(x=246.94, linestyle="--")

    #4________________________________________________________________
    #do4
    plt.text(261.63,0,'Do_4',rotation=90)
    plt.axvline(x=261.63, linestyle="--")
    
    #re4
    plt.text(293.66,0,'Re_4',rotation=90)
    plt.axvline(x=293.66, linestyle="--")

    #mi4
    plt.text(329.63,0,'Mi_4',rotation=90)
    plt.axvline(x=329.63 ,linestyle="--")

    #fa4
    plt.text(349.23,0,'Fa_4',rotation=90)
    plt.axvline(x=349.23, linestyle="--")
    
    #sol4
    plt.text(392.00,0,'Sol_4',rotation=90)
    plt.axvline(x=392.00,linestyle="--")
    
    #la4
    plt.text(440.00,0,'La_4',rotation=90)
    plt.axvline(x=440.00, linestyle="--")   

    #si4
    plt.text(493.88,0,'Si_4',rotation=90)
    plt.axvline(x=493.88, linestyle="--")

    #5________________________________________________________________
    
    #do5
    plt.text(523.25,0,'Do_5',rotation=90)
    plt.axvline(x=523.25, linestyle="--")
    
    #re5
    plt.text(587.33,0,'Re_5',rotation=90)
    plt.axvline(x=587.33, linestyle="--")

    #mi5
    plt.text(659.26,0,'Mi_5',rotation=90)
    plt.axvline(x=659.26, linestyle="--")

    #fa5
    plt.text(698.46,0,'Fa_5',rotation=90)
    plt.axvline(x=698.46, linestyle="--")
    
    #sol5
    plt.text(783.99,0,'Sol_5',rotation=90)
    plt.axvline(x=783.99, linestyle="--")

    #la5
    plt.text(880.00,0,'La_5',rotation=90)
    plt.axvline(x=880.00, linestyle="--")  
    
    #si5
    plt.text(987.77,0,'Si_5',rotation=90)
    plt.axvline(x=987.77, linestyle="--")

    #6________________________________________________________________
    #do6
    plt.text(1046.50,0,'Do_6',rotation=90)
    plt.axvline(x=1046.50, linestyle="--")
    
    #re6
    plt.text(1174.66,0,'Re_6',rotation=90)
    plt.axvline(x=1174.66,linestyle="--")

    #mi6
    plt.text(1318.51,0,'Mi_6',rotation=90)
    plt.axvline(x=1318.51, linestyle="--")

    #fa6
    plt.text(1396.91,0,'Fa_6',rotation=90)
    plt.axvline(x=1396.91, linestyle="--")
    
    #sol6
    plt.text(1567.98,0,'Sol_6',rotation=90)
    plt.axvline(x=1567.98, linestyle="--")
    
    #la6
    plt.text(1760.00,0,'La_6',rotation=90)
    plt.axvline(x=1760.00,  linestyle="--")  

    #si6
    plt.text(1975.53,0,'Si_6',rotation=90)
    plt.axvline(x=1975.53, linestyle="--")

    #Grafico
    plt.plot(freq_dx, module_dx, label='Potenza dx',c='g')
    plt.rcParams["figure.autolayout"]=True
    plt.title("Potenza rispetto note")
    plt.xlim(0,2500)
    plt.show()


<<<<<<< HEAD

=======
#--------------------------------------------------------------------------------------
#ANTITRASFORMATION FOURIER TAKING DIFFERENTS MASKS 
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
b=input("Vuoi vedere la ricorstruzione con i picchi?\n(1 se si altrimenti altro)\n")
if int(b)==1:
    fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    fig.set_size_inches(10, 8)
<<<<<<< HEAD
    fig.suptitle("Segnali filtrati ricostruiti con ifft") 
=======
    plt.title("Segnali filtrati") 
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a

    #---------------------------------------
    #ricostruzione con primo picco 
    maschera = module_dx == max1_dx
    #fft_dx_filtrata = fft_colonna_destra*maschera

    # invertiamo il segnale

    dx_filtrato1 = ifft(fft_colonna_destra*maschera)
<<<<<<< HEAD
    ax1.set_title('Segnale filtrato primo picco')
    ax1.plot(time, dx_filtrato1, label='Segnale filtrato ', c ='red')
=======
    ax1.set_title('Segnale dx filtrato primo picco')
    ax1.plot(time, dx_filtrato1, label='Segnale filtrato dx', c ='indianred')
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza(u.a)')
    ax1.set_xlim(0,0.3)


    #---------------------------------------
    #ricostruzione con primi due picchi 
    maschera2 = np.logical_or(module_dx == max1_dx,module_dx==max2_dx)
    #fft_dx_filtrata = fft_colonna_destra*maschera

    # invertiamo il segnale

    dx_filtrato2 = ifft(fft_colonna_destra*maschera2)
<<<<<<< HEAD
    ax2.set_title('Segnale primi due picchi')
    ax2.plot(time, dx_filtrato2, label='Segnale filtrato ', c ='yellowgreen')
=======
    ax2.set_title('Segnale dx primi due picchi')
    ax2.plot(time, dx_filtrato2, label='Segnale filtrato dx', c ='navy')
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    ax2.set_xlabel('Time(s)')
    ax2.set_ylabel('Ampiezza(u.a)')
    ax2.set_xlim(0,0.3)


    #----------------------------------------
    #ricostruzione con primi due picchi 
    maschera3 = np.logical_or(np.logical_or(module_dx == max1_dx, module_dx==max2_dx), module_dx==max3_dx)
    #fft_dx_filtrata = fft_colonna_destra*maschera

    # invertiamo il segnale

    dx_filtrato3 = ifft(fft_colonna_destra*maschera3)
<<<<<<< HEAD
    ax3.set_title('Segnale primi tre picchi')
    ax3.plot(time, dx_filtrato3, label='Segnale filtrato ', c ='deepskyblue')
=======
    ax3.set_title('Segnale dx primi tre picchi')
    ax3.plot(time, dx_filtrato3, label='Segnale filtrato dx', c ='forestgreen')
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    ax3.set_xlabel('Time(s)')
    ax3.set_ylabel('Ampiezza(u.a)')
    ax3.set_xlim(0,0.3)
    
    maschera4=np.absolute(fft_colonna_destra) > 2500
    dx_filtrato4 = ifft(fft_colonna_destra*maschera4)
<<<<<<< HEAD
    ax4.set_title('Segnale picchi con banda ')
    ax4.plot(time, dx_filtrato4, label='Segnale filtrato ', c ='magenta')
=======
    ax4.set_title('Segnale dx con range picchi ')
    ax4.plot(time, dx_filtrato4, label='Segnale filtrato dx', c ='khaki')
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    ax4.set_xlabel('Time(s)')
    ax4.set_ylabel('Ampiezza(u.a)')
    ax4.set_xlim(0,0.3)


    plt.show()

<<<<<<< HEAD
    # #PARTE FILTRATA
    # fig, ((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    # ax1.plot(time, dx_filtrato1, label ='Colonna sinistra', c='indianred')
    # ax1.legend(loc='upper right')
    # ax2.plot(time, dx_filtrato2, label='Colonna destra', c='navy')
    # ax2.legend(loc='upper right')
    # ax3.plot(time, dx_filtrato3, label='Colonna destra', c='forestgreen')
    # ax4.plot(time, dx_filtrato4, label='Colonna destra', c='khaki')
    # ax1.set_xlabel('Time(s)')
    # ax1.set_ylabel('Ampiezza del segnale(u.a)')
    # ax2.set_xlabel('Time(s)')
    # ax1.set_title('Andamento primo canale')
    # ax2.set_title('Andamento secondo canale')
    # #ax3.set_xlim(0, 0.2)
    # #ax2.set_xlim(0, 0.2)
    # #ax1.set_xlim(0, 0.2)
    # ax4.set_xlim(0,1.45) #SENNO STI CAZZI DI BATTIMENTI TIRANO IN SU 
    # plt.legend()
    # plt.show()
=======
    #PARTE FILTRATA
    fig, ((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    ax1.plot(time, dx_filtrato1, label ='Colonna sinistra', c='indianred')
    ax1.legend(loc='upper right')
    ax2.plot(time, dx_filtrato2, label='Colonna destra', c='navy')
    ax2.legend(loc='upper right')
    ax3.plot(time, dx_filtrato3, label='Colonna destra', c='forestgreen')
    ax4.plot(time, dx_filtrato4, label='Colonna destra', c='khaki')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Andamento primo canale')
    ax2.set_title('Andamento secondo canale')
    #ax3.set_xlim(0, 0.2)
    #ax2.set_xlim(0, 0.2)
    #ax1.set_xlim(0, 0.2)
    ax4.set_xlim(0,1.45) #SENNO STI CAZZI DI BATTIMENTI TIRANO IN SU 
    plt.legend()
    plt.show()
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    
    
    
    print("\n|------------------------------------------------------------|\n")
    print("\nConfronto tra funzione ifft e antitrasformata programmata\n")


    dx_fil1 = antitrasformata_fourier_seno_coseno2(fft_colonna_destra*maschera,freq_dx, samplerate)  #mettere gia con la frequenza la mask 
    dx_fil2 = antitrasformata_fourier_seno_coseno2(fft_colonna_destra*maschera2,freq_dx, samplerate)  #mettere gia con la frequenza la mask 
    dx_fil3 = antitrasformata_fourier_seno_coseno2(fft_colonna_destra*maschera3,freq_dx, samplerate)  #mettere gia con la frequenza la mask 
    dx_fil4 = antitrasformata_fourier_seno_coseno2(fft_colonna_destra*maschera4,freq_dx, samplerate)  #mettere gia con la frequenza la mask 



<<<<<<< HEAD
    fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    fig.set_size_inches(10, 8)
    fig.suptitle("Segnali filtrati ricostruiti con seno e coseno") 

    ax1.set_title('Segnale filtrato primo picco')
    ax1.plot(time, dx_fil1, label='Segnale filtrato ', c ='red')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza(u.a)')
    ax1.set_xlim(0,0.3)

    # invertiamo il segnale

 
    ax2.set_title('Segnale primi due picchi')
    ax2.plot(time, dx_fil2, label='Segnale filtrato ', c ='yellowgreen')
    ax2.set_xlabel('Time(s)')
    ax2.set_ylabel('Ampiezza(u.a)')
    ax2.set_xlim(0,0.3)

    ax3.set_title('Segnale primi tre picchi')
    ax3.plot(time, dx_fil3, label='Segnale filtrato ', c ='deepskyblue')
    ax3.set_xlabel('Time(s)')
    ax3.set_ylabel('Ampiezza(u.a)')
    ax3.set_xlim(0,0.3)
    
    ax4.set_title('Segnale picchi con banda ')
    ax4.plot(time, dx_fil4, label='Segnale filtrato ', c ='magenta')
    ax4.set_xlabel('Time(s)')
    ax4.set_ylabel('Ampiezza(u.a)')
    ax4.set_xlim(0,0.3)


=======
    #CONFRONTO 1 IFFT-PROGRAMMATA
    fig, (ax1,ax2)= plt.subplots(1,2)
    ax1.plot(time, dx_filtrato1, label ='Colonna sinistra', c='indianred')
    ax1.legend(loc='upper right')
    ax2.plot(time, dx_fil1, label='Colonna destra', c='navy')
    ax2.legend(loc='upper right')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Segnale dx filtrato primo picco con ifft')
    ax2.set_title('Segnale dx filtrato primo picco con metodo sin e cos')
    #ax1.set_xlim(0, 0.2) 
    plt.legend()
    plt.show()


    #CONFRONTO 2 IFFT-PROGRAMMATA
    fig, (ax1,ax2)= plt.subplots(1,2)
    ax1.plot(time, dx_filtrato2, label ='IFFT', c='indianred')
    ax1.legend(loc='upper right')
    ax2.plot(time, dx_fil2, label='Programmata', c='navy')
    ax2.legend(loc='upper right')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Segnale dx filtrato primi 2 picchi con ifft')
    ax2.set_title('Segnale dx filtrato primi 2 picchi con metodo sin e cos')
    #ax1.set_xlim(0, 0.2) 
    plt.legend()
    plt.show()


    #CONFRONTO 3 IFFT-PROGRAMMATA
    fig, (ax1,ax2)= plt.subplots(1,2)
    ax1.plot(time, dx_filtrato3, label ='IFFT', c='indianred')
    ax1.legend(loc='upper right')
    ax2.plot(time, dx_fil3, label='Programmata', c='navy')
    ax2.legend(loc='upper right')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Segnale dx filtrato primi 3 picchi con ifft')
    ax2.set_title('Segnale dx filtrato primi 3 picchi con metodo sin e cos')
    #ax1.set_xlim(0, 0.2) 
    plt.legend()
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a
    plt.show()



<<<<<<< HEAD
#Parte che scrive in audio 
#sf.write(r"C:\Users\diavo\OneDrive\Desktop\Università\Anno 3\Laboratorio 3\Laboratorio-3\Laboratorio\5°Esperimento\copia_suono.wav",dx_fil1,samplerate)
=======
    #CONFRONTO 4 IFFT-PROGRAMMATA
    fig, (ax1,ax2)= plt.subplots(1,2)
    ax1.plot(time, dx_filtrato4, label ='IFFT', c='indianred')
    ax1.legend(loc='upper right')
    ax2.plot(time, dx_fil4, label='Programmata', c='navy')
    ax2.legend(loc='upper right')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Ampiezza del segnale(u.a)')
    ax2.set_xlabel('Time(s)')
    ax1.set_title('Segnale dx filtrato primi 3 picchi con banda con ifft')
    ax2.set_title('Segnale dx filtrato primi 3 picchi con banda con metodo sin e cos')
    #ax1.set_xlim(0, 0.2) 
    plt.legend()
    plt.show()



#--------------------------------------------------------------------------------------------------------------------------------------------------------
#LET'S WRITE AUDIO FILE .WAV
sf.write(r"C:\Users\diavo\OneDrive\Desktop\Università\Anno 3\Laboratorio 3\Laboratorio-3\Laboratorio\5°Esperimento\copia_suono.wav",dx_fil1,samplerate)
>>>>>>> 43267b2b3a6c04190c5a023440ea37313a377f9a


