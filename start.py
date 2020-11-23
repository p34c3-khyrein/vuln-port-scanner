#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# Vuln Port Scanner
now_version = "1.3" 
# This Python file uses the following encoding: utf-8

# =================================================== #
# Created November | Copyright (c) 2020 P34C3_KHYREIN #
# =================================================== #

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################

########################################################################
#                               Import Module
import sys , time , os , json , socket , getopt
from datetime import datetime
########################################################################
#                         Import Module Requirements
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    import pyfiglet
except ImportError:
    print("INSTALL REQUIREMENTS LIBRARY...")
    os.system('pip3 install pyfiglet')
    os.system('pip3 install requests')
    print("\nOpen again...")
    sys.exit()
os.system("clear")
########################################################################
#                        Check Python Version
if sys.version[0] in "2":
    print ("\nVuln Port Scanner Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\t  Vuln Port Scanner \033[1;91mI like to See Ya, Happy \033[0m\n\n")
    exit()
########################################################################
#                               Color
color_list = {
    # reguler
    "reset":"\033[0m",
    "hitam":"\033[0;30m", "b_hitam":"\033[1;30m", "u_hitam":"\033[4;30m", "bg_hitam":"\033[40m", "hi_hitam":"\033[0;90m", "bhi_hitam":"\033[1;90m", "bghi_hitam":"\033[0;100m",
    "merah":"\033[0;31m", "b_merah":"\033[1;31m", "u_merah":"\033[4;31m", "bg_merah":"\033[41m", "hi_merah":"\033[0;91m", "bhi_merah":"\033[1;91m", "bghi_merah":"\033[0;101m",
    "hijau":"\033[0;32m", "b_hijau":"\033[1;32m", "u_hijau":"\033[4;32m", "bg_hijau":"\033[42m", "hi_hijau":"\033[0;92m", "bhi_hijau":"\033[1;92m", "bghi_hijau":"\033[0;102m",
    "kuning":"\033[0;33m","b_kuning":"\033[1;33m","u_kuning":"\033[4;33m","bg_kuning":"\033[43m","hi_kuning":"\033[0;93m","bhi_kuning":"\033[1;93m","bghi_kuning":"\033[0;103m",
    "biru":"\033[0;34m",  "b_biru":"\033[1;34m",  "u_biru":"\033[4;34m",  "bg_biru":"\033[44m",  "hi_biru":"\033[0;94m",  "bhi_biru":"\033[1;94m",  "bghi_biru":"\033[0;104m",
    "ungu":"\033[0;35m",  "b_ungu":"\033[1;35m",  "u_ungu":"\033[4;35m",  "bg_ungu":"\033[45m",  "hi_ungu":"\033[0;95m",  "bhi_ungu":"\033[1;95m",  "bghi_ungu":"\033[0;105m",
    "cyan":"\033[0;36m",  "b_cyan":"\033[1;36m",  "u_cyan":"\033[4;36m",  "bg_cyan":"\033[46m",  "hi_cyan":"\033[0;96m",  "bhi_cyan":"\033[1;96m",  "bghi_cyan":"\033[0;106m",
    "putih":"\033[0;37m", "b_putih":"\033[1;37m", "u_putih":"\033[4;37m", "bg_putih":"\033[47m", "hi_putih":"\033[0;97m", "bhi_putih":"\033[1;97m", "bghi_putih":"\033[0;107m",
}
def color(param):
    if param == True:
        terminal_clear()
        for x in color_list:
            print(color_list["putih"]+"kode warna: "+color_list[x]+x+color_list["putih"])
        sys.exit()
    else:
        try:
            return color_list[param]
        except:
            print('color "'+param+'" tidak tersedia...')
            sys.exit()
