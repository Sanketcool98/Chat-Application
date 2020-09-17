import socket
s = socket.socket()
port = 12345
s.connect(('192.168.2.116',12345))
d1 = "Hii"
while d1 != "bye":
    q = s.recv(1024)
    print("Server:",q.decode())
    d1 = input("Client:",)
    s.send(str.encode(d1))
s.close()
