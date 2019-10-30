import socket
host="127.0.0.1"
port=54321
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server dang chay")
S.bind((host,port))
S.listen()
Conn,addr=S.accept()
print("Co ket noi tu ",addr)
data=Conn.recv(1024)
temp =data.decode()
list_text = temp.split()

def tinhTong(listSo):
    tongDuong=0;
    tongAm=0;
    for x in listSo:
        k=int(x)
        if k > 0:
            tongDuong += k
        if k < 0:
            tongAm += k
    return tongDuong,tongAm

data1, data2 = tinhTong(list_text)
Conn.sendall(str(data1).encode())
Conn.sendall(str(data2).encode())
S.close()

'''
tongDuong =0
tongAm =0
for i in arr: 
	tem = int(i)
	if tem>0:
		tongDuong += tem
	else:
		tongAm += tem

result = 'Tong duong: ' + str(tongDuong) + '   ' + 'Tong am: ' + str(tongAm)
Conn.sendall(result.encode())

'''
