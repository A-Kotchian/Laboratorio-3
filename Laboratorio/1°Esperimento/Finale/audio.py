import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import socket
import struct



#Permette di selezionare un speaker,un microfono e permettono di registrare l'audio
speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
print("Speaker selezionato: ", default_speaker, "\n")


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




#Grafico suono
tempo=np.linspace(0,int(t),len(data))
plt.plot(tempo,data,color="blue")
plt.rcParams["figure.autolayout"]=True
plt.rcParams["figure.figsize"]=[7.5,3.5]
plt.title("Grafico suono")
plt.xlabel("Tempo[s]")
plt.ylabel("Ampiezza audio[u.m]")
plt.show()







#Permette di creare e modificare il file "Record.txt"

d=input("Vuoi salvare i tuoi dati su un file?(Inserire 1 se si, inserire altro altrimenti)\n")


string_data=[]     

for x in range(0, len(data)):
           
            n=" ".join([str(data[x][0]),str(data[x][1])])
            string_data.append(n)
            
spin=" ".join(string_data)



if(int(d)==1):
    f=open("Record.txt","a")
    for x in data:
        f.write(str(x)+"\n")
    f.close()

    

            
#Permette di riprodurre l'audio          
d=input("\nVuoi riprodurre l'audio?\n(Inserire 1 se si, inserire altro altrimenti)\n")
if(int(d)==1):
    print("Riproducendo l'audio")
    default_speaker.play(data, samplerate=44100)
    print("L'array dei dati registrati è lungo ", len(data))




#Permette di far comunicare server e client 
d=input("\nVuoi inviare attraverso i socket il tuo file audio?\n1-Si\n2-No\n")
if(int(d)==1):
    c=input("\nSe avete inserito si, preghiamo di avviare il server per evitare eventuali errori e di inserire 1 quando si è pronti:\n")
    if(int(c)==1):
        name=input("Inserisci host: ")
        host=str(name)
        port=12345
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        
        data_bit = spin.encode()
        s.sendall(str(len(data_bit)).encode()) 
        tempo=1024
        risposta=s.recv(1024)  
        print("Il server risponde: ", risposta.decode())    

        risp=risposta.decode() 
        if risp == "Accettato":
            s.sendall("Quanti sono i byte".encode())
            risposta1=s.recv(tempo)
            div=risposta1.decode() #divisore
            divi = int(div)
            a=0
            if(len(data_bit)%divi==0):
                a=round(len(data_bit)/divi)
                print(a)
            else:
                a=round(len(data_bit)/divi)
                a=a+1
                print(a)

            s.sendall(str(a).encode())

            #Metodo per scomporre i dati e scriverli come un array unico 
            chuncks=[]

            for i in range(0,len(data_bit),divi):
                chuncks.append(data_bit[i:i+divi])
                
            for i in range(0,len(chuncks)):
                s.sendall(chuncks[i])

            resault=s.recv(tempo) #intenzionale
            result=resault.decode()
            print("\nIl server risponde ",result)
        else:
            print("ciao")


        s.close()
        
    else:
        print("\nNessun server rilevato!\nArrivederci")
        
        

else:
    print("Errore,il programma si chiuderà")
    
