import socket # import required library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make a socket
mysock.connect('data.pr4e.org', 80) # extend the socket and connect it to a web server on port 80
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # make a request and assign it to a variable
mysock.send(cmd) # send the request

# Prepare to receive data from the web server
while True:
    data = mysock.recv(512) # receive 512 characters at a time
    if len(data) < 1:       # if zero data comes back, 
        break               # break the loop...
    print(data.decode())    # decode data and display the web page
mysock.close()              # ... and close the socket
