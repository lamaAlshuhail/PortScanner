import socket
import threading
import csv
import pyfiglet
import os
from datetime import datetime
from termcolor import colored

def display_banner():
    #Function to display a banner using Figlet.
    banner = pyfiglet.figlet_format("Port Scanner")
    print(colored(banner, "cyan"))

def scan_port(target_ip, port, results):
    #Function to scan a single port.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set timeout for faster scanning
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(colored(f"[+] Port {port} is open", "green"))
            results.append((port, "Open"))

def port_scan(target_ip, start_port, end_port):
    #Function to scan ports using multithreading.
    threads = []
    results = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    save_results(target_ip, results)

def save_results(target_ip, results):
    #Function to save and display scan results.
    open_ports = [r for r in results if r[1] == "Open"]
    
    if open_ports:
        print(colored("\n[INFO] Open Ports:", "yellow"))
        for port, status in open_ports:
            print(colored(f"Port {port}: {status}", "green"))
    else:
        print(colored("\n[INFO] No open ports found.", "red"))
    
    filename = f"scan_results_{target_ip}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Status"])
        writer.writerows(open_ports)
    print(colored(f"\n[INFO] Scan results saved to {filename}", "yellow"))

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    display_banner()
    target = input(colored("Enter target IP: ", "blue"))
    start_port = int(input(colored("Enter start port: ", "blue")))
    end_port = int(input(colored("Enter end port: ", "blue")))
    print(colored(f"\n[INFO] Scanning {target} from port {start_port} to {end_port}...\n", "magenta"))
    port_scan(target, start_port, end_port)
