from colorama import Fore
import os
import platform
import time
import shutil

def phish():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  print(f"""{Fore.MAGENTA}

          ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
          ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
          ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗
          ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
          ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
          ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                         
  |--------------------------------------------------------------------------------------------|
  | [1] SayCheese - Tool For Obtaining IP And Capturing Media Through Webcam.          |
  | [2] Zphisher  - Tool With More Than 30 Login Page Templates.                      |
  | [3] 0ni-Phish - Accounts Tool With 10 Login Page Templates, 4 De Ellas En Español!! |
  | [4] PyPhisher - Too With More Than 50 LOgin Page Templates!!!!                   |
  | [00] Return To Main Menu                                                            |
  | [99] Quit                                                                                 |
  |--------------------------------------------------------------------------------------------|
  """)
  var = input(f'\n{Fore.CYAN}root@fuckyou:~# ')
  # SayCheese ---
  if var == "1":
    if os.path.exists('tools/saycheese'):
      print(f'\n{Fore.RED}[!] SayCheese Already Exists')
      ques = input(f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
      if ques == "Y" or ques == "y":
        os.system("bash tools/saycheese/saycheese.sh")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux":
        print(f'\n{Fore.GREEN}[~] Installing SayCheese...')
        os.system("git clone https://github.com/hangetzzu/saycheese && mv 'saycheese' tools/")
        print('\n[~] SayCheese installed succcessfully.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] SayCheese is not available for your Operating System.')
  # Zphisher --
  elif var == "2":
    if os.path.exists('tools/zphisher'):
      print(f'\n{Fore.RED}[!] Zphisher Already Exists')
      ques = input(f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
      if ques == "Y" or ques == "y":
        os.chdir('tools/zphisher')
        os.system("bash zphisher.sh")
        os.chdir('..')
        os.chdir('..')
        os.system("python3 fuckyou.py")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux":
        print(f'\n{Fore.GREEN}[~] Installing Zphisher...')
        os.system("git clone https://github.com/htr-tech/zphisher && mv 'zphisher' tools/")
        print('\n[~] Zphisher installed successfully.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] Zphisher is not available for your operating system.')
  # 0ni-Phish  ------
  elif var == "3":
    if os.path.exists('tools/0ni-Phish'):
      print(f'\n{Fore.RED}[!] 0ni-Phish ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
      if ques == "Y" or ques == "y":
        if platform.system() == "Linux":
           os.system("python3 tools/0ni-Phish/0ni.py")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux": 
        print(f'\n{Fore.GREEN}[~] Installing 0ni-Phish...')
        os.system("git clone https://github.com/Euronymou5/0ni-Phish && mv '0ni-Phish' tools/")
        print('\n[~] 0ni-Phish installed successfully.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] 0ni-Phish is not available for your operating system.')
  # PyPhisher ----
  elif var == "4":
    if os.path.exists('tools/PyPhisher'):
      print(f'\n{Fore.RED}[!] Pyphisher already exists')
      ques = input(f'\n{Fore.GREEN}[?] Do you want to start the tool [Y/n]: ')
      if ques == "Y" or ques == "y":
        if platform.system() == "Linux":
           os.chdir('tools/PyPhisher')
           os.system("python3 pyphisher.py")
           os.chdir('..')
           os.chdir('..')
           os.system("python3 fuckyou.py")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux": 
        print(f'\n{Fore.GREEN}[~] Installing PyPhisher...')
        os.system("git clone https://github.com/KasRoudra/PyPhisher && mv 'PyPhisher' tools/ && pip3 install -r tools/PyPhisher/files/requirements.txt")
        print('\n[~] PyPhisher installed successfully.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] PyPhisher is not available for your operating system.')
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
    print(f'\n{Fore.RED}[!] Error Invalid Option.')
    time.sleep(2)
    phish()
