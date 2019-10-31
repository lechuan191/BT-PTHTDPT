import socket

HOST = "172.16.109.11"
PORT = 1111
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
con, addr = s.accept()

data = con.recv(1024).decode().split()
soDuong=""
soAm = ""
soChan=""
soLe = ""
soNguyenTo =""
def cau2(n):
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
    	soAm = soAm+" "+str(number)
    if number > 0:
    	soDuong= soDuong+" "+str(number)
    if number % 2 == 0:
        soChan=soChan+" "+str(number)
    else :
        soLe= soLe +" "+str(number)
    if (cau2(number)==True):
        soNguyenTo=soNguyenTo+" "+str(number)
con.sendall(("Các số dương là :"+str(soDuong)+"\nCác số âm là :"+str(soAm)+"\n Các số chẳn là :"+str(soChan)+"\nCác số lẻ là:"+str(soLe)+"\nCác số nguyên tố là :"+str(soNguyenTo)).encode())

s.close()
