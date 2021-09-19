import socket


class target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = socket.gethostbyname(hostname)


raw = input('Enter a hostname')
tgt = target(raw)


def scanner():
    for port in range(75, 85):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((tgt.ip, port))

        if result == 0:
            print("Port {}: Open".format(port))

        else:
            print("Port {}: Closed".format(port))
            sock.close()


scanner()
