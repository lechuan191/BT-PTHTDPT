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

def demCau(chuoi):
	num=chuoi.count('.')
	return num
	
def demDong(chuoi):
	num2=chuoi.count('\n')+1
	return num2
	
	
result = "So cau:"+str(demCau(chuoi)) +"\n So dong:"+str(demDong(chuoi))

# isprime(c) 


Conn.sendall(str(result).encode())