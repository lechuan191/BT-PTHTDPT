import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
con, addr = s.accept()

data1 = con.recv(1024).decode()
data2 = data1.split()
soCau = 0
soChu = 0
def demSoCau(src):
	count = 1
	for i in src:
		if i == '.':
			count +=1
	return count
def demSoChu(src):
	count = len(src)
	return count

soCau = demSoCau(data1)
soChu = demSoChu(data2)

con.sendall(("Tong so cau: "+str(soCau)+"\nTong so chu: "+str(soChu)).encode())

s.close()
