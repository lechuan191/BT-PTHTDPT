import socket
host="127.0.0.1"
port=54321
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.connect((host,port))
print("Da ket noi voi server")
# Cau a
#f = open('tinhTong.txt','r')
#text = f.read()
#S.sendall(text.encode())

#Cau b
data=""
print("Nhap 12 so nguyen: ")
for i in range(12):
    a = input("Nhap so thu: "+i)
    if(i==0):
        data = data + a
    else:
        data = data + " " + a
S.sendall(data.encode())
#data=S.recv(1024);
#print('Server tra lai: ', repr(data.decode()))
data1 = S.recv(1024)
data2 = S.recv(1024)
print('Tong cac so am : ', data1.decode())
print('Tong cac so duong : ', data2.decode())
S.close()

