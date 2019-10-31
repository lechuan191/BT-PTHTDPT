import socket
HOST = "172.16.109.11"
PORT = 1111
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Nhập vào các số nguyên: ")
str = input()
print("Danh sách bạn đã nhập: ", str)
s.sendall(str.encode())
data = s.recv(1024).decode()
print(data)
s.close()

