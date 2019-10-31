import socket

HOST = "10.14.0.229"
PORT = 3333
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
con, addr = s.accept()

data = con.recv(1024).decode().split()
chuoiDuong=""
chuoiAm = ""
chuoiChan=""
chuoiLe = ""
chuoiNguyenTo =""
def isPrime(n):
  if(n>0):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 
  else:
        return False


for number in data:
    number=int(number)
    if number < 0:
    	chuoiAm = chuoiAm+" "+str(number)
    if number > 0:
    	chuoiDuong= chuoiDuong+" "+str(number)
    if number % 2 == 0:
        chuoiChan=chuoiChan+" "+str(number)
    else :
        chuoiLe= chuoiLe +" "+str(number)
    if (isPrime(number)==True):
        chuoiNguyenTo=chuoiNguyenTo+" "+str(number)
con.sendall(("Chuoi Duong la :"+str(chuoiDuong)+"\nChuoi Am la :"+str(chuoiAm)+"\nChuoi chan la :"+str(chuoiChan)+"\nChuoi so le la:"+str(chuoiLe)+"\nChuoi so nguyen to la:"+str(chuoiNguyenTo)).encode())
#Phương thức decode() Giải mã chuỗi bởi sử dụng encoding đã cho.


s.close()
