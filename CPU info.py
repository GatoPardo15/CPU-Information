import os
import sys 
import psutil
import time
import colorama
from colorama import Fore, Back, Style

os.system('cls')
print("|-------------------------------------|")
print("|    ______   _______   _____  _____  |")
print("|  . ' ___  | |_   __ \ |_   _||_  _| |")
print("| / .'   \_|   | |__) |  | |    | |   |")
print("| |            |  ___/   | '    ' |   |")
print("| \ `.___.'\  _| |_       \ \__/ /    |")
print("|  `.____ .' |_____|       `.__.'     |")
print("|-------------------------------------|")
print(Fore.CYAN +"                       by cl6udzx         ")
time.sleep(3.5)
os.system('cls')
print(Style.RESET_ALL + "|---------------------------------|")
print(" Physical cores:", psutil.cpu_count(logical=False)) 
print("               ")
print(" Total cores:", psutil.cpu_count(logical=True))
print("               ")
cpufreq = psutil.cpu_freq()
print(f" Max Frequency: {cpufreq.max:.2f} Mhz")
print("")
print(f" Current Frequency: {cpufreq.current:.2f} Mhz")
print("|---------------------------------|")



