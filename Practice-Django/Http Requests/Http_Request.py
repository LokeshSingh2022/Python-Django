import socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('www.facebook.com', 80))
cmd = ("GET / HTTP/1.1\r\n\r\nHost: www.google.com\r\n\r\n")
mySock.send(cmd.encode())

while True:
    data = mySock.recv(4096)
    if len(data) < 1:
        break
    else:
        print(str(data.decode()))
mySock.close()