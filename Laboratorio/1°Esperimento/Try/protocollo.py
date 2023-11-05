import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import socket
import struct

host="localhost"
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
data_bit = spin.encode()
s.send(len(data_bit).encode()) 
tempo=1024

risposta=s.recv(tempo)  
print("Il server risponde: ", risposta.decode())

risp=risposta.decode() 




if risp == "accettato":
    s.send("Quanti sono i byte".encode())
    risposta1=s.recv(tempo)
    div=risposta1.decode() #divisore
    a=0
    if(len(data_bit)%div==0):
        a=len(data_bit)/div
    else:
        a=len(data_bit)/div
        a=a+1
    
    chuncks=[]

    for i in range(0,len(data_bit),int(div)):
        chuncks.append(data_bit[i:i+int(div)])
    for i in range(0,len(chuncks)):
        s.sendall(chuncks[i].encode())

else:
    print("ciao")
s.send
s.close()