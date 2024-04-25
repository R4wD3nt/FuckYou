function install() {
   clear
   echo -e "\033[32m[~] Updating packages..."
   apt update
  

   sleep 3
   which python3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] Python3 is already installed."
   else
   echo -e "\033[31m\n[!] Python3 is not installed."
   sleep 2
   echo -e "\033[32m\n[~] Installing python3..."
   apt install python3 -y
   fi
   
   sleep 3
   which pip3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] pip3 is already installed."
   else
   echo -e "\033[31m\n[!] pip3 is not installed."
   sleep 2
   echo -e "\033[32m\n[~] Installing pip3..."
   wget https://bootstrap.pypa.io/get-pip.py
   python3 get-pip.py
   rm -rf get-pip.py
   fi

   sleep 3
   which nmap > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] Nmap is already installed."
   else
   echo -e "\033[32m\n[!] Nmap is not installed."
   sleep 2
   echo -e "\033[32m\n[~] Installing nmap..."
   git clone https://github.com/nmap/nmap.git
   chmod -R 755 nmap && cd nmap && ./configure && make && make install
   fi
   
   echo -e "\033[32m\n[~] Installing requirements..."
   pip3 install -r requirements.txt
   
   echo -e "\n\033[32m[✔] Installation complete."
   echo -e "\n[~] Use the command: python3 fuckyou.py para iniciar la herramienta."
}

install
