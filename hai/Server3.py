import socket

HOST = "172.16.109.11"
PORT=1111                                                                                                                                            
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
con, addr = s.accept()

data1 = con.recv(1024).decode()
data2 = data1.split()

def demTuDog(src):
	count = 0;
	for i in src:
		if i == 'dog':
			count +=1
	return count



dem = demTuDog(data2)

print("dadsad",dem)

con.sendall(("Tu Dog xuat hien: "+str(dem)).encode())

s.close()
