import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("Da ket noi den server")
f = open("test1b.txt","r")
data = f.read()
print("Noi dung file: "+data)
s.sendall(data.encode())
data = s.recv(1024).decode()
print("Server tra ve: \n",data)
s.close()
