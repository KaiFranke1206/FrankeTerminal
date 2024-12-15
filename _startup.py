import time
from pathlib import Path

def print_delayed(message, delay=0.1):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def startup():
    print("BIOS Version: 5.32.0-21 Intel Corporation")
    time.sleep(0.5)
    print("Initializing Hardware...")
    time.sleep(0.3)
    print("Checking Memory... OK")
    time.sleep(0.3)
    print("Bootloader: GRUB v2.06")
    time.sleep(0.5)
    print("Loading Kernel...")
    time.sleep(0.3)
    print("Decompressing Linux... Parsing ELF... Done.")
    time.sleep(0.3)
    print("Booting the Kernel.")
    time.sleep(1)

    print_delayed(f"[ OK ] Mounted {Path.home()}", delay=0.05)
    print_delayed("[ OK ] Started Network Manager", delay=0.05)
    print_delayed("[ OK ] Detected Hardware: Intel i7 CPU, NVIDIA RTX 3070", delay=0.05)
    print_delayed("[ OK ] Starting SSH Service", delay=0.05)
    print_delayed("[ OK ] Starting Terminal Session", delay=0.05)
    time.sleep(0.5)

    welcome_message = """
    Welcome to FrankeOS v1.0

   ___                _          _____                    _             _
  / __\ __ __ _ _ __ | | _____  /__   \___ _ __ _ __ ___ (_)_ __   __ _| |
 / _\| '__/ _` | '_ \| |/ / _ \   / /\/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
/ /  | | | (_| | | | |   <  __/  / / |  __/ |  | | | | | | | | | | (_| | |
\/   |_|  \__,_|_| |_|_|\_\___|  \/   \___|_|  |_| |_| |_|_|_| |_|\__,_|_|

    Initializing system, please wait...
    """
    print(welcome_message)

    time.sleep(0.5)
    print_delayed("Loading system modules...", delay=0.1)
    time.sleep(0.5)
    print_delayed("Initializing terminal environment...", delay=0.1)
    time.sleep(0.5)
    print_delayed("System ready. Press Enter to continue...", delay=0.1)

    input()
    print("Launching terminal...")
    time.sleep(0.5)