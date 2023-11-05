import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import math
import scipy
from scipy import optimize
import scipy.odr as odr


def linear_func(p, x):
    m, c = p
    return m*x + c



vin = 3.00
inc_v = 0.01


freq=np.array([30,91,150,160,170,180,190,200,210,220,230,240,270,290,300,400,500,600])

freq=freq*(10**3)

inc_f = np.full(len(freq),10**3)
Amp=np.array([1.51,1.48,1.32,1.28,1.20,1.16,1.13,1.06,0.998,0.987,0.961,0.929,0.825,0.791,0.760,0.600,0.536,0.488])
inc_a = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001])


guad = np.empty(len(Amp))
inc_g = np.empty(len(Amp))
for i in range(0,len(Amp)):
    guad[i]=Amp[i]/vin
    print(Amp[i]/vin)
    inc_g[i] = math.sqrt(pow(inc_a[i]/vin,2)+pow(Amp[i]*inc_v/(vin*2),2))



print("Guad è \n",guad)
print("inc_Guad è \n",inc_g)




a=input("\nVuoi i primi due grafici ?\n")
if(int(a)==1):
    print("\nPer continuare chiudere le schede dei grafici\n")
    print("Grafico con valori normali")


    f1 = plt.figure(1)
    plt.errorbar(freq/10**3, guad, xerr = inc_f/10**3, yerr = inc_g, fmt = ".",ecolor = 'green', color = "red")
    plt.title("Grafico Frequenza-Guadagno")
    plt.xlabel("Frequenza (kHz)")
    plt.ylabel("Guadagno")


    print("Grafico con valori scala logaritmica")

    f2 = plt.figure(2)
    plt.errorbar(freq, guad, xerr = inc_f, yerr = inc_g, fmt = ".", ecolor = 'red', color = "green")
    plt.title("Grafico Frequenza-Guadagno")
    plt.yscale("log")
    plt.xscale("log")

    plt.xlabel("Logaritmo(Frequenza (Hz))")
    plt.ylabel(" Guadagno (dB)")
    plt.show()




b=input("\nVuoi il grafico?\n")

if(int(b)==1):



   

  

    freq1 = np.log10(freq)
    guad1 = 20*np.log10(guad) #*20


    print(freq1)
    print(guad1)

    print("------------------------------------\n")
    inc_f1_log = np.empty(len(freq1))

    for i in range(0,len(freq1)):
        inc_f1_log[i]=inc_f[i]/(freq[i])

    inc_g_log = np.empty(len(guad))

    for i in range(0,len(guad)):
        inc_g_log[i]=inc_g[i]/(guad[i])

    inc_g_log = inc_g_log*20


    print(inc_g_log)
    print(inc_f1_log)

    print("\n\n\n\n")
    
    linear_model = odr.Model(linear_func)
    data = odr.RealData(freq1[2:], guad1[2:], sx=inc_f1_log[2:], sy=inc_g_log[2:])
    linear_odr    = odr.ODR(data, linear_model,    beta0=[20., 60.])
    linear_out    = linear_odr.run()
    
    
    print('---------- Funzione  Lineare   ---------')
    linear_out.pprint()
    plt.errorbar(freq1,guad1,xerr=inc_f1_log,yerr=inc_g_log, fmt='.',c='red', label='Dati')
    plt.title('Fit lineare guadagno frequenza (logaritmo)')
    plt.plot(freq1[:13],np.full(len(freq1)-5,guad1[0]), label='Guadagno nominale1')
    
    plt.plot(np.linspace(5,5.8, 10), linear_func(   linear_out.beta,   np.linspace(5,5.8, 10)),    c='lightblue',       label='Fit lineare') #4,10
    plt.axvline(x=np.log10([200000]), linestyle='--', color = 'indianred')
    plt.axhline(y=-9.03221,linestyle="--", label='Guadagno a -3db', color = 'darkred', alpha = 0.5)
    plt.xlabel('Logaritmo(frequenza (Hz))')
    plt.ylabel('Guadagno (dB)')
    print("\nPer continuare chiudere le schede dei grafici\n")
    plt.legend()
    
    plt.show()


   

