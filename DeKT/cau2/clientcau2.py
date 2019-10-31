import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("Nhap chuoi:")
x=input()
print("Noi dung ban vua nhap: "+x)
s.sendall(x.encode())
data = s.recv(1024).decode()
print("Server tra ve: \n",data)
s.close()
