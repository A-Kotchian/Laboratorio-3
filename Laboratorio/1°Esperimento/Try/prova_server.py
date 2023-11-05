import socket
import struct

import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib






host="localhost"    
port=12345  

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

print("Host: ",host,", Port: ",port)

s.listen(1)
conn, addr= s.accept()

print("Connected by ",addr)

while True:

    try:
            dati=''
            print("\nCollezionando dati:)\n ") #cosa riceviamo
            for i in range(1,2):
                string=conn.recv(1024)
                dati = dati + string.decode()
                print(dati)

                
                
            a_str_spl = dati.split()
        
            ints=[]
            for x in range(0, len(a_str_spl)-1, 2):
                n=[float(a_str_spl[x]), float(a_str_spl[x+1])]
                ints.append(n) 
                print("Ciaouuuu")
            
            conn.sendall("Ricevuto".encode())
    

        


            f=open("Record_ricevuto.txt","a")
            for x in ints:            #ints                         
                f.write(str(x)+"\n")
                
            f.close()
                
            break 
    
    
    except socket.error:
        print("\nC'è un errore! Mannaggia mannaggia\n")
        break
#else:   
       # print("Mi dispiace,non abbiamo collezionato nessun dato :(".encode())

conn.close()
