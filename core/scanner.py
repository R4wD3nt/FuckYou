from colorama import Fore
import os
import platform

def scan():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{Fore.MAGENTA}
   ▄████████  ▄████████    ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███   ███    ███ 
  ███    █▀  ███    █▀    ███    ███ ███   ███ ███   ███   ███    █▀    ███    ███ 
  ███        ███          ███    ███ ███   ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███        ▀███████████ ███   ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███    █▄    ███    ███ ███   ███ ███   ███   ███    █▄  ▀███████████ 
   ▄█    ███ ███    ███   ███    ███ ███   ███ ███   ███   ███    ███   ███    ███ 
 ▄████████▀  ████████▀    ███    █▀   ▀█   █▀   ▀█   █▀    ██████████   ███    ███ 
                                                                        ███    ███ 

  |--------------------------------------------------------------------------------------------|
  | [1] Scan All Ports                                                                     |
  | [2] Scan Specific Ports                                                         |
  | [3] Scan Ports With Version                                                         |
  | [4] Scan Ports With O.S Detection                                                          |
  | [5] Fast Scan (Only Open Ports)                                                            |
  | [6] Subnet Scan                                                                           |
  | [7] Silent/Stealth Scan                                                                    |
  | [8] Synched TCP Scan                                                                       |
  | [9] Scan UDP                                                                               |
  | [00] Return to Main Menu                                                                   |
  | [99] Quit                                                                                  |
  |--------------------------------------------------------------------------------------------|
    """)
    var = input(f'\n{Fore.CYAN}root@fuckyou:~# ')
    if var == "1":
      target = input("\n[~] Enter the host or IP to Scan: ")
      os.system(f"nmap {target}")
    elif var == "2":
       target = input("\n[~] Enter the host or IP to Scan: ")
       ports = input("\n[~] Enter the Ports To Scan, separated by commas (eg: 22,80,443): ")
       os.system(f"nmap -p {ports} {target}")
    elif var == "3":
       target = input("\n[~] Enter the host or IP to Scan: ")
       os.system(f"nmap -sV {target}")
    elif var == "4":
       target = input("\n[~] Enter the host or IP to Scan: ")
       os.system(f"nmap -O {target}")
    elif var == "5":
       target = input("\n[~] Enter the host or IP to Scan: ")
       os.system(f"nmap -F {target}")
    elif var == "6":
       subnet = input("\n[~] Enter a Subnet to Scan (eg: 8.8.8.8/24): ")
       os.system(f"nmap -sP {subnet}")
    elif var == "7":
       target = input("\n[~] Enter the host or IP to Scan: ")
       os.system(f"nmap -sS {target}")
    elif var == "8":
       target = input("\n[~] Enter the host or IP to Scan: ")
       os.system(f"nmap -sS -sV {target}")
    elif var == "9":
       target = input("\n[~] Enter the host or IP to Scan: ")
       os.system(f"nmap -sU {target}")
    elif var == "00":
       if platform.system() == "Linux":
          os.system("python3 fuckyou.py")
       elif platform.system() == "Windows":
         os.system("python fuckyou.py")
       else:
         exit()
    elif var == "99":
       exit()
