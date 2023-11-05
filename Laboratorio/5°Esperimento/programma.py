import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import socket
import struct
from scipy import constants,fft 
import soundfile as sf


"""
mics = sc.all_microphones()
print("Microfoni disponibili: ", mics, "\n")
default_mic = sc.default_microphone()
print("Microfono selezionato: ", default_mic, "\n")



t=input("Quanti secondi vuoi registrare?\n")
print("Registrando: ")
data = default_mic.record(samplerate=44100, numframes=44100*int(t)) #per decidere quanti secondi fare basta mettere numframes come samplerate*secondi
print("Array acquisito: ")
print(data)
print("\n")

"""

data,samplerate=sf.read("./pulita_semplice.wav")
print(samplerate)
print(data)
print(len(data))

sf.write("./pulita_semplice.wav",data,samplerate)

#Grafico suono
tempo=np.linspace(0,int(t),len(data))
plt.plot(tempo,data,color="blue")
plt.rcParams["figure.autolayout"]=True
plt.rcParams["figure.figsize"]=[7.5,3.5]
plt.title("Grafico suono")
plt.xlabel("Tempo[s]")
plt.ylabel("Ampiezza audio[u.m]")
plt.show()


