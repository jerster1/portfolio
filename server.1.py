# pylint: disable=E1601,E1101

import socket

serverAddress = ('0.0.0.0', 9999)

try:
    serverSocket = socket.socket()
    serverSocket.bind(serverAddress)
    serverSocket.listen(10)
    print "Now listening on %s:%s" % (serverAddress)
except:
    print "Unable to bind to %s on port %s" % (serverAddress)

while True:
    try:
        connection, address = serverSocket.accept()
        buf = connection.recv(2048)
        if len(buf) > 0:
            print "Received message: %s" % (buf)
    except KeyboardInterrupt:
        print "Closing server..."
        break
