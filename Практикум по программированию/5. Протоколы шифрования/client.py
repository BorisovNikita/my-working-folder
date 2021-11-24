import socket, random, threading

def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))

def listening(sock):
    global private_key
    while True:
        msg = sock.recv(1024).decode()
        msg = decrypt(private_key, msg)
        print(msg)

b = random.randint(10,99)

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', 10101))

server_key = sock.recv(1024).decode().split("|")
server_key = [int(item) for item in server_key]
myself_b = pow(server_key[1],b)%server_key[2]
private_key = pow(server_key[0],b)%server_key[2]
sock.send((str(myself_b)).encode())

threading.Thread(target = listening, args = (sock, ), daemon = True).start()

while True:
    cmd = input()
    if cmd == "stop":
        break
    cmd = encrypt(private_key, cmd)
    sock.send(cmd.encode())

sock.close()