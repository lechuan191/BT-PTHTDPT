import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

f = open("test2.txt","r")
data = f.read()
print("Noi dung trong file test: "+data)
s.sendall(data.encode())
data = s.recv(1024).decode()
print(data)
s.close()
