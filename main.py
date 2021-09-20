from __future__ import print_function

import random
import socket
import settings as hf
import pyfiglet
from consolebar import ConsoleBar

global tgt

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
    def randomizer():
        fonts = ['doom']
        colors = ['GREEN']

        random_font = random.choice(fonts)
        random_color = random.choice(colors)
        pyfiglet.print_figlet(proj_info.title, font=random_font, colors=random_color)

    randomizer()

    hf.break_line(80)


def mini_banner():
    pyfiglet.print_figlet(proj_info.title, font='doom', colors='GREEN')
    hf.break_line(80)


# defining the target class
class target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = socket.gethostbyname(hostname)
        self.fqdn = socket.getfqdn(hostname)


# getting the target
def target_acquisition():
    print('\nEnter a hostname (e.g. abc.com) : \n')
    raw = input(' >> ')
    if raw == '99':
        hf.clear()
        main()
    else:
        global tgt
        try:
            tgt = target(raw)
            hf.clear()
            mini_banner()
            print('\nScanning: ' + raw)
            print('IP address: ' + tgt.ip + '\n')
            hf.break_line(80)
            print(' ')
        except:
            main()


# the scanning engine
def scanner():
    open_ports = []

    starting_port = 75
    ending_port = 100

    for port in ConsoleBar(range(starting_port, ending_port)):
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
        hf.clear()

        def report_data():
            hf.break_line(80)
            hostname_report =   'Target:                ' + tgt.hostname
            ip_report =         'IP address:            ' + tgt.ip
            fqdn_report =       'FQDN:                  ' + tgt.fqdn

            print(hostname_report + '\n' + ip_report + '\n' + fqdn_report)

        print("REPORT: ")
        report_data()

        print('Port range:            ' + str(starting_port) + ' - ' + str(ending_port))

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
