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

arr = chuoi.split()

def KiemTraAmDuong(chuoi): 
        if (int(chuoi)>0):
            return True
        return False
    
def KiemTraChanLe(chuoi): 
        if(int(chuoi)%2==0):
            return True
        return False
if(int(chuoi)==0):
    Conn.sendall(str("So chan va khong am khong duong").encode())


result=""
if(KiemTraChanLe(chuoi)==True):
    result=result+"So Chan va "
else:
    result=result+"So Le va "
    
if(KiemTraAmDuong(chuoi)==True):
    result=result+"Duong"
else:
    result=result+"Am"

Conn.sendall(str(result).encode())

#Conn.sendall(str(result).encode())