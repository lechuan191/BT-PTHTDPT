import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
print("Server dang chay")
s.listen()
con, addr = s.accept()
print("Client ket noi: ",addr)
data = con.recv(1024).decode().split()

def isPrime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 
def tinhTongChanLe(chuoi):
    tongChan=0
    tongLe=0
    for i in chuoi:
        if int(i)%2== 0:
            tongChan += int(i)
        else:
            tongLe += int(i)
    return tongChan,tongLe
def tinhTongChan(chuoi):
    tongChan=0
    for i in chuoi:
        x=int(i)
        if x%2== 0:
            tongChan += x
    return tongChan
def tinhTongLe(chuoi):
    tongLe=0
    for i in chuoi:
        x=int(i)
        if x%2!=0:
            tongLe += x
    return tongLe
def tinhTongSNT(chuoi):
    tongSNT=0
    for i in chuoi:
        x=int(i)
        if isPrime(x)==True:
            tongSNT+=x
    return tongSNT
tongC, tongL=tinhTongChanLe(data)
#tongC=tinhTongChan(data)
#tongL=tinhTongLe(data)
tongSNT=tinhTongSNT(data)

ketQua="Tong so chan la : "+str(tongC)+"\nTong so le la: "+str(tongL)+"\nTong So nguyen to: "+str(tongSNT)
con.sendall(ketQua.encode())
s.close()
