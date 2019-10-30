
import socket
host="127.0.0.1"
port=8888
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server dang chay")
S.bind((host,port))
S.listen()
Conn,addr=S.accept()
data=Conn.recv(1024)
chuoi =data.decode()
print("Chuoi client gui:",chuoi)

def demSoCau(s):
    dem=0
    for i in s:
        if i==".":
            dem +=1
    return dem

def demSoCau2(s):
    num=s.count(".")
    return num;

def demSoDong(s):
    lines = s.split("\n")
    for l in lines:
      if not l:
         lines.remove(l)
    return len(lines)
def demSoDong2(s):
    num=s.count("\n")+1
    return num;
result = "Tong so cau: "+str(demSoCau(chuoi))+"\nTong so cau cach 2: "+str(demSoCau2(chuoi))+"\nTong so dong: "+str(demSoDong(chuoi))+"\nTong so dong cach 2: "+str(demSoDong2(chuoi))

Conn.sendall(result.encode())


# count = 0
# with open("tuvung.txt",'r') as f:
#      for line in f:
#        split_words = line.split()
#        for word in split_words:
#          for char in word:
#            if(char=="."):
#              count = count + 1

# print("Tong so cau la:",count)