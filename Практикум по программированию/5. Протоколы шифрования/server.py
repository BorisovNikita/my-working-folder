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

def get_keys():
    try:
        with open("server_key.txt", "r") as keyfile:
            keys = keyfile.readline()
        keys = [int(item) for item in keys.split("|")]
    except FileNotFoundError:
        a, g, p = (random.randint(10,99) for _ in range(3))
        myself_a = pow(g,a)%p
        public_key = (myself_a, g, p)


get_keys()


sock = socket.socket()
sock.setblocking(True)
sock.bind(('', 10101))
sock.listen(0)

conn, addr = sock.accept()

conn.send("{0}|{1}|{2}".format(*public_key).encode())
client_b = conn.recv(1024)
private_key = pow(int(client_b),a)%p

threading.Thread(target = listening, args = (conn, ), daemon = True).start()
        
while True:
    cmd = input()
    if cmd == "stop":
        break
    cmd = encrypt(private_key, cmd)
    conn.send(cmd.encode())

sock.close()