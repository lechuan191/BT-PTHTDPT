import socket
HOST = '127.0.0.1'
PORT = 8888 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
f = open("demSoTu.txt", "r") 
text = f.read()
f.close()
s.send(text.encode()) 
data = s.recv(1024)
print('So tu trong file: ', data.decode()) 
s.close()
