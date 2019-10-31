import socket

HOST = 'localhost'
PORT = 12391                                                                                                                                            
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

print("So tu dog la: %d",dem)

con.sendall(("Tu Dog xuat hien: "+str(dem)).encode())

s.close()
