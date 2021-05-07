import socket
import sys
import os
import cipher

#change IP and Port as needed
IP = "127.0.0.1"
PORT = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen(5)
clientsocket, address = server.accept()

file_name = input("enter file name ")

f = open(file_name,'rb')
data=f.read(1024)
while data:
	#send
	clientsocket.send(encrypt(data))
	data=f.read(1024)
clientsocket.close()
print("File transfer success!")
	
