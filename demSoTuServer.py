import socket
HOST = '127.0.0.1'
PORT = 8888       
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024).decode()
list = data.split() 
sotu = len(list)
conn.sendall(str(sotu).encode()) 
s.close()
