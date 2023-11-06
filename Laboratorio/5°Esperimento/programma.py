import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import socket
import struct
from scipy import constants, fft 
import soundfile as sf


#(**)
#Mettere il path del file es:" /home/alessandro/Laboratorio-3/Laboratorio/5°Esperimento/diapason.wav" completo senno non funziona oppure aprire VSCode/Emac/ecc... dalla cartella 
data,samplerate=sf.read("/home/alessandro/Laboratorio-3/Laboratorio/5°Esperimento/diapason.wav",always_2d=True)  

#NB IL CANALE SINISTRO è data[...][0]  CANALE DESTRO è data[...][1]
print("\nIl numero di samplerate è: ", samplerate)
print("\n Data: \n ",data)
print("\nIl numero di elementi nel data è: ",len(data),"\n")


datamono_sx=[]
datamono_dx=[]
for i in range(len(data)):
    datamono_sx.append(data[i][0])
    datamono_dx.append(data[i][1])

#Mettere il path dove vuoi che il file si trovi :)   (Vale stesso discordo di (**) )
sf.write("/home/alessandro/Laboratorio-3/Laboratorio/5°Esperimento/copia_suono.wav",datamono_sx,samplerate)

#Grafico suono
tempo=np.linspace(0,int(10),len(data))
plt.plot(tempo,datamono_sx,color="blue",alpha=0.5)
plt.plot(tempo,datamono_dx,color="orange",alpha=0.5)
plt.rcParams["figure.autolayout"]=True
plt.rcParams["figure.figsize"]=[7.5,3.5]
plt.title("Grafico suono")
plt.xlabel("Tempo[s]")
plt.ylabel("Ampiezza audio[u.m]")
plt.show()



t=input("\nVuoi vedere il grafico della potenza?\n1 se si altrimenti 0\n")
if(int(t)==1):
    #DA FARE PARTE REALE E IMMAGINARIA E MODULO !!!


    print("\nLen Potenza:\n")
    #Potenza
    data_ff_sx=fft.fft(datamono_sx)  # n/2+1
    data_ff_dx=fft.fft(datamono_dx)  # n/2+1
    print(len(data_ff_sx))
    print(len(data_ff_dx))



    #Reale
    print("\nLen Reale:\n")
    real_data_ff_sx=np.real(fft.fft(datamono_sx))  # n/2+1
    real_data_ff_dx=np.real(fft.fft(datamono_dx))  # n/2+1
    print(len(real_data_ff_sx))
    print(len(real_data_ff_dx))

    #Immaginaria
    print("\nLen Immaginaria:\n")
    imm_data_ff_sx=np.imag(fft.fft(datamono_sx))  # n/2+1
    imm_data_ff_dx=np.imag(fft.fft(datamono_dx))  # n/2+1
    print(len(imm_data_ff_sx))
    print(len(imm_data_ff_dx))


    """ 
    Due metodi per la frequenza:
    
    1°)


    freq_ff=0.5*fft.rfftfreq(data_ff.size, 1.0/samplerate)

    this is how Stefano Germani did: the 0.5 he called "nyquist"
    Unlike fftfreq (but like scipy.fftpack.rfftfreq) the Nyquist frequency component is considered to be positive.
    
    2°)
    """

    freq_ff = fft.fftfreq(len(datamono_sx), 1.0/samplerate)
    

    print("\n Data fourier : \n ",data_ff_sx)
    print("\nIl numero di elementi nel data fourier è: ",len(data_ff_sx),"\n")
    print("\n La frequenza: \n ",freq_ff)
    print("\nIl numero di elementi nel frequenza è: ",len(freq_ff),"\n")
    
    """
    plt.figure(20)
    fig = plt.gcf()
    fig.set_size_inches(10, 8)
    plt. title("FFT" )
    plt.xlabel('Frequenza (hz)')
    plt.ylabel( 'Ampiezza (parte reale) (u.a) ')
    plt.plot(freq_ff[:len(data_ff_sx)], data_ff_sx[:len(data_ff_sx)].real, "go--")
    #plt.plot(freq_ff[:len(data_ff_dx)], data_ff_dx[:len(data_ff_dx)].imag, "ro--")
    plt.show()
    """
    

         
    
      
    fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2)
    fig.set_size_inches(10, 8)
    plt.title("Trasformate Fourier")     
 


    #----------------------------------------------------------------
    #Ax1= POTENZA

    ax1.set_xlabel('Frequenza (hz)')
    ax1.set_ylabel( 'Potenza (u.a) ')

    ax1.plot(freq_ff[:len(data_ff_sx)], data_ff_sx[:len(data_ff_sx)], "g-")

    #----------------------------------------------------------------
    #Ax2= Reale

    ax2.set_xlabel('Frequenza (hz)')
    ax2.set_ylabel( 'Ampiezza (parte reale) (u.a) ')

    ax2.plot(freq_ff[:len(real_data_ff_sx)], real_data_ff_sx[:len(real_data_ff_sx)], "b-")
    #----------------------------------------------------------------
    #Ax3= Immaginaria

    ax3.set_xlabel('Frequenza (hz)')
    ax3.set_ylabel( 'Ampiezza (parte immaginaria) (u.a) ')
    ax3.plot(freq_ff[:len(imm_data_ff_sx)], imm_data_ff_sx[:len(imm_data_ff_sx)], "m-")
    
    
    ax4.set_visible(False) #non ti fa vedere il grafico 

    plt.show()

    #----------------------------------------------------------------
    print("\nRispetto alle note:\n")
    
    plt.plot(freq_ff[:len(data_ff_sx)], data_ff_sx[:len(data_ff_sx)], "g-")
    #NOTA:
    


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
    plt.rcParams["figure.autolayout"]=True
    plt.title("Potenza rispetto note")
    plt.xlim(0,2500)
    plt.xlabel("frequenza[Hz]")
    plt.ylabel("Potenza[u.m]")
    plt.show()