B = color("biru"); Y = color("kuning"); G = color("hijau"); W = color("putih"); R = color("merah"); C = color("cyan")
########################################################################
#                               Symbol
symbol_list = {
        "check":"✔","check_green_box":"✅",
        "cross":"✖","cross_red":"❌","cross_green_box":"❎",
        
        "muka_nangis":"😭","muka_sedih":"😥","muka_setan":"😈",
        "muka_kacamata":"😎","muka_love":"😍","muka_ketawa":"😂",
        "muka_senyum1":"😀","muka_senyum2":"😁",
        "muka_jengkel":"😒","muka_datar":"😕",
        
        "seratus":"💯","rantai":"🔗",
        "palu":"🔨","kunci_motor":"🔧","palu_kunci":"🛠",
        "gear":"⚙","pisau":"🔪",
        "kapak":"🪓","tulang":"🦴",
        "hati":"🧡","otak":"🧠","patah_hati":"💔",
        "mercon":"🧨","magnet":"🧲",
        "kompas":"🧭","resep":"🧾",
        "disket":"💾","jangkar":"⚓","map":"🗺",
        "roket":"🚀","sepeda":"🚴","vespa":"🛵","satelit":"🛰",
        "tidak_boleh":"🚫","tidak_boleh_masuk":"⛔","dilarang_masuk_proyek":"🚧",
        "lampu":"💡","lampu_traffic":"🚥",
        "jam_beker":"⏰","jam_tangan":"⌚","stopwatch":"⏱",
        "timbangan":"⚖️","kaca_pembesar":"🔍",
        "tepat_sasaran":"🎯","dua_topeng":"🎭",
        "hp":"📱","telepon":"📞",
        "antena":"📡","pc":"💻",
        "karung_uang":"💰","uang":"💵",
        "kunci_rumah":"🔑","kunci_gembok":"🔐",
        "bell":"🔔","speaker":"🔊",
        "gembok_lock":"🔒","gembok_unlock":"🔓",
        "warning":"⚠",
        "bomb":"💣","ganja":"🍁",
        "injection":"💉","skull":"💀",
        "ghost_1":"👹","ghost_2":"👺","ghost_3":"👻",
        "kacamata":"👓",
        
        "tepuk_tangan":"👏","oke":"👌","dadah":"👋",
        "jempol_atas":"👍","jempol_bawah":"👎",
        
        "text_up":"🆙","text_new":"🆕","text_ok":"🆗",
        "text_sos":"🆘","text_free":"🆓",
        "square_back":"🔙","square_soon":"🔜",
    }
def symbol(param):
    if param == True:
        terminal_clear()
        for x in symbol_list:
            print(x+": "+ symbol_list[x] )
        sys.exit()
    else:
        try:
            return symbol_list[param]
        except:
            print('symbol "'+param+'" tidak tersedia...')
            sys.exit()
########################################################################
#                               Banner
## Font Available
# slant , banner3-D , isometric1 , alligator , alligator2 , banner
# big , binary (:V) , block (bg, color) , chunky , colossal , computer
# contessa , contrast , 

# ok: banner3-D , contessa , contrast , cosmic , drpepper
# ascii_banner = pyfiglet.figlet_format("VULN PORT SCANNER", font="drpepper")
ascii_banner = """
"""+color("b_merah")+""" _ _  _ _  _    _ _  """+color("b_cyan")+"""  ___  ___  ___  ___  """+color("b_hijau")+"""  ___  ___  ___  _ _  _ _  ___  ___
"""+color("b_merah")+"""| | || | || |  | \ | """+color("b_cyan")+""" | . \| . || . \|_ _| """+color("b_hijau")+""" / __>|  _>| . || \ || \ || __>| . \\
"""+color("b_merah")+"""| ' || ' || |_ |   | """+color("b_cyan")+""" |  _/| | ||   / | |  """+color("b_hijau")+""" \__ \| <__|   ||   ||   || _> |   /
"""+color("b_merah")+"""|__/ `___'|___||_\_| """+color("b_cyan")+""" |_|  `___'|_\_\ |_|  """+color("b_hijau")+""" <___/`___/|_|_||_\_||_\_||___>|_\_\\
"""
row_pembatas = 79
########################################################################
#                              Function
def execute(cmd):
    os.system(cmd)
def terminal_clear():
    execute('clear')

def wget(link):
    print (color("kuning") + "DOWNLOAD FILE...\n" + color("merah") + 'execute: ' + color("kuning") + 'wget ' + link + '\n' + color("hijau"))
    execute('wget '+link)

def rename(awal,akhir):
    execute('mv '+awal+' '+akhir)
def rm(link):
    execute('rm '+link)

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

