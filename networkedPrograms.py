import socket # import required library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make a socket
mysock.connect('data.pr4e.org', 80) # extend the socket and connect it to a web server on port 80
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # make a request and assign it to a variable
mysock.send(cmd) # send the request

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
