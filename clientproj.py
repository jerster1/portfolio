import socket
import argparse
from sys import exit

serverAddress = [("127.0.0.1")]


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", nargs='+',
                    help="the port you want to add")
args = parser.parse_args()

if args.port:
    clientData = ' '.join(args.port)
else:
    clientData = raw_input("whats the port number: ")
    int(clientData)
    serverAddress.append(clientData)
    print serverAddress
    print clientData

try:
    clientSocket = socket.socket()
    print serverAddress
    clientSocket.connect(serverAddress)
except:
    exit("Unable to establish connection to server.")

try:
    clientSocket.send(clientData)
except:
    exit("Unable to send data.")