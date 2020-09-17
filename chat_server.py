import socket
s = socket.socket()
print("Socket created successfully")
port = 12345
s.bind(('',port))
s.listen()
print("Socket is listening")
c,addr = s.accept()
p = "Hii"
while p != "bye" :
    data = input("Server:",)
    c.send(str.encode(data))
    p = c.recv(1024)
    print("Client:",p.decode())
c.close()
