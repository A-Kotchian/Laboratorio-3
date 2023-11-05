
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


freq=np.array([29.9,51.5,84.7,169,198,294,385,490,538])
#kHz

Amp=np.array([8.80,5.12,3.04,1.46,1.24,0.826,0.608,0.440,0.364])



R2=5610
R1=[1350,2330,3910,8190,9790,14610,19530,26900,32700]
inc_R1=np.full(len(R1),1)
inc_R2=1
inc_f = np.full(len(freq),1)
inc_a = np.array([0.01,0.01,0.01,0.01,0.01,0.001,0.001,0.001,0.001])



rapp=np.empty(len(Amp))
inc_rapp = np.empty(len(Amp))
guad = np.empty(len(Amp))
inc_g = np.empty(len(Amp))
for i in range(0,len(Amp)):
    guad[i]=Amp[i]/vin
    print(Amp[i]/vin)
    rapp[i]=R2/R1[i]
    inc_rapp[i] = math.sqrt(pow(inc_R2/R1[i],2)+pow(R2*inc_R1[i]/(R1[i]**2),2))
    inc_g[i] = math.sqrt(pow(inc_a[i]/vin,2)+pow(Amp[i]*inc_v/(vin**2),2))



print("Guad è \n",guad)
print("inc_Guad è \n",inc_g)




a=input("\nVuoi i primi due grafici ?\n")
if(int(a)==1):
    print("\nPer continuare chiudere le schede dei grafici\n")
    print("Grafico con valori normali")


    
    plt.errorbar( rapp, freq, xerr = inc_rapp, yerr = inc_f, fmt=".",ecolor = 'navy', color = "yellow",label='R2/R1')
    plt.errorbar(guad, freq, xerr = inc_g, yerr = inc_f, fmt = ".",ecolor = 'green', color = "red",label='Guadagno')
    plt.title("Grafico Frequenza-Guadagno")
    plt.ylabel('frequenza (kHz)')
    plt.xlabel('Guadagno ')
    plt.legend()
    plt.show()

    print("Grafico con valori scala logaritmica")

    
    plt.errorbar( rapp, freq, xerr = inc_rapp, yerr = inc_f, fmt=".",ecolor = 'navy', color = "yellow",label='R2/R1')
    plt.errorbar(guad, freq, xerr = inc_g, yerr = inc_f, fmt = ".", ecolor = 'red', color = "green",label='Guadagno')
    plt.title("Grafico Frequenza-Guadagno")
    plt.yscale("log")
    plt.xscale("log")
 
    plt.ylabel('Logaritmo(frequenza (kHz))')
    plt.xlabel('Guadagno (dB)')
    plt.legend()
    plt.show()




b=input("\nVuoi il grafico?\n")

if(int(b)==1):



   

    rapp1 = 20*np.log10(rapp)

    freq1 = np.log10(freq)
    guad1 = 20*np.log10(guad) #*20

    print(rapp1)
    print(freq1)
    print(guad1)

    print("------------------------------------\n")
    inc_f1_log = np.empty(len(freq1))
    inc_r1_log = np.empty(len(rapp1))
    for i in range(0,len(freq1)):
        inc_f1_log[i]=inc_f[i]/(freq[i])
        
        inc_r1_log[i]=inc_rapp[i]/(rapp[i])

    inc_g_log = np.empty(len(guad))

    for i in range(0,len(guad)):
        inc_g_log[i]=inc_g[i]/(guad[i])

    inc_g_log = inc_g_log*20
    inc_r1_log = inc_r1_log*20

    print(inc_g_log)
    print(inc_f1_log)
    print(inc_r1_log)
    print("\n\n\n\n")
    
    linear_model = odr.Model(linear_func)
    data = odr.RealData(rapp1, freq1, sx=inc_r1_log, sy=inc_f1_log)
    linear_odr    = odr.ODR(data, linear_model,    beta0=[1., 0])
    linear_out    = linear_odr.run()
    
    
    print('---------- Funzione  Lineare   ---------')
    linear_out.pprint()
    plt.errorbar(rapp1,freq1,xerr=inc_r1_log,yerr=inc_f1_log, fmt='.',c='red', label='Dati')
    plt.title('Fit lineare R2/R1 frequenza (logaritmo)')
    plt.plot(rapp1, linear_func(   linear_out.beta,  rapp1),    c='lightblue',       label='Fit lineare') #4,10
    plt.ylabel('Logaritmo(frequenza (Hz))')
    plt.xlabel('R2/R1 (dB)')
    print("\nPer continuare chiudere le schede dei grafici\n")
    plt.legend()
    
    plt.show()


    linear_model = odr.Model(linear_func)
    data = odr.RealData(guad1, freq1, sx=inc_g_log, sy=inc_f1_log)
    linear_odr    = odr.ODR(data, linear_model,    beta0=[1., 0])
    linear_out    = linear_odr.run()
    
    
    print('---------- Funzione  Lineare   ---------')
    linear_out.pprint()
    plt.errorbar(guad1,freq1,xerr=inc_g_log,yerr=inc_f1_log, fmt='.',c='red', label='Dati')
    plt.title('Fit lineare guadagno frequenza (logaritmo)')
    plt.plot(guad1, linear_func(   linear_out.beta,  guad1),    c='lightblue',       label='Fit lineare') #4,10
    plt.ylabel('Logaritmo(frequenza (Hz))')
    plt.xlabel('Guadagno (dB)')
    print("\nPer continuare chiudere le schede dei grafici\n")
    plt.legend()
    
    plt.show()
   

