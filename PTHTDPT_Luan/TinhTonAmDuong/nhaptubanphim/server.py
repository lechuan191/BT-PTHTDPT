import socket
host="127.0.0.1"
port=65433
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server dang chay")
S.bind((host,port))
S.listen()
Conn,addr=S.accept()
data=Conn.recv(1024)
chuoi =str(data.decode())
print ('Noi dung file la:\n', chuoi)
arr = chuoi.split()

def  TinhTongAm(arr): 
	tongAm =0
	for i in arr: 
		if int(i)<0:
			tongAm += int(i)
	return tongAm

def  TinhTongDuong(arr): 
	
	tongDuong =0

	for i in arr: 
		if int(i)>=0:
			tongDuong += int(i)
	return tongDuong



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True





def Le(n):
    a = 0 
    b = 0
    for i in range(1, n+1):
        if i % 2 == 0:
        	a = a + 1
        	
    return  a 
def Chan(n):
    a = 0 
    for i in range(1, n+1):
        if i % 2 == 0:
        	a = a + 1
        	
    return  a 	
       
        	


            
  

#demLe = Le(chuoi)
#demChan  =  Chan(chuoi)

#print("So Chan", demChan)
#print("So Le", demLe)
					
result = 'Tong duong: ' + str(TinhTongDuong(arr)) + 'Tong am: ' + str(TinhTongAm(arr))
# isprime(c) 

#Conn.sendall(str(demLe).encode())
#Conn.sendall(str(demChan).encode())
Conn.sendall(str(result).encode())