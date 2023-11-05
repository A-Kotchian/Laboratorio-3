
#Librerie importare 


import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import socket
import struct



#Il comando socket rileva tutti gli speakers, li mostra sul terminale
# e seleziona come speaker lo speaker di default.


speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
print("Speaker selezionato: ", default_speaker, "\n")




#Il comando rileva tutti gli microfoni, li mostra sul terminale
# e seleziona come microfono lo microfono di default.


mics = sc.all_microphones()
print("Microfoni disponibili: ", mics, "\n")
default_mic = sc.default_microphone()
print("Microfono selezionato: ", default_mic, "\n")



#Il programma inizia a collezionare dati dell'audio registrato 
# microfono di default


print("Registrando: ")
data = default_mic.record(samplerate=44100, numframes=44100*int(t)) #per decidere quanti secondi fare basta mettere numframes come samplerate*secondi
print("Array acquisito: ")
print(data)  #Mostra l'array dei dati registrati
print("\n")


#Grafico suono


t=5     #Durata della registrazione audio
tempo=np.linspace(0,int(t),len(data))
plt.plot(tempo,data,color="blue")
plt.rcParams["figure.autolayout"]=True
plt.rcParams["figure.figsize"]=[7.5,3.5]
plt.title("Grafico suono")
plt.xlabel("Tempo[s]")
plt.ylabel("Ampiezza audio[u.m]")
plt.show()


#(Mettere foto grafico e spiegare per un motivo di ingresso il grafico 
# viene brutto)




#Il programma colleziona i dati e li salva su un file "Record.txt"


f=open("Record.txt","a")
for x in data:
        f.write(str(x)+"\n")
f.close()





#Il programma riscrive l'array in una stringa unica di numeri


string_data=[]     

for x in range(0, len(data)):
           
            n=" ".join([str(data[x][0]),str(data[x][1])])
            string_data.append(n)
            
spin=" ".join(string_data)




#Il programma permette di riascoltare l'audio partendo dall'array dei dati 


print("Riproducendo l'audio")
default_speaker.play(data, samplerate=44100)
print("L'array dei dati registrati è lungo ", len(data))



#Il programma crea una rete tra server e il programma con cui
#possono scambiarsi dei dati attraverso i socket


name="localhost" #Si inserisce l'ip del server
host=str(name)
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))




#Il server  chiede la lunghezza dell'array dei dati


data_bit = spin.encode()
s.sendall(str(len(data_bit)).encode()) 
tempo=1024
risposta=s.recv(1024)  
print("Il server risponde: ", risposta.decode())    






#Il programma una volta che sa la lunghezza massima del buffer
# calcola il numero di pacchetti e invia il numero al server cosi,
# quest'ultimo, può ricostruire l'array di dati.


risp=risposta.decode() 
if risp == "Accettato":
    s.sendall("Quanti sono i byte".encode())
    risposta1=s.recv(tempo)
    div=risposta1.decode() #divisore
    divi = int(div)
    n_pack=0
    if(len(data_bit)%divi==0):
        n_pack=round(len(data_bit)/divi)
        print(n_pack)
    else:
        n_pack=round(len(data_bit)/divi)
        n_pack=n_pack+1
        print(n_pack)

    s.sendall(str(n_pack).encode())





#Il programma inizia a dividere i dati da inviare in piccoli pacchetti 
# più piccoli, ogni pacchetto è un array di dati.



    chuncks=[]

    for i in range(0,len(data_bit),divi):
        chuncks.append(data_bit[i:i+divi])
        
    for i in range(0,len(chuncks)):
        s.sendall(chuncks[i])

    r=s.recv(tempo) 
    result=r.decode()
    print("\nIl server risponde ",result)





else:
    print("\nErrore nessun server rilevato/nessun dato in arrivo/uscita!\n")
        
    s.close()




