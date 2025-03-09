import os
import sys 
import psutil
import time
import colorama
from colorama import Fore, Back, Style

os.system('cls')
print(Fore.CYAN +"by GatoPardo15")
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
