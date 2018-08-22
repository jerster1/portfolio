import socket
import argparse
import ipaddress
 
def grab(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
 
        return banner
    except:
        return
 
 
parser = argparse.ArgumentParser()
parser.add_argument("ip_range", metavar="IP RANGE", type=ipaddress.ip_network, required = True,
                    help="The host that you would like to scan.")
parser.add_argument(
    "-p", "--port", help="The port to scan. Default = 21", type=int, default=21)
args = parser.parse_args()
 
ip = socket.gethostbyname_ex(args.ip_range)
port = args.port
 
banner = grab(ip[2][0], port)
 
if banner:
    print(banner)
else:
    print("Not listening on port {}".format(port))