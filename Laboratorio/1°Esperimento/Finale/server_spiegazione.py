

#Librerie importare.

import socket
import struct
import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib







#Il server prende l'host e la port con cui i client/programmi dovrenno 
#connettersi per poter comunicare.



nome=socket.gethostname()    
port=12345  
host=socket.gethostbyname(nome)
print(host)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
print("Host: ",host,", Port: ",port)






#Il server aspetta possibili collegamenti con client e accetta eventuali
#richieste.



s.listen(1)
conn, addr= s.accept()
print("Connected by ",addr)






#Una volta che il collegamento server-client è avvenuta,
#i due programmi iniziano a scambiarsi informazioni.



while True: #True viene da s.accept()

    try:
        
       
        data=conn.recv(1024)
        print(data.decode())


#Una volta che i due iniziano a comunicare, il server comunica
#la lunghezza del buffer al client.

length=conn.recv(1024)
conn.send(str(1024).encode()) #tempo




#Una volta che il server ha ricevuto il numero di pacchetti
#inizia a collezionare i dati.



n_pack=conn.recv(1024)
pack=int(n_pack.decode())
dati=''
print("\nCollezionando dati:)\n ") #cosa riceviamo
for i in range(1,pack):
    string=conn.recv(1024)
    dati = dati + string.decode()




#Ad ogni pacchetto acquisito, il server riordina la string ricevuta
# e lo trasforma in un array.

    
a_str_spl = dati.split()
ints=[]
for x in range(0, len(a_str_spl)-1, 2):
    n=[float(a_str_spl[x]), float(a_str_spl[x+1])]
    ints.append(n) 




#Il server comunica al client che tutti i pachetti sono arrivati.



conn.sendall("Ricevuto".encode())




#Il server crea un file di raccolta dei dati registrati     




f=open("Record_ricevuto.txt","a")
for x in ints:            #ints                         
    f.write(str(x)+"\n")
    
f.close()





#Il server permette di riascolare l'audio mostrando i possibili speaker
# e riproducendo l'audio dallo speaker di default.



speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
print("Speaker selezionato: ", default_speaker, "\n")
print("Riproducendo l'audio")
default_speaker.play(ints, samplerate=44100)
print("L'array dei dati registrati è lungo ", len(ints))
