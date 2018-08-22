import socket
import argparse
from sys import exit

serverAddress = ("0.0.0.0", 9999)

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", nargs='+',
                    help="The message that you would like to send.")
args = parser.parse_args()

if args.message:
    clientData = ' '.join(args.message)
else:
    clientData = raw_input("Tell me something: ")

try:
    clientSocket = socket.socket()
    clientSocket.connect(serverAddress)
except:
    exit("Unable to establish connection to server.")

try:
    clientSocket.send(clientData)
except:
    exit("Unable to send data.")
