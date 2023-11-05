import socket
import struct
import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib





#Crea un socket che permette al server di comunicare con il client
nome=socket.gethostname()    
port=12345  
host=socket.gethostbyname(nome)
print(host)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

print("Host: ",host,", Port: ",port)

s.listen(1)
conn, addr= s.accept()

print("Connected by ",addr)


#Comunicazione client-socket
while True:

    try:
        
       
        data=conn.recv(1024)
        print(data.decode())
       
        if (int(data.decode())> 8*(10**10)):

            conn.send("Troppo grande!".encode())
        else:
            conn.send("Accettato".encode())
        

            length=conn.recv(1024)
            conn.send(str(1024).encode()) #tempo

           
            #metodo per ricevere i dati e riordinarli come una lista di lista 
            a=conn.recv(1024)
            pack=int(a.decode())
            
            dati=''
            print("\nCollezionando dati:)\n ") #cosa riceviamo
            for i in range(1,pack):
                string=conn.recv(1024)
                dati = dati + string.decode()
                
                
            a_str_spl = dati.split()
        
            ints=[]
            for x in range(0, len(a_str_spl)-1, 2):
                n=[float(a_str_spl[x]), float(a_str_spl[x+1])]
                ints.append(n) 
            
            conn.sendall("Ricevuto".encode())
    

            #Il server crea un file di raccolta dei dati registrati     
            f=open("Record_ricevuto.txt","a")
            for x in ints:            #ints                         
                f.write(str(x)+"\n")
                
            f.close()



            #Il server permette di riascolare l'audio
            d=input("\nVuoi riprodurre l'audio?\n(Inserire 1 se si, inserire altro altrimenti)\n")
            if(int(d)==1):
                speakers = sc.all_speakers()
                print("Speaker disponibili: ", speakers, "\n")
                default_speaker = sc.default_speaker()
                print("Speaker selezionato: ", default_speaker, "\n")
                print("Riproducendo l'audio")
                default_speaker.play(ints, samplerate=44100)
                print("L'array dei dati registrati è lungo ", len(ints))
                
            break 
    
    
    except socket.error:
        print("\nC'è un errore! Mannaggia mannaggia\n")
        break

conn.close()
