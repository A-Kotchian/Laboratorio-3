
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


freq=np.array([12,20.6,31,41,50,60,70,80,90,100,110,120,130,140,150,155])



inc_f = np.full(len(freq),1)
Amp=np.array([18.3,11.9,8.08,5.88,4.92,4.00,3.60,3.16,2.76,2.52,2.28,2.08,1.96,1.84,1.72,1.64])
inc_a = np.full(len(Amp),0.01)


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
    plt.errorbar(guad, freq, xerr = inc_g, yerr = inc_f, fmt = ".",ecolor = 'green', color = "red")
    plt.title("Grafico Frequenza-Guadagno")
    plt.ylabel('frequenza (Hz)')
    plt.xlabel('Guadagno ')


    print("Grafico con valori scala logaritmica")

    f2 = plt.figure(2)
    plt.errorbar(guad, freq, xerr = inc_g, yerr = inc_f, fmt = ".", ecolor = 'red', color = "green")
    plt.title("Grafico Frequenza-Guadagno")
    plt.yscale("log")
    plt.xscale("log")

    plt.ylabel('Logaritmo(frequenza (Hz))')
    plt.xlabel('Guadagno (dB)')
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
    data = odr.RealData(guad1, freq1, sx=inc_g_log, sy=inc_f1_log)
    linear_odr    = odr.ODR(data, linear_model,    beta0=[1., 0])
    linear_out    = linear_odr.run()
    
    
    print('---------- Funzione  Lineare   ---------')
    linear_out.pprint()
    plt.errorbar(guad1,freq1,xerr=inc_g_log,yerr=inc_f1_log, fmt='.',c='red', label='Dati')
    plt.title('Fit lineare guadagno frequenza (logaritmo)')
    plt.axhline(y = np.log10(1/(2*np.pi*300*(10**(-9))*5610)), linestyle='--', color = 'forestgreen', label = 'Frequenza di taglio teorica')
    plt.plot(guad1, linear_func(   linear_out.beta,  guad1),    c='lightblue',       label='Fit lineare') #4,10
    plt.axhline(y = np.log10([155]), linestyle='--', color = 'sienna', label='Frequenza di taglio effettiva del filtro')
    plt.ylabel('Logaritmo(frequenza (Hz))')
    plt.xlabel('Guadagno (dB)')
    print("\nPer continuare chiudere le schede dei grafici\n")
    plt.legend()
    
    plt.show()


   

