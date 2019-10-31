import socket

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
print("Server dang chay")
s.listen()
con, addr = s.accept()
print("Client ket noi: ",addr)
data = con.recv(1024).decode()

# def kiemTraChanLe(n):
#     if n%2 == 0:
#         return "So chan"
#     else:
#         return "So le"

def kiemTraChanLe2(number):
    x=int(number)
    y = x % 2
    if y == 0:
        return True
    else:
        return False
        
kiemtra=kiemTraChanLe2(data)
if kiemtra==True:
    kq="Chan"
else:
    kq="Le"
con.sendall(str(kq).encode())
s.close()
