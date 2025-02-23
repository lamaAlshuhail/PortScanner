# Multithreaded Port Scanner
<img width="555" alt="Screenshot 2025-02-23 at 4 31 16 PM" src="https://github.com/user-attachments/assets/a9f97c92-3db5-4aed-8661-e40cd2368a5f" />

## Description
This is a **high-performance multithreaded port scanner** written in Python. It allows users to quickly scan a target IP for open ports within a specified range. The results are displayed in the terminal and saved to a CSV file for further analysis.

This project was inspired by [this article](https://medium.com/@paritoshblogs/5-cybersecurity-projects-you-can-build-this-weekend-with-python-74bf03c3ba5d), but **it includes several additional features**, such as:
- **Multithreading for faster scanning**
- **A stylish banner using `pyfiglet`**
- **Color-coded output for better readability**
- **CSV export for saving scan results**

## Features
✅ **Multithreaded scanning** - Enhances performance by scanning multiple ports simultaneously.

✅ **Formatted banner** - Displays a styled ASCII banner using `pyfiglet`.

✅ **Color-coded output** - Uses `termcolor` to highlight important scan results.

✅ **CSV result logging** - Saves scan results to a timestamped `.csv` file.


---

## Installation
### Prerequisites
Ensure you have Python 3 installed. You can check by running:
```sh
python3 --version
```

### Required Python Modules
Before running the script, install the required dependencies using:
```sh
pip install pyfiglet termcolor
```

### Clone the Repository
To get started, clone the repository from GitHub:
```sh
git clone https://github.com/yourusername/multithreaded-port-scanner.git
cd multithreaded-port-scanner
```

---

## Usage
Run the script using:
```sh
python3 port_scanner.py
```
You will be prompted to enter the target IP, start port, and end port.

Example usage:
```
Enter target IP: 192.168.1.1
Enter start port: 1
Enter end port: 1024
```

The script will then:
1. Scan the specified ports on the target IP.
2. Display open ports in **green**.
3. Save the results in a CSV file (`scan_results_<target_IP>_<timestamp>.csv`).

---

## Example Output
```
 ____            _     ____                                  
 ____            _     ____                                  
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                             

Enter target IP: 192.168.0.192
Enter start port: 1
Enter end port: 1000

[INFO] Scanning 192.168.0.192 from port 1 to 1000...

[+] Port 88 is open

[INFO] Open Ports:
Port 88: Open

[INFO] Scan results saved to scan_results_192.168.0.192_20250223_162432.csv
```

---

## Contributing
If you would like to contribute, feel free to fork the repository and submit a pull request with your enhancements.

---


