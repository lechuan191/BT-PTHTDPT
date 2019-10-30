
import socket
host="127.0.0.1"
port=8888
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server dang chay")
S.bind((host,port))
S.listen()
Conn,addr=S.accept()
data=Conn.recv(1024)
temp =data.decode()
print("Client gui: ",temp)
arr = temp.split(" ")

def tinhTongAD(s):
    tongDuong=0
    tongAm=0
    for i in s:
        if int(i)> 0:
            tongDuong += int(i)
        else:
            tongAm += int(i)
    return tongDuong,tongAm
def tinhTongCL(s):
    tongChan=0
    tongLe=0
    for i in s:
        x=int(i)
        if x%2==0:
            tongChan+=x
        else:
            tongLe+=x
    return tongChan, tongLe

# tongDuong =0
# tongAm =0
# for i in arr: 
#     if int(i)>0:
#         tongDuong += int(i)
#     else:
#         tongAm += int(i)
#result = 'Tong duong: ' + str(tongDuong) + '\nTong am: ' + str(tongAm)

tongD, tongA=tinhTongAD(arr)
tongC, tongL=tinhTongCL(arr)
result = "Tong duong:" + str(tongD) + "\nTong am: "+ str(tongA) +"\nTong chan:" + str(tongC) + "\nTong le: "+ str(tongL)
Conn.sendall(result.encode())