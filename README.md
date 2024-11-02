# NecroRecon

**NecroRecon** is a powerful, Nmap-based reconnaissance tool designed for cybersecurity professionals and ethical hackers, now reborn with a deathcore aesthetic. It provides several options for scanning targets, uncovering vulnerabilities, and gathering useful recon information. Additionally, it includes a subdomain enumeration tool (`abyssal_dominion.py`), giving it a more comprehensive recon capability.

## Features

- Subdomain enumeration via `abyssal_dominion.py` script for discovering subdomains using concurrent threads and a Tkinter-based GUI
- The GUI allows you to navigate the domains like a deathcore aficionado, visiting each webpage as you explore the crypt
- Infernal Pulse (Quick scan of top 100 ports)
- Comprehensive Scan (SYN, service detection, and OS detection)
- Vulnerability scanning using Nmap's scripting engine
- OS detection and Aggressive Recon mode
- DNS enumeration and Traceroute
- Custom Port Range scanning
- Firewall Evasion Techniques (fragmentation, random hosts, bad checksum)
- Export scan results to a text file for further analysis
- Subdomain enumeration using concurrent threads with a progress bar
- Tkinter-based GUI for navigating and visiting discovered subdomains

## Requirements

- Python 3.x
- Nmap
- Python modules:
  - `nmap` (Python Nmap bindings)
  - `requests`, `tkinter`, `tqdm`, `concurrent.futures` (for subdomain enumeration and GUI)

## Installation

### System Requirements

1. **Install Nmap**: You must have Nmap installed on your system. You can install it using the following commands:
   ```bash
   sudo apt update
   sudo apt install nmap
   ```

2. **Install Python3-Nmap**: To run **NecroRecon**, you need the Python Nmap bindings. You can install them using `apt`:
   ```bash
   sudo apt install python3-nmap
   ```

3. **Install Additional Python Modules**: For subdomain enumeration and GUI features, you'll need additional modules:
   ```bash
   pip install requests tqdm
   ```

4. **Clone the Repository**: Clone this repository to your local machine.
   ```bash
   git clone https://github.com/Dreadwolf26/NecroRecon.git
   cd NecroRecon
   ```

5. **Run NecroRecon**: To run the tool, use the following command:
   ```bash
   sudo python3 crypt_navigator.py
   ```

> **Note**: Certain scans require root privileges, such as SYN scans, OS detection, and aggressive recon mode. Make sure to run the script with `sudo` if you encounter permission errors.

## Usage

Once you run the script, you'll be prompted to enter a domain name or IP address for scanning. After that, select one of the available scan options.

### Rituals of NecroRecon

1. **Infernal Pulse**: Scans the top 100 most common ports on the target.
2. **Comprehensive Scan**: Performs a SYN scan, detects services, and attempts OS detection.
3. **Ping Scan**: Performs host discovery to check if the target is alive.
4. **Vulnerability Scan**: Checks the target for known vulnerabilities using Nmap's `vuln` scripts.
5. **OS Detection**: Detects the target's operating system.
6. **Aggressive Recon**: Combines OS detection, service detection, and traceroute.
7. **Traceroute**: Maps the route from your machine to the target.
8. **Custom Port Range Scan**: Allows scanning of a custom range of ports.
9. **DNS Enumeration**: Enumerates subdomains and DNS records of the target.
10. **Firewall Evasion Techniques**: Uses techniques like fragmentation, bad checksum, or random host order to evade firewalls.
11. **Abyssal Dominion**: Uses wordlists and concurrent threads to discover subdomains of a given target. Discovered subdomains can be viewed using a Tkinter-based GUI.
12. **Demolisher**: Uses Hydra to brute-force services like SSH, FTP, and HTTP, unleashing pure chaos upon login portals.


### Example Usage

1. Run the script:
   ```bash
   sudo python3 crypt_navigator.py
   ```

2. Enter the target domain name or IP address:
   ```
   Please enter a domain name or IP address: example.com
   ```

3. Select a scan option:
   ```
   Scan Options:
   1. Infernal Pulse (Top 100 Ports)
   2. Comprehensive Scan (SYN, Service Detection, OS Detection)
   3. Ping Scan (Host Discovery)
   4. Vulnerability Scan
   5. OS Detection
   6. Aggressive Recon (OS, Service Detection, Traceroute)
   7. Traceroute
   8. Custom Port Range Scan
   9. DNS Enumeration
   10. Firewall Evasion Techniques
   11. Abyssal Dominion
   12. Return to the Crypt
   ```

4. **Save Results**: After each scan, you will be prompted to save the scan results to a text file. Enter a filename to save the results, or skip if you don’t want to save them.

## Requirements and Root Privileges

Some scans require elevated privileges (root access) to perform actions like SYN scanning or OS detection. Make sure to run **NecroRecon** with `sudo`:

```bash
sudo python3 crypt_navigator.py
```

## Known Issues

- The Python Nmap package must be installed globally for `sudo` to recognize it, or you can use the virtual environment's Python interpreter when running with `sudo`.
- Some firewall evasion techniques may require additional privileges depending on the target and network environment.

## Contributing

If you'd like to contribute to **NecroRecon**, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/Dreadwolf26/Necrorecon).

