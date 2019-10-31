import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
# nhap chuoi cach nhau khoang trang
print("Nhap day so:")
value=[]
i=0
for i in range(10):
    a = input("Nhap so:")
    value.append(a.split(" "))


print("Noi dung nhap: "+value)
s.sendall(value.encode())

# print("Noi dung nhap: "+x)
# s.sendall(x.encode())
data = s.recv(1024).decode()
print("Server tra ve: \n",data)
s.close()
