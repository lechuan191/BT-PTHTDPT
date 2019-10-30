import socket
host = "127.0.0.1"
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print("Da ket noi voi server")
# cau 1a
f = open('tongsoad.txt','r')
text = f.read()
print("Du lieu doc tu file: ",text)
s.sendall(text.encode())
data=s.recv(1024);
print('Server tra lai:\n', data.decode())

# cau 1 b 
# data = ""
# i = 0
# print("Nhap 10 so nguyen: ")
# for i in range(5):
#     a = input("Nhap so thu %d:" %(i+1))
#     data = data +" " + a
# # kq=data+" "
# s.sendall(data.encode())
# data=s.recv(1024);
# print('Server tra lai: ', data.decode())


