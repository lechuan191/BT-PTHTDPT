import socket
host = "127.0.0.1"
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print("Da ket noi voi server")
f = open('tuvung.txt','r')
text = f.read()
print("Noi dung file: ",text)
s.sendall(text.encode())
data=s.recv(1024);
print('Server tra lai:\n', data.decode())
