import socket
host="127.0.0.1"
port=65433
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.connect((host,port))
print("Da ket noi voi server")

f = open('nhap.txt', 'r')
str= f.read()
print ('Noi dung file la:\n', str)
S.sendall(str.encode())
data=S.recv(1024);

print('Server tra lai: ', repr(data.decode()))

