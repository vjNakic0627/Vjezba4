import socket
import datetime

host = socket.gethostname()
port=12345
client_socket = socket.socket()
client_socket.connect((host,port))
unos=input(b"Unesi:")
if(unos == 'vaše_ime_prezime'):
    client_socket.sendall(b"Unos nije podrzan")
else:
    client_socket.sendall(unos.encode())

data=client_socket.recv(1024)
print(data)
print(datetime.datetime.now())
client_socket.close()