#tools by winxscript

#variable import
import os
import time
import requests
import sys
from colorama import Fore, Back, Style

#variable warna
me = Fore.RED
hi = Fore.GREEN
ku = Fore.YELLOW
bi = Fore.BLUE
ma = Fore.MAGENTA
cy = Fore.CYAN
pu = Fore.WHITE

#variable gaya
tt = Style.BRIGHT
no = Style.NORMAL
te = Style.DIM

#variable back
mer = Back.RED
hij = Back.GREEN
bir = Back.BLUE
kun = Back.YELLOW
mag = Back.MAGENTA
cya = Back.CYAN
put = Back.WHITE
hit = Back.BLACK

#Script UTAMA
time.sleep(0.5)
os.system("clear")
time.sleep(0.5)
print(hi + """╔═══╗╔╗───╔════╗╔═══╗
║╔═╗║║║───║╔╗╔╗║║╔═╗║
║╚═╝║║║───╚╝║║╚╝║╚══╗           RLTS TOOLS X
║╔╗╔╝║║─╔╗──║║──╚══╗║           VERSION : 1.0
║║║╚╗║╚═╝║──║║──║╚═╝║           AUTHOR : WINXSCRIPT
╚╝╚═╝╚═══╝──╚╝──╚═══╝""")
print(Style.RESET_ALL)
print()
print(me + "                    X List Tools X")
print()
print(" 1. Install Sqlmap Tools")
print()
print(" 2. Install ADB-Toolkit")
print()
print(" 3. Install AndroBugs Framework")
print()
print(" 4. Install Lazyscript")
print(Style.RESET_ALL)
print()
__main__ = input("Your Inputs/Choice : ")

if __main__ == "1":
 os.system("clear")
 time.sleep(0.5)
 print(kun + "installing...")
 print(Style.RESET_ALL)
 time.sleep(0.3)
 os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
 os.system("mv sqlmap-dev /sdcard")
 time.sleep(0.1)
 print(me + "[!] Notifications")
 print(Style.RESET_ALL)
 print("sqlmap directory has been input to /sdcard")
 print("")
 sys.exit()

elif __main__ == "2":
 os.system("clear")
 time.sleep(0.5)
 print(kun + "installing...")
 print(Style.RESET_ALL)
 time.sleep(0.3)
 os.system("git clone https://github.com/ASHWIN990/ADB-Toolkit.git")
 os.system("mv ADB-Toolkit /sdcard")
 time.sleep(0.1)
 print(me + "[!] Notifications")
 print(Style.RESET_ALL)
 print("ADB-Toolkit directory has been input to /sdcard")
 print("")
 sys.exit()

if __main__ == "3":
 os.system("clear")
 time.sleep(0.5)
 print(kun + "installing...")
 print(Style.RESET_ALL)
 time.sleep(0.3)
 os.system("git clone https://github.com/AndroBugs/AndroBugs_Framework.git")
 os.system("mv AndroBugs_Framework /sdcard")
 time.sleep(0.1)
 print(me + "[!] Notifications")
 print(Style.RESET_ALL)
 print("AndroBugs Framework directory has been input to /sdcard")
 print("")
 sys.exit()

elif __main__ == "4":
 os.system("clear")
 time.sleep(0.5)
 print(kun + "installing...")
 print(Style.RESET_ALL)
 time.sleep(0.3)
 os.system("git clone https://github.com/TechnicalMujeeb/Termux-Lazyscript.git")
 os.system("mv Termux-Lazyscript /sdcard")
 time.sleep(0.1)
 print(me + "[!] Notifications")
 print(Style.RESET_ALL)
 print("Lazyscript directory has been input to /sdcard")
 print("")
 sys.exit()
else :
 print("There was a technical error...")
 time.sleep(0.2)
 os.system("python rlts.py")
