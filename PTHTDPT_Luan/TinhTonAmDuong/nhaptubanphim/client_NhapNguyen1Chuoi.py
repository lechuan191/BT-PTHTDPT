import socket
host="127.0.0.1"
port=65433
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.connect((host,port))
print("Da ket noi voi server")
#a=input(str("nhap so:"))
#S.sendall(a.encode())
#S.sendall(b.encode())
inputChuoi=input('Nhap chuoi:')

S.sendall(inputChuoi.encode())
data=S.recv(1024);

print('Server tra lai: ', repr(data.decode()))
#print('Server tra lai: ', repr(data.decode()))
#print('Server tra lai: ', repr(data.decode()))

