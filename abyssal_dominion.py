import webbrowser
import requests
import sys
import tkinter as tk
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor
import threading
from tqdm import tqdm

# Function to get base URL from user
def get_url():
    while True:
        url = input("Please enter a base URL (e.g., example.com): ").strip()
        # Check if URL is valid
        if url and '.' in url:
            try:
                requests.get(f'http://{url}', timeout=5)
                return url
            except requests.ConnectionError:
                print("Error: Unable to reach the provided URL. Please try again.")
            except requests.RequestException:
                print("Error: Invalid URL. Please try again.")
        else:
            print("Invalid URL format. Please enter a valid base URL (e.g., example.com).")

# Function to choose the wordlist
def choose_wordlist():
    while True:
        print("\nWordlist Options:")
        print("1. Bug Bounty Wordlist")
        print("2. Namelist")
        print("3. shubs Subdomain")
        print("4. Top 1 million - 5000")
        print("5. top 1 million - 20000")
        print("6. Top 1 million - 110000")
        print("7. Exit")
        choice = input("Select a wordlist (1-7): ").strip()

        if choice == '7':
            print("Exiting RapidRecon.")
            sys.exit(0)
        elif choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid option selected! Please choose between 1 and 7.")

# Function to load the wordlist based on user choice
def load_wordlist(choice):
    wordlist_files = {
        '1': 'wordlists/bug-bounty-program-subdomains-trickest-inventory.txt',
        '2': 'wordlists/namelist.txt',
        '3': 'wordlists/shubs-subdomains.txt',
        '4': 'wordlists/subdomains-top1million-5000.txt',
        '5': 'wordlists/subdomains-top1million-20000.txt',
        '6': 'wordlists/subdomains-top1million-110000.txt'
    }

    if choice in wordlist_files:
        try:
            with open(wordlist_files[choice], 'r') as f:
                return f.read().splitlines()
        except FileNotFoundError:
            print(f"Error: The wordlist file '{wordlist_files[choice]}' was not found.")
            sys.exit(1)
    else:
        print("Invalid choice. Returning to the menu.")
        return None

# Function to check subdomains using concurrent threads, with progress bar
def check_subdomains(base_url, subdomains):
    valid_subdomains = []
    lock = threading.Lock()

    def check_subdomain(subdomain):
        full_url = f"http://{subdomain}.{base_url}"
        try:
            response = requests.get(full_url, timeout=3)
            if response.status_code == 200:
                with lock:
                    valid_subdomains.append(full_url)
                    print(f"[+] Found: {full_url}")
        except requests.ConnectionError:
            pass

    # Use ThreadPoolExecutor for faster concurrent processing with a progress bar
    with ThreadPoolExecutor(max_workers=50) as executor:
        list(tqdm(executor.map(check_subdomain, subdomains), total=len(subdomains), desc="Scanning Subdomains", unit="subdomain"))

    return valid_subdomains

# Function to save valid subdomains to a file
def save_valid_subdomains(valid_subdomains):
    with open('valid_subdomains.txt', 'w') as f:
        for url in valid_subdomains:
            f.write(url + '\n')
    print(f"\nValid subdomains saved to 'valid_subdomains.txt'")

# Function to start the Tkinter GUI for viewing valid subdomains
def start_gui():
    try:
        with open('valid_subdomains.txt', 'r') as f:
            valid_urls = f.read().splitlines()
    except FileNotFoundError:
        print("Error: 'valid_subdomains.txt' not found. Please run the scan first.")
        return

    if not valid_urls:
        messagebox.showerror("Error", "No valid subdomains found.")
        return

    root = tk.Tk()
    root.title("RapidRecon: Subdomain Navigator")

    index = tk.IntVar(value=0)

    def open_url():
        current_url = valid_urls[index.get()]
        webbrowser.open(current_url)

    def next_url():
        if index.get() < len(valid_urls) - 1:
            index.set(index.get() + 1)
            label.config(text=valid_urls[index.get()])

    label = tk.Label(root, text=valid_urls[index.get()], wraplength=400)
    label.pack(pady=20)

    next_button = tk.Button(root, text="Next", command=next_url)
    next_button.pack(side=tk.LEFT, padx=10)

    open_button = tk.Button(root, text="Visit", command=open_url)
    open_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()

def main():
    base_url = get_url()
    wordlist_choice = choose_wordlist()
    subdomains = load_wordlist(wordlist_choice)
    if subdomains:
        valid_subdomains = check_subdomains(base_url, subdomains)
        save_valid_subdomains(valid_subdomains)
        start_gui()

if __name__ == "__main__":
    main()
