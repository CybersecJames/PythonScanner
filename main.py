from __future__ import print_function
import socket
import settings as hf
import pyfiglet
from consolebar import ConsoleBar

global tgt

hf.break_line(80)
hf.clear()


# --------------------------------------------------------------------------------
#  ____        _   _                    ____
# |  _ \ _   _| |_| |__   ___  _ __   / ___|  ___ __ _ _ __  _ __   ___ _ __
# | |_) | | | | __| '_ \ / _ \| '_ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# |  __/| |_| | |_| | | | (_) | | | |  ___) | (_| (_| | | | | | | |  __/ |
# |_|    \__, |\__|_| |_|\___/|_| |_| |____/ \___\__,_|_| |_|_| |_|\___|_|
#        |___/
# --------------------------------------------------------------------------------


# basic project info
class proj_info:
    title = 'Python Scanner'
    dev = 'James Montrief'
    description = 'Python Scanner is a simple port scanning application written in python'


# prints the home screen
def home_screen():
    pyfiglet.print_figlet(proj_info.title)
    hf.break_line(80)


# defining the target class
class target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = socket.gethostbyname(hostname)


# getting the target
def target_acquisition():
    print('\nEnter a hostname (e.g. abc.com) : \n')
    raw = input(' >> ')
    global tgt
    tgt = target(raw)
    hf.clear()
    home_screen()
    print('\nScanning: ' + raw)
    print('IP address: ' + tgt.ip + '\n')
    hf.break_line(80)
    print(' ')


# the scanning engine
def scanner():
    open_ports = []

    for port in ConsoleBar(range(60, 100)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((tgt.ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
                open_ports.append("Port {}  | Open".format(port) + '     | ' + service)

            except:
                open_ports.append("Port {}  | Open   ".format(port) + '  | ')

            sock.close()

    # printing the report
    def report():
        # clear the screen and print the main screen
        hf.clear()
        home_screen()

        # print out target and ip
        print('Target: ' + tgt.hostname)
        print('IP address: ' + tgt.ip)

        # header
        print('\nPort       ' + 'Status    ' + 'Service ')
        hf.break_line(80)

        # printing the open_ports list
        print(*open_ports, sep='\n')

        hf.break_line(80)

        # exit
        input('\nPress any key to continue...')
        hf.clear()

    report()


# main loop
def main():
    home_screen()
    target_acquisition()
    scanner()
    main()


if __name__ == '__main__':
    main()
