from __future__ import print_function

import random
import socket
import time

import settings as hf
import pyfiglet
from consolebar import ConsoleBar

global tgt
global timer

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
        hf.break_line(80)
        print(proj_info.title + ' | Developed by: ' + proj_info.dev)
        hf.break_line(80)

    randomizer()




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
        t1 = time.time()
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
    t1 = time.time()
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

            t2 = time.time()
            global timer
            timer = round(t2 - t1, 2)

            sock.close()

    # printing the report
    def report():
        hf.clear()

        print("REPORT: ")

        def report_data():
            hf.break_line(80)
            hostname_report =   'Target:           ' + tgt.hostname
            ip_report =         'IP address:       ' + tgt.ip
            fqdn_report =       'FQDN:             ' + tgt.fqdn

            print(hostname_report + '\n' + ip_report + '\n' + fqdn_report)
            print('Port range:       ' + str(starting_port) + ' - ' + str(ending_port))
            print('\nScanning finished in ' + str(timer) + ' seconds\n')
            print('\nPort       ' + 'Status    ' + 'Service ')
            hf.break_line(80)

            print(*open_ports, sep='\n')

        report_data()

        hf.break_line(80)

        # exit
        input('\n' * 5 + 'Press any key to continue...')
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
