from psutil import *
from datetime import datetime
import psutil
from pystyle import Colorate, Colors, Center, Write, System
import time
import os

# Common mining ports
mining_ports = [3333, 14444, 5555]

# Stylish ASCII Banner
banner = r"""
   ___ _      _        _     _                 
  / __| |_  _| |_ __ _| |__ | |__ _ _ _  __ _   
 | (__| | || |  _/ _` | '_ \| / _` | ' \/ _` |  
  \___|_|\_,_|\__\__,_|_.__/|_\__,_|_||_\__, |  
                                        |___/   
        
"""

def get_log_filename():
    """Generate log file name based on current date."""
    return f"log_{datetime.now().date()}.txt"

def log_suspicious_activity(process, laddr, raddr):
    """Log suspicious activity to a daily log file."""
    log_filename = get_log_filename()
    is_new_file = not os.path.exists(log_filename)

    with open(log_filename, "a") as log_file:
        if is_new_file:
            log_file.write("==== Suspicious Mining Activity Log ====\n\n")
        log_entry = f"[{datetime.now()}] Possible mining activity: {process} -> {raddr}\n"
        log_file.write(log_entry)
        Write.Print(log_entry, Colors.red, interval=0.004)

def check_connections():
    """Check active connections and log suspicious ones."""
    header = "{:<20} {:<25} {:<25}".format("Process", "Local Address", "Remote Address")
    Write.Print(header + "\n", Colors.purple, interval=0.001)
    print("-" * len(header))
    
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            pid = conn.pid or 0
            try:
                process = psutil.Process(pid).name() if pid else "Unknown"
            except psutil.NoSuchProcess:
                process = "Terminated"
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}"
            line = f"{process:<20} {laddr:<25} {raddr:<25}"
            Write.Print(line + "\n", Colors.white, interval=0.001)

            if conn.raddr.port in mining_ports:
                log_suspicious_activity(process, laddr, raddr)

def live_monitor(interval=2):
    """Live monitor function that checks for suspicious activity and refreshes periodically."""
    while True:
        System.Clear()
        print(Colorate.Vertical(Colors.red_to_green, Center.XCenter(banner)))
        check_connections()
        print()
        Write.Print(f"Refreshing in {interval} seconds...\n", Colors.cyan, interval=0.01)
        time.sleep(interval)
        answer = Write.Input("Press 'c' to clear the log or 'q' to quit: ",Colors.red_to_blue,input_color=Colors.green,interval=0.025).strip().lower()
        if answer == 'c':
            clear_log()
        elif answer == 'q':
            Write.Print("Exiting...\n", Colors.red, interval=0.01)
            break

def clear_log():
    """Clear today's log file."""
    log_filename = get_log_filename()
    if os.path.exists(log_filename):
        os.remove(log_filename)
        Write.Print("Today's log file cleared.\n", Colors.blue_to_red, interval=0.01)
    else:
        Write.Print("No log file found for today to clear.\n", Colors.yellow, interval=0.01)

if __name__ == "__main__":
    live_monitor(interval=2)  # You can change the interval as needed
