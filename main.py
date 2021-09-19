import socket
import settings
import pyfiglet

settings.clear()


# --------------------------------------------------------------------------------
#  ____        _   _                    ____
# |  _ \ _   _| |_| |__   ___  _ __   / ___|  ___ __ _ _ __  _ __   ___ _ __
# | |_) | | | | __| '_ \ / _ \| '_ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# |  __/| |_| | |_| | | | (_) | | | |  ___) | (_| (_| | | | | | | |  __/ |
# |_|    \__, |\__|_| |_|\___/|_| |_| |____/ \___\__,_|_| |_|_| |_|\___|_|
#        |___/
# --------------------------------------------------------------------------------


class proj_info:
    title = 'Python Scanner'
    dev = 'James Montrief'
    description = 'Python Scanner is a simple port scanning application written in python'


pyfiglet.print_figlet(proj_info.title)
settings.breakline(75)


class target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = socket.gethostbyname(hostname)


print('Enter a hostname')
raw = input(' >> ')
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
