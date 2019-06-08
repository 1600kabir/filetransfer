import socket



clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#input IP and Port
clientsocket.connect(("127.0.0.1", 1234))
print("Connected to server...")
filename = input(str("What would you like to name the incoming file?"))

f = open(filename, 'wb')
data = clientsocket.recv(1024)
f.write(data)
print("File transfer success!")



