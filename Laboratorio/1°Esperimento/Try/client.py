
import socket


host="localhost"
#mettere host=socket.gethostname() per ricavare nome host?

port=12345

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

s.sendall("Ciao pipo!".encode()) #mandiamo questo, prima di encode ci metti cosa vuoi inviare

data=s.recv(1024)
print("Il server risponde", data.decode())

s.close()

