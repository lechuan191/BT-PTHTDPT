import socket
HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
print("Server dang chay")
s.listen()
con, addr = s.accept()
print("Client ket noi: ",addr)
# data = con.recv(1024).decode()
# data2=data.split()
data=con.recv(1024)
temp =data.decode()
print("Client gui: ",temp)
arr = temp.split(" ")
def demTuDog(s):
	count = 0;
	for i in s:
		if i == str('dog'):
			count +=1
	return count
ketQua="So tu dog la: "+str(demTuDog(temp))
con.sendall(ketQua.encode())
s.close()