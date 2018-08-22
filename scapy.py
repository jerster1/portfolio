import scapy

send(IP(dst="192.168.86.244",src="192.168.86.192")/TCP(dport=80, sport=1234)//"i am .190 and i got ur packet")