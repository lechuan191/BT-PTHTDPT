import socket
host="127.0.0.1"
port=54321
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.connect((host,port))
print("Da ket noi voi server")
f = open('tinhTong.txt','r')
text = f.read()
S.sendall(text.encode())
data=S.recv(1024);
print('Server tra lai: ', repr(data.decode()))
