import socket
from collections import Counter
host="127.0.0.1"
port=65433
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server dang chay")
S.bind((host,port))
S.listen()
Conn,addr=S.accept()
data=Conn.recv(1024)
chuoi =str(data.decode())

def demChuDog(chuoi):
        num1=chuoi.count(' dog ')
        num2=chuoi.count(' dog.')
        num3=chuoi.count(' dog,')
        num5=chuoi.count(' dog;')
        num6=chuoi.count(' dog:')
        return num1+num2+num3+num5+num6
	
result =str(demChuDog(chuoi))

# isprime(c) 


Conn.sendall(str(result).encode())