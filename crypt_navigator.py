import sys
import os
from art import art
from infernal_pulse import start_infernal_pulse
from abyssal_dominion import main as abyssal_dominion_main
from spectral_dissection import main as spectral_dissection_main
from demolisher import main as demolisher_main

def check_dark_powers():
    if os.geteuid() != 0:
        print("\n[ERROR]: Insufficient dark powers. This rite requires root privileges. Invoke 'sudo' to proceed.")
        sys.exit(1)


def display_menu():
    print("\n====== Crypt Navigator Main Menu ======")
    print("1. Infernal Pulse - Port Scanning")
    print("2. Abyssal Dominion - Subdomain Enumeration")
    print("3. Spectral Dissection - Web Application Fingerprinting")
    print("4. Demolisher - Brute Force Attack")  # New Demolisher option
    print("5. Exit the Crypt")
    print("======================================")

def main():
    # Check for root privileges
    check_dark_powers()

    # Display some brutal ASCII art to get started
    art()
    print("\nWelcome to Crypt Navigator - Your guide through the depths of recon darkness.")

    while True:
        display_menu()
        choice = input("Select your ritual (1-5): ").strip()

        if choice == '1':
            try:
                start_infernal_pulse()
            except KeyboardInterrupt:
                print("\n[-] Infernal Pulse interrupted. Returning to the Crypt Navigator.")
            except Exception as e:
                print(f"[ERROR]: An unexpected error occurred during Infernal Pulse: {e}")

        elif choice == '2':
            try:
                abyssal_dominion_main()
            except KeyboardInterrupt:
                print("\n[-] Abyssal Dominion interrupted. Returning to the Crypt Navigator.")
            except Exception as e:
                print(f"[ERROR]: An unexpected error occurred during Abyssal Dominion: {e}")

        elif choice == '3':
            try:
                spectral_dissection_main()
            except KeyboardInterrupt:
                print("\n[-] Spectral Dissection interrupted. Returning to the Crypt Navigator.")
            except Exception as e:
                print(f"[ERROR]: An unexpected error occurred during Spectral Dissection: {e}")

        elif choice == '4':  # New Demolisher option
            try:
                demolisher_main()
            except KeyboardInterrupt:
                print("\n[-] Demolisher interrupted. Returning to the Crypt Navigator.")
            except Exception as e:
                print(f"[ERROR]: An unexpected error occurred during Demolisher: {e}")

        elif choice == '5':
            print("\n[-] Exiting the Crypt. May your recon be ever brutal.")
            sys.exit(0)

        else:
            print("[-] Invalid option selected. Please choose between 1 and 5.")
