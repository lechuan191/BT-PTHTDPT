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

def isPrime2(n): 
    if (n <= 1): 
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
  
    return True
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
def xuatchuoi(chuoi):
    chuoiAm=""
    chuoiDuong=""
    chuoiChan=""
    chuoiLe=""
    chuoiNguyenTo=""
    for number in chuoi:
        number=int(number)
        if number < 0:
            chuoiAm = chuoiAm+" "+str(number)
        if number > 0:
            chuoiDuong= chuoiDuong+" "+str(number)
        if number % 2 == 0:
            chuoiChan=chuoiChan+" "+str(number)
        else :
            chuoiLe= chuoiLe +" "+str(number)
        if (isPrime2(number)==True):
            chuoiNguyenTo=chuoiNguyenTo+" "+str(number)
    return  chuoiAm, chuoiDuong, chuoiChan, chuoiLe, chuoiNguyenTo
def tinhTongChanLe(chuoi):
    tongChan=""
    tongLe=""
    for i in chuoi:
        y=int(i)
        if y%2== 0:
            tongChan +=" "+y
        else:
            tongLe +=" "+y
    return tongChan,tongLe

def tinhTongSNT(chuoi):
    tongSNT=""
    for i in chuoi:
        x=int(i)
        if isPrime(x)==True:
            tongSNT+=" "+x
    return tongSNT
# tongC, tongL=tinhTongChanLe(arr)
# tongSNT=tinhTongSNT(arr)
chuoiAm,chuoiDuong,chuoiChan,chuoiLe,chuoiNguyenTo=xuatchuoi(arr)
ketQua="Chuoi Duong la :"+str(chuoiDuong)+"\nChuoi Am la :"+str(chuoiAm)+"\nChuoi chan la :"+str(chuoiChan)+"\nChuoi so le la:"+str(chuoiLe)+"\nChuoi so nguyen to la:"+str(chuoiNguyenTo)
con.sendall(ketQua.encode())
s.close()
