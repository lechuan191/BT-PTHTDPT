import socket
host="127.0.0.1"
port=54321
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server dang chay")
S.bind((host,port))
S.listen()
Conn,addr=S.accept()
data=Conn.recv(1024)
temp =data.decode()
arr = temp.split()
def tinhTong(list):
    tongDuong=0;
    tongAm=0;
    for x in list:
        if x > 0:
            tongDuong += x
        if x < 0:
            tongAm += x
    return tongDuong,tongAm
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
