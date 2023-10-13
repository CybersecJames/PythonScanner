# import statements
import socket
import os
os.system("pip install consolebar")
os.system("pip install pyfiglet")
import pyfiglet
from consolebar import ConsoleBar


# --------------------------------------------------------------------------------
#  ____        _   _                    ____
# |  _ \ _   _| |_| |__   ___  _ __   / ___|  ___ __ _ _ __  _ __   ___ _ __
# | |_) | | | | __| '_ \ / _ \| '_ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# |  __/| |_| | |_| | | | (_) | | | |  ___) | (_| (_| | | | | | | |  __/ |
# |_|    \__, |\__|_| |_|\___/|_| |_| |____/ \___\__,_|_| |_|_| |_|\___|_|
#        |___/
# --------------------------------------------------------------------------------

# ------------------------------------- PROJECT INFO ------------------------------------------ #
# general project information
class proj_info:
    title = 'Python Scanner'
    dev = 'James Montrief'
    description = 'Python Scanner is a simple port-scanning application written in python.'


# ---------------------------------------- BANNERS -------------------------------------------- #
# clear function
def clear():
    os.system("cls")

# break line
break_line = '--------------------------------------------------------------------------------'
def break_line_alt(dashes):
    print('-' * dashes)

# set up the banner class
class banner:
    def __init__(self, name, header, subtitle, message):
        self.name = name
        self.header = header
        self.subtitle = subtitle
        self.message = message

# welcome banner
welcome_banner = banner(
    name='Welcome Banner',
    header=proj_info.title,
    subtitle=break_line + '\n' + proj_info.title + ' | ' + 'Developed by: ' + proj_info.dev + '\n' + break_line,
    message=proj_info.description,
)

# small banner
small_banner = banner(
    name='Small Banner',
    header=proj_info.title,
    subtitle=proj_info.title + ' | ' + 'Developed by: ' + proj_info.dev,
    message=proj_info.description,
)

def simple_banner():
    pyfiglet.print_figlet(proj_info.title, colors=banner_color)
    print(welcome_banner.subtitle)

# banner colors
banner_color = 'GREEN'
banner_font = 'DOOM'

# ---------------------------------------- WElCOME SCREEN -------------------------------------------- #
# sets the welcome screen
def welcome_screen():
    pyfiglet.print_figlet(text=proj_info.title, colors=banner_color)
    print(welcome_banner.subtitle)

    def pass_screen():
        msg = '\nPress [ENTER] to continue... \n'
        input(msg)

    pass_screen()

    clear()

# -------------------------------------- TARGET ACQUISITION ------------------------------------------ #
# defining the target class
class target:
    def __init__(self, hostname, start_port, end_port):
        self.hostname = hostname
        self.start_port = start_port
        self.end_port = end_port
        self.ip = socket.gethostbyname(hostname)
        self.fqdn = socket.getfqdn(hostname)

# reconnaissance
def recon_target():
    # acquire the target
    simple_banner()
    tgt_prompt = '\nEnter a hostname (e.g. abc.com): \n  >>  '
    tgt = input(tgt_prompt)
    clear()

    # starting port
    simple_banner()
    start_port_prompt = '\nEnter the starting port: '
    start_port = int(input(start_port_prompt + '\n  >>  '))

    clear()

    # ending port
    simple_banner()
    end_port_prompt = '\nEnter the ending port: '
    end_port = int(input(end_port_prompt + '\n  >>  '))

    clear()

    if start_port > end_port:
        recon_target()

    # socket timeout
    simple_banner()
    sock_timeout_prompt = '''Enter the scanning speed: 
    1 - Fastest 
    2 - Medium   
    3 - Slow
    '''

    sock_timeout = int(input(sock_timeout_prompt + '\n  >>  '))
    clear()

    def wait_screen():
        simple_banner()
        message = 'Starting reconnaissance of the target, please wait...'
        print(message)

    wait_screen()

    # recon
    tgt = target(tgt, start_port, end_port)
    clear()
    
    # ---------------------------------------- SCANNING ENGINE ------------------------------------------ #
    # scanning engine
    open_ports = []

    # target information
    simple_banner()
    print('\nScanning target: ' + tgt.hostname)
    print('IP address: ' + tgt.ip)
    print('Scanning ports ' + str(start_port) + ' - ' + str(end_port) + '\n')

    # scanning for ports
    for port in ConsoleBar(range(start_port, end_port)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(sock_timeout / 5)
        result = sock.connect_ex((tgt.ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)

                if port < 99:
                    open_ports.append("Port {}      | Open".format(port) + '     | ' + service)

                elif port > 99:
                    open_ports.append("Port {}     | Open".format(port) + '     | ' + service)

            except:
                if port < 99:
                    open_ports.append("Port {}      | Open".format(port) + '     | ')

                elif port > 99:
                    open_ports.append("Port {}     | Open".format(port) + '     | ')

            sock.close()

    # printing the report
    def report():
        clear()

        print("REPORT: ")
        print(break_line)

        hostname_report = 'Target:           ' + tgt.hostname
        ip_report = 'IP address:       ' + tgt.ip
        fqdn_report = 'FQDN:             ' + tgt.fqdn

        print(hostname_report + '\n' + ip_report + '\n' + fqdn_report)
        print('Port range:       ' + str(start_port) + ' - ' + str(end_port))

        print('\nPort       ' + 'Status    ' + 'Service ')
        print(break_line)

        print(*open_ports, sep='\n')

        print(break_line)

        # exit
        rerun = input('\n' * 3 + 'Press [ENTER] to run another scan, or type "exit" to quit.\n \n')

        if rerun == 'exit':
            clear()
            print('Thank you for using Python Scanner.')
            exit()

        clear()

    report()

# main loop
def main():
    recon_target()
    main()

welcome_screen()

if __name__ == '__main__':
    main()
