from colorama import Fore
import os
import platform
import time
import shutil


def doxxer():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{Fore.RED}
        ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   
        █ ▄▀   █ █      █ █    █   █ █    █   █ █   █  █  █  █ █ █ █         
        ▐ █    █ █      █ ▐     ▀▄▀  ▐     ▀▄▀  ▐   █  ▐  ▐  █  ▀█ █    ▀▄▄  
          █    █ ▀▄    ▄▀      ▄▀ █       ▄▀ █      █       █   █  █     █ █ 
         ▄▀▄▄▄▄▀   ▀▀▀▀       █  ▄▀      █  ▄▀   ▄▀▀▀▀▀▄  ▄▀   █   ▐▀▄▄▄▄▀ ▐ 
        █     ▐             ▄▀  ▄▀     ▄▀  ▄▀   █       █ █    ▐   ▐         
        ▐                  █    ▐     █    ▐    ▐       ▐ ▐                  
  |--------------------------------------------------------------------------------------------|
  | [1] Doxxer-Toolkit - Kit complete Doxxing for linux and termux.                          |
  | [2] Garuda  -  Doxxing Toolkit for: full name, IP, phone number.               |
  | [3] LineX - Tool for obtaining phone number information.                        |
  | [4] IPlogger - IPlogger from terminal for linux and termux.                                |
  | [00] Return to main menu                                                            |
  | [99] Quit                                                                                 |
  |--------------------------------------------------------------------------------------------|
  """)
    var = input(f'\n{Fore.BLUE}root@fuckyou:~# ')
    # Doxxer-toolkit ---
    if var == "1":
        if os.path.exists('tools/Doxxer-Toolkit'):
            print(f'\n{Fore.RED}[!] Doxxer-Toolkit already exists')
            ques = input(
                f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
            if ques == "Y" or ques == "y":
                os.system("python3 tools/Doxxer-Toolkit/dox.py")
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing Doxxer-Toolkit...')
                os.system(
                    "git clone https://github.com/Euronymou5/Doxxer-Toolkit && mv 'Doxxer-Toolkit' tools/ && bash tools/Doxxer-Toolkit/install.sh"
                )
                print('\n[~] Doxxer-Toolkit installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] Doxxer-Toolkit is not available for your operating system.'
                )
    # Garuda --
    elif var == "2":
        if os.path.exists('tools/Garuda'):
            print(f'\n{Fore.RED}[!] Garuda already exists')
            ques = input(
                f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
            if ques == "Y" or ques == "y":
                print("""
        Arguments:

        --name     Doxxear full name

        --ip       Doxxear IP address

        --mail     Doxxear email

        --phone    Doxxear telephone number

        --user     Doxxear Username
        """)
                arg = input(
                    f'{Fore.BLUE}\n[~] Enter a garuda argument: ')
                if arg == "--name" or arg == "--ip" or arg == "--mail" or arg == "--phone" or arg == "--user":
                    os.system(f"python3 tools/Garuda/garuda.py {arg}")
                else:
                    print(
                        f'\n{Fore.RED}[!] Error you must enter an argument.')
                    time.sleep(2)
                    doxxer()
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing Garuda...')
                os.system(
                    "git clone https://github.com/noob-coder123/Garuda && mv 'Garuda' tools/ && pip install -r tools/Garuda/requirements.txt "
                )
                print(f'\n[~] Garuda installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] Garuda is not available for your operating system.'
                )
    # LineX  ------
    elif var == "3":
        if os.path.exists('tools/LineX'):
            print(f'\n{Fore.RED}[!] LineX already exists')
            ques = input(
                f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
            if ques == "Y" or ques == "y":
                if platform.system() == "Linux":
                    os.system("python3 tools/LineX/linex.py")
                elif platform.system() == "Windows":
                    os.system("python tools/LineX/linex_win.py")
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing LineX...')
                os.system(
                    "git clone https://github.com/Euronymou5/LineX.git && mv 'LineX' tools/ && pip install requests"
                )
                print('\n[~] LineX installed successfully.')
                time.sleep(2)
                doxxer()
            elif platform.system() == "Windows":
                print(f'\n{Fore.GREEN}[~] Installing LineX...')
                os.system("git clone https://github.com/Euronymou5/LineX.git")
                shutil.move("LineX/", "tools")
                os.system("pip install requests")
                print('\n[~] LineX installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] LineX is not available for your operating system.'
                )
    # IPlogger ----
    elif var == "4":
        if os.path.exists('tools/IPlogger'):
            print(f'\n{Fore.RED}[!] IPlogger already exists')
            ques = input(
                f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
            if ques == "Y" or ques == "y":
                os.system("python3 tools/IPlogger/run.py")
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing IPlogger...')
                os.system(
                    "git clone https://github.com/Euronymou5/IPlogger && mv 'IPlogger' tools/"
                )
                print('\n[~] IPlogger installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] IPlogger is not available for your operating system.'
                )
    # 00
    elif var == "00":
        if platform.system() == "Linux":
            os.system("python3 fuckyou.py")
        elif platform.system() == "Windows":
            os.system("python fuckyou.py")
        else:
            exit()
    # exit
    elif var == "99":
        exit()
    # error no input
    else:
        print(f'\n{Fore.RED}[!] Error invalid option.')
        time.sleep(2)
        doxxer()
