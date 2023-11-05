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
data,samplerate=sf.read("/home/alessandro/Laboratorio-3/Laboratorio/5°Esperimento/pulita_media.wav",always_2d=True)  

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
plt.plot(tempo,data,color="blue")
plt.rcParams["figure.autolayout"]=True
plt.rcParams["figure.figsize"]=[7.5,3.5]
plt.title("Grafico suono")
plt.xlabel("Tempo[s]")
plt.ylabel("Ampiezza audio[u.m]")
plt.show()



t=input("\nVuoi vedere il grafico della potenza?\n1 se si altrimenti 0\n")
if(int(t)==1):
    data_ff_sx=fft.rfft(datamono_sx)  # n/2+1
    data_ff_dx=fft.rfft(datamono_dx)  # n/2+1
    print(len(data_ff_sx))
    print(len(data_ff_dx))
    """ 
    Due metodi per la frequenza:
    
    1°)


    freq_ff=0.5*fft.rfftfreq(data_ff.size, 1.0/samplerate)

    this is how Stefano Germani did: the 0.5 he called "nyquist"
    Unlike fftfreq (but like scipy.fftpack.rfftfreq) the Nyquist frequency component is considered to be positive.
    
    2°)
    """

    freq_ff = fft.rfftfreq(len(datamono_sx), 1.0/samplerate)
    

    print("\n Data fourier : \n ",data_ff_sx)
    print("\nIl numero di elementi nel data fourier è: ",len(data_ff_sx),"\n")
    print("\n La frequenza: \n ",freq_ff)
    print("\nIl numero di elementi nel frequenza è: ",len(freq_ff),"\n")
    
    
    plt.figure(20)
    fig = plt.gcf()
    fig.set_size_inches(10, 8)
    plt. title("FFT" )
    plt.xlabel('Frequenza (hz)')
    plt.ylabel( 'Ampiezza (parte reale) (u.a) ')
    plt.plot(freq_ff[:len(data_ff_sx)], data_ff_sx[:len(data_ff_sx)].real, "go--")
    #plt.plot(freq_ff[:len(data_ff_dx)], data_ff_dx[:len(data_ff_dx)].imag, "ro--")
    plt.show()


    
