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
#send_one_message(s,spin)
array=[[1,2],[4,5],[6,7]]


string_data=[]     

for x in range(0, len(array)):
            n=" ".join([str(array[x][0]),str(array[x][1])])
            string_data.append(n)

print(string_data)           
spin=" ".join(string_data)

data_bit = spin.encode()

divi=1024

chuncks=[]

for i in range(0,len(data_bit),divi):
    chuncks.append(data_bit[i:i+divi])
    
print(chuncks)    
for i in range(0,len(chuncks)):
    s.sendall(chuncks[i])

resault=s.recv(1024) #intenzionale
result=resault.decode()
print("\nIl server risponde ",result)



s.close()
