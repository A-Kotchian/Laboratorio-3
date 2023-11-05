import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import math
import scipy
from scipy import optimize
import scipy.odr as odr




file = pd.read_csv("/home/alessandro/Desktop/Laboratorio/3°Esperimento/Pippo.csv")
print(file.columns)
print(file.info)



##################################################################################


#Raccolta Volts


volt=[]
list_volt=[]

for i in file["CH2"][2:]:
    list_volt.append(float(i))

for i in range(0,7):
    volt.append(list_volt[i*180:180+i*180])


##################################################################################

#Raccolta Temp

temp=[]
list_temp=[]

for i in file["X"][2:]:
    list_temp.append(float(i))

for i in range(0,7):
    temp.append(list_temp[i*180:180+i*180])




##################################################################################


#Grafico dati


x = []
for i in list_temp:
    x.append(int(i)*0.01)

plt.plot(x, list_volt, '-.',label="dati")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensione (V)")
plt.legend()
plt.show()




##################################################################################

b=input("Vuoi visualizzare il grafico ogni due picchi?\nInserire 1 se si, altrimenti altro\n")
if(int(b)==1):


    #DA 1-4

    fig, ((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    fig.suptitle("Volt-Tempi")

    ax1 

    ax1.plot(temp[0],volt[0],"-",color='blue', alpha=0.5)
    ax2.plot(temp[1],volt[1],"-",color='green', alpha=0.5)
    ax3.plot(temp[2],volt[2],"-",color='red', alpha=0.5 )
    ax4.plot(temp[3],volt[3],"-",color='lightgreen', alpha=0.5)

    ax1.legend(["Dati"])
    ax2.legend(["Dati"])
    ax3.legend(["Dati"])
    ax4.legend(["Dati"])

    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Tensione (V)")

    ax2.set_xlabel("Tempo (s)")
    ax2.set_ylabel("Tensione (V)")

    ax3.set_xlabel("Tempo (s)")
    ax3.set_ylabel("Tensione (V)")

    ax4.set_xlabel("Tempo (s)")
    ax4.set_ylabel("Tensione (V)")
    
    plt.show()

    #DA 5-7

    fig, ((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    fig.suptitle("Volt-Tempi")

    ax1 

    ax1.plot(temp[4],volt[4],"-",color='blue', alpha=0.5)
    ax2.plot(temp[5],volt[5],"-",color='green', alpha=0.5)
    ax3.plot(temp[6],volt[6],"-",color='red', alpha=0.5 )

    ax1.legend(["Dati"])
    ax2.legend(["Dati"])
    ax3.legend(["Dati"])

    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Tensione (V)")

    ax2.set_xlabel("Tempo (s)")
    ax2.set_ylabel("Tensione (V)")

    ax3.set_xlabel("Tempo (s)")
    ax3.set_ylabel("Tensione (V)")

    ax4.set_visible(False)
    plt.show()



##################################################################################

#Calcolo e raccolta minimi

min_V=[]
min_t=[]

c=[110,110,110,110,110,110,110]
d=[110,110,110,110,110,110,110]

min_tick=[]

for i in range(0,7):
    for j in range(0,len(volt[i])):
        if volt[i][j]<=c[i]:
            c[i]=volt[i][j]
            d[i]=j+i*180
    min_V.append(c[i])
    min_t.append(d[i]*0.01)
    min_tick.append(d[i])

print("I tuoi minimi sono: ")
for i in range(0,len(min_V)):
    print("{:}°minimo è {:} con {:.2f} (s)\n".format(i,min_V[i],min_t[i]))




##################################################################################
"""
#GRAFICO MINIMI 

plt.plot(min_t, min_V, '.')
plt.show()

"""
##################################################################################

print("\n-----------------------------\n")



#Periodo e calcolo

T=[min_t[1]-min_t[0],min_t[2]-min_t[1],min_t[3]-min_t[2],min_t[4]-min_t[3],min_t[5]-min_t[4],min_t[6]-min_t[5]]
inc_T=[]

for i in T:
    inc_T.append(math.sqrt(pow(2*0.001,2)))

print("I periodi sono: ")
for i in range(0,6):
    print("\n-",round(T[i],3)," +- ", inc_T[i], " (s)")



print("\n-----------------------------\n")


##################################################################################


#Grafico e misura g

g=[0,0,0,0,0,0]
inc_g=[0,0,0,0,0,0]
for i in range(0,6):
    g[i]=4*(math.pi**2)*0.79*(1/(T[i]**2))                    #l=0.79+- 0.05
    inc_g[i]=math.sqrt(   pow(4*(math.pi**2)*0.05*(1/(T[i]**2)),2)  +  pow((8*(math.pi**2)*0.79*inc_T[i]*(1/(T[i]**3))),2))    


print("I valori di g per ogni periodo sono: \n")
for i in range(0,6):
    print("\n-",round(g[i],4)," +- ", round(inc_g[i],4), " (m/s^2)")

plt.errorbar(range(0,len(g)),g, yerr=inc_g, fmt=".", color="blue",label="Valori calcolati")
plt.axhline(y = 9.80665, color = 'red', linestyle = '-',label="Valore teorico")
plt.xlabel("n° Periodo")
plt.ylabel("Accelerazione (m/s^2)")
plt.legend() 
plt.show()

 
file



##################################################################################
##################################################################################


#CODICI PER CONTROLLARE RIGHE 

"""

#per riga 20 e 43


for i in volt:
    print (i,"\n", "Di lunghezza: ", len(i),"\n")
    print("\n \n \n \n ------------------------- \n \n \n \n ")    #Controllo dati 

    

#Per riga 43

print("Lunghezza tempi: ")

for i in range(0,7):
    print(len (temp[i]))


    
#Per riga 20

for i in range(0,7):
    print(len (volt[i]))


"""
