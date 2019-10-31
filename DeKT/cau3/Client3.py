import socket

HOST = 'localhost'
PORT = 12391

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
content = open('test3.txt', 'r').read()
print("Nội dung trong file test: "+content)
s.sendall(content.encode())
data = s.recv(1024)
print('Số từ dog trong câu:', data.decode())
