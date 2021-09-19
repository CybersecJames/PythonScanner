import socket
import settings
import pyfiglet
from consolebar import ConsoleBar
global tgt

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


# prints the home screen
def home_screen():
    pyfiglet.print_figlet(proj_info.title)


class target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = socket.gethostbyname(hostname)


def target_acquisition():
    print('Enter a hostname')
    raw = input(' >> ')
    global tgt
    tgt = target(raw)


def scanner():
    open_list = []

    for port in ConsoleBar(range(69, 200)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        result = sock.connect_ex((tgt.ip, port))

        if result == 0:
            open_list.append("Port {}: Open".format(port))

            sock.close()

    def report():
        print(open_list)
        input('Press any key to continue...')
        settings.clear()

    report()


def main_loop():
    home_screen()
    target_acquisition()
    scanner()
    main_loop()


main_loop()