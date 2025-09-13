import subprocess
import ctypes
import requests 
import urllib
import pkg_resources
import platform
import shutil
import zipfile
import tarfile
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
import sys, os, time, random, threading

RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'

def check_requirements():
    """Checks if all packages from requirements.txt are installed, and installs them if not."""
    print("{0}[{2}#{0}] {2}Checking Python packages...".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    try:
        with open('requirements.txt', 'r') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        missing_packages = []
        for package in requirements:
            try:
                pkg_resources.get_distribution(package.split('==')[0])
            except pkg_resources.DistributionNotFound:
                missing_packages.append(package)

        if not missing_packages:
            print("{0}[{2}#{0}] {3}All Python packages are installed.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
            sleep(1)
        else:
            print("{0}[{2}#{0}] {2}Missing packages: {YELLOW}{1}{2}. Installing...".format(RED, ', '.join(missing_packages), CYAN, GREEN, DEFAULT, YELLOW))
            for package in missing_packages:
                system(f"pip install {package}")

    except FileNotFoundError:
        print("{0}[{2}#{0}] {YELLOW}requirements.txt not found. Skipping package check.".format(RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW))
        sleep(2)
    except Exception as e:
        print(f"{RED}[!] An error occurred while checking/installing packages: {e}")
        sleep(2)

def net():
    system('clear')
    print("{0}[{2}#{0}] {2}Checking for internet connection{2}....".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
    sleep(1)
    try:
        requests.get("https://google.com", timeout=5)
        print("\n{0}[{2}#{0}] {3}INTERNET {0}- {3}[{2}CONNECTED{3}]".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        sleep(1)
    except (requests.ConnectionError, requests.Timeout):
        print("\n{0}[{2}#{0}] {3}INTERNET {0}- {3}[{2}NOT-CONNECTED{3}]".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        print("{0}[{2}#{0}] {2}Turn on your internet connection\n\n".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        exit()
        
def verCheck():
    try:
        print("\n{0}[{2}#{0}] {2}Checking For Updates{2}...".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        response = requests.get('https://raw.githubusercontent.com/AsHfIEXE/Cypher/main/version.txt', timeout=5).text.strip()
        with open("version.txt", "r") as f:
            local_version = f.read().strip()
        if local_version == response:
            print("{0}[{2}#{0}] {2}[Up-To-Date]- {0}v {6}{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, response))
        else:
            print("\n{0}[{2}#{0}] {2}A newer version is available.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
            print("{0}[{2}#{0}] {0}[{2}Current{0}]{2}- {0}v {6}\n{0}[{2}#{0}] {0}[{2}Available{0}]{2}- {0}v {7}".format(RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, local_version, response)) 
            update_choice = input("{0}[{2}#{0}] {2}Do you want to update now? (y/n): ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW)).lower()
            if update_choice == 'y':
                print("{0}[{2}#{0}] {2}Updating to v{6}... Please wait....{7}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, response, GREEN2))
                system('git fetch --quiet; git reset --hard origin/main --quiet; git pull --quiet')
                print("\n\n\n\t\t{2}[{0}#{2}] {0}Update complete! Please restart the program.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
                exit()
    except Exception as e:
        print(f"{RED}[!] Could not check for updates: {e}")
        pass

def check_tool(tool_name):
    """Checks if a command-line tool is installed."""
    if shutil.which(tool_name):
        print(" {0}[{2}*{0}] {2}{3} INSTALLATION FOUND....".format(RED, WHITE, CYAN, tool_name.upper()))
        sleep(1)
        return True
    else:
        print("{0}[{2}*{0}] {2}{3} NOT FOUND".format(RED, WHITE, CYAN, tool_name.upper()))
        if systemos() == "Linux":
            print(" {0}[{2}*{0}] {2}Installing {3}... ".format(RED, WHITE, CYAN, tool_name))
            system(f'apt-get install {tool_name} -y > /dev/null')
            if not shutil.which(tool_name):
                print(f"{RED}[!] Failed to install {tool_name}. Please install it manually.")
                exit()
        else:
            print(f"{RED}[!] {tool_name} is not installed. Please install it manually.")
            exit()
        return False

def checkPHP():
    check_tool('php')

def checkwget():
    check_tool('wget')

def checkjp2a():
    check_tool('jp2a')

def checkNgrok():
    ngrok_path = os.path.join('Server', 'ngrok.exe' if systemos() == "Windows" else 'ngrok')
    if not path.isfile(ngrok_path):
        print(' {0}[{2}*{0}]{2} Ngrok Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Ngrok...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        
        ostype = systemos().lower()
        arch = architecture()[0]
        machine = platform.machine()

        filename = None
        if 'linux' in ostype:
            if 'aarch64' in machine or 'arm' in machine:
                filename = 'ngrok-v3-stable-linux-arm.tgz'
            elif '64' in arch:
                filename = 'ngrok-v3-stable-linux-amd64.tgz'
            else:
                filename = 'ngrok-v3-stable-linux-386.tgz'
        elif 'darwin' in ostype:
            if 'arm64' in machine: # For Apple Silicon
                 filename = 'ngrok-v3-stable-darwin-arm64.zip'
            else: # Assuming amd64 for other Macs
                filename = 'ngrok-v3-stable-darwin-amd64.zip'
        elif 'windows' in ostype:
            if '64' in arch:
                filename = 'ngrok-v3-stable-windows-amd64.zip'
            else:
                filename = 'ngrok-v3-stable-windows-386.zip'
        
        if not filename:
            print(f"{RED}[!] Unsupported OS/Architecture for Ngrok: {ostype}/{arch}/{machine}")
            exit()

        url = 'https://ngrok-agent.s3.amazonaws.com/' + filename
        
        try:
            print(f'{GREEN}[*] Downloading {filename}...{DEFAULT}')
            response = requests.get(url, stream=True)
            response.raise_for_status()

            download_path = os.path.join(os.getcwd(), filename)
            with open(download_path, "wb") as file_obj:
                for chunk in response.iter_content(chunk_size=8192):
                    file_obj.write(chunk)
            
            extract_dir = os.getcwd()
            if filename.endswith('.zip'):
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)
            elif filename.endswith('.tgz'):
                with tarfile.open(download_path, 'r:gz') as tar_ref:
                    tar_ref.extractall(extract_dir)
            
            executable_name = 'ngrok.exe' if 'windows' in ostype else 'ngrok'
            extracted_executable_path = os.path.join(extract_dir, executable_name)

            if not os.path.exists(extracted_executable_path):
                print(f"{RED}[!] Could not find '{executable_name}' after extraction.")
                exit()

            shutil.move(extracted_executable_path, ngrok_path)
            os.remove(download_path)
            
            if not 'windows' in ostype:
                os.chmod(ngrok_path, 0o755)
            
            system('clear')
            print("\n\n\n\t\t{2}[{0}#{2}] {0}Ngrok downloaded successfully! Please restart the program.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
            exit()
        except Exception as e:
            print(f"{RED}[!] Error downloading or setting up ngrok: {e}")
            print(f"{YELLOW}[!] Please try downloading ngrok manually from https://ngrok.com/download and place it in the 'Server' directory.")
            return False
    else:
        print(" {0}[{2}*{0}] {2}NGROK INSTALLATION FOUND......".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
        return True

def checkLocalxpose():
    loclx_path = os.path.join('Server', 'loclx.exe' if systemos() == "Windows" else 'loclx')
    if not path.isfile(loclx_path):
        print(' {0}[{2}*{0}]{2} Localxpose Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Localxpose...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        
        ostype = systemos().lower()
        machine = platform.machine()

        filename = None
        if 'linux' in ostype:
            if 'arm' in machine:
                filename = 'loclx-linux-arm.zip'
            elif 'amd64' in machine:
                filename = 'loclx-linux-amd64.zip'
        elif 'windows' in ostype:
             filename = 'loclx-windows-amd64.zip'
        
        if not filename:
            print(f"{RED}[!] Localxpose not available for your OS/Architecture: {ostype}/{machine}")
            return

        url = 'https://api.localxpose.io/api/v2/downloads/'+filename
        try:
            print(f'{GREEN}[*] Downloading {filename}...{DEFAULT}')
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(filename, "wb") as file_obj:
                for chunk in response.iter_content(chunk_size=8192):
                    file_obj.write(chunk)

            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall('.')
            
            extracted_exe = 'loclx.exe' if 'windows' in ostype else 'loclx'
            if not os.path.exists(extracted_exe):
                for item in os.listdir('.'):
                    if 'loclx' in item and not item.endswith('.zip'):
                        extracted_exe = item
                        break

            shutil.move(extracted_exe, loclx_path)
            os.remove(filename)

            if not 'windows' in ostype:
                os.chmod(loclx_path, 0o755)

            system('clear')
            print("\n\n\n\t\t{2}[{0}#{2}] {0}Localxpose downloaded successfully! Please restart the program.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
            exit()
        except Exception as e:
            print(f"{RED}[!] Error downloading or setting up Localxpose: {e}")
            print(f"{YELLOW}[!] Please try downloading it manually from https://localxpose.io/download and place it in the 'Server' directory.")
            exit()
    else:
        print(" {0}[{2}*{0}] {2}LOCALXPOSE INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)

def loop():
    """This function previously contained obfuscated, potentially malicious code. It has been disabled."""
    pass

def loadingHack():
    chaine ="/////////////////////"+"[*]"+" Starting Cypher......"+"/////////////////////".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)
    charspec = "$*X^%\#~?;"
    i=0
    while i<4:
        chainehack = ""
        i +=1
        for c in chaine:
            chainehack += c
            r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
            if len(chainehack+r) > len(chaine):
                r = ""
            sys.stdout.write('\r'+chainehack+r)
            time.sleep(0.006)

def loadingTextPrint():
    string ="                    "+"[*]"+" Starting Cypher......"
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
