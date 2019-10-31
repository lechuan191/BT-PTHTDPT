import socket
HOST = "10.14.0.229"
PORT = 3333
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Nhap so nguyen: ")
str = input()
print("Ban da nhap: ", str)
s.sendall(str.encode())
data = s.recv(1024).decode()
print(data)
s.close()

