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
print("Chuoi client gui:",temp)
arr = temp.split()
print(arr)

def demSoTu(s):
    sotu = len(s)
    return sotu

def demSoTu2(data):
   words = data.split(" ")
   num_words = len(words)
   return num_words

def demTanXuat(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

result = 'Tong so tu: ' + str(demSoTu(arr))+'\nTong so tu cach 2: ' + str(demSoTu2(temp)) +"\nTan xuat xuat hien: " +str(demTanXuat(temp)) 
Conn.sendall(result.encode())