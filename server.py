# pylint: disable=E1601,E1101

import socket

serverAddress = ('0.0.0.0', 9999) #ip listening to all addresses

try:
    serverSocket = socket.socket()
    serverSocket.bind(serverAddress) #tells socket where to listen
    serverSocket.listen(10) #starts the server (Maximum number of connections)
    print "Now listening on %s:%s" % (serverAddress)
except:
    print "Unable to bind to %s on port %s" % (serverAddress)

while True:
    try:
        connection, address = serverSocket.accept() #returns a socket and the address
        buf = connection.recv(2048) #recive 2048 bytes
        if len(buf) > 0: #if recive anything >0 bytes, goto print
            print "Received message: %s" % (buf)
    except KeyboardInterrupt:
        print "Closing server..."
        break
