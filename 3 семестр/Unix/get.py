import socket
host = input("Введите хост: ")
recource = input("Введите ресурс: ")
if not host:
    host = "192.168.1.34"
if not recource:
    recource = "a1.com"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 

s.connect((host , 80))
s.send(f"GET / HTTP/1.1\r\nHost: {recource}\r\n\r\n".encode())
print(s.recv(4096))
s.close