# get info from database
def get_version():
    terminal_clear()
    t0 = time.time()
    try:
        print("Get info from database...")
        response = requests_retry_session().get("https://raw.githubusercontent.com/p34c3-khyrein/version/main/vuln-port-scanner.json",timeout=5,headers={'User-Agent': 'Mozilla/5.0'})
        return json.loads(response.text)
    except Exception as x:
        print('It failed :( ' + x.__class__.__name__ + ', status:' + str(response.status_code) + '\ncontent:\n' + response.text)
        sys.exit()
    else:
        print('It eventually worked ' + response.status_code)
        sys.exit()
    finally:
        t1 = time.time()
        print('Time Took: ' + str(round(t1 - t0, 2)) + ' seconds')
        time.sleep(2)
info = get_version()

def pembatas():
    print(color("b_kuning")+"-" * row_pembatas +color("hijau"))
def banner():
    print("")
    pembatas()
    print(ascii_banner)
    print(color("b_biru")+ "Version: "  + now_version + (" " * (row_pembatas-28)) +color("b_kuning")+ "by " +color("b_hijau")+ "P34C3_KHYREIN")
    pembatas()

# check update sources
if info["version"] != now_version:
    banner()
    print("please update new sources!")
    print("now version: " +color("b_hijau")+ info["version"])
    print(symbol("timbangan") +color("b_ungu")+ "  what's new? : \n")
    info_wn = info['whats_new']
    # info_wn.sort(key=lambda x: x.count, reverse=True)
    for p in info_wn:
        info_update = p['update']
        update = "\n"
        for a in info_update:
            update += "      " + symbol(a["icon"]) +color("b_ungu")+  " : " +color("hijau")+  a["info"] + "\n"
        ok_print = "   "+ symbol("check_green_box") +color("b_biru")+ " [" +color("b_hijau")+ p['version'] +color("b_biru")+ "] " +C+ update
        print( ok_print )
    
    ready = input(color("b_cyan")+ "Ready to Update? (Y/y ~ N/n/*): " +color("b_hijau"))
    if ready == "Y" or ready == "y":
        print("")
        rename(sys.argv[0],"backup.py")
        wget("https://raw.githubusercontent.com/p34c3-khyrein/version/main/vuln-port-scanner.json")
        print(symbol("check_green_box")+" Updated!")
        print(color("b_cyan")+ "please open again!")
    else:
        print(color("b_merah")+ "you should update this file!")
        
    pembatas()
    sys.exit()

def help_information():
    banner()
    print("Example: python3 start.py -t 8.8.8.8")
    print("         python3 start.py -t www.google.com")
########################################################################
#                         Initial Definition

# Get full command-line arguments
full_cmd_arguments = sys.argv
# Keep all but the first
argument_list = full_cmd_arguments[1:]
short_options = "ht:"
long_options = ["help", "target="]
try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    print("Help: python3 start.py -h")
    sys.exit(2)
if len(arguments) == 0:
    help_information()
    sys.exit()

# info port target
port_target = info["port_target"]
########################################################################
#                                 Main
def main(argv):
    # banner print
    banner()
    
    # Evaluate given options
    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            help_information()
        elif current_argument in ("-t", "--target"):
            target = socket.gethostbyname(current_value)
            
            # Information Target and Time
            pembatas() 
            print("Scanning Target: " + target) 
            print("Scanning started at: " + str(datetime.now()))
            
            # Check what time the scan started
            t1 = datetime.now()
            pembatas()
            
            try:
                # will scan ports
                for data in port_target: 
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                    socket.setdefaulttimeout(1) 
                    
                    # returns an error indicator 
                    result = s.connect_ex((target,data["port"])) 
                    if result ==0: 
                        print("{}: Port {} is open".format(data["name"],data["port"])) 
                    s.close()
            except KeyboardInterrupt: 
                    print("\n Exitting Program !!!!") 
                    sys.exit() 
            except socket.gaierror: 
                    print("\n Hostname Could Not Be Resolved !!!!") 
                    sys.exit() 
            except socket.error: 
                    print("\ Server not responding !!!!") 
                    sys.exit()
            pembatas()
            # Checking the time again
            t2 = datetime.now()
            # Calculates the difference of time, to see how long it took to run the script
            total =  t2 - t1
            # Printing the information to screen
            print('Scanning Completed in: ', total )
            pembatas()
    
if __name__ == "__main__":
   main(sys.argv[1:])
   print(color("reset"))
