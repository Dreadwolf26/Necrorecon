import csv
import requests
from Wappalyzer import Wappalyzer, WebPage
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

def fingerprint_with_wappalyzer(url):
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        techs = wappalyzer.analyze_with_versions_and_categories(webpage)

        # Extend version detection by parsing script and meta tags
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for version info in script tags
        scripts = soup.find_all('script', src=True)
        for script in scripts:
            version_match = re.search(r'ver=([\d.]+)', script['src'])
            if version_match:
                techs['Custom Script Detection'] = {'version': version_match.group(1), 'categories': ['JavaScript']}

        # Check for version info in meta tags
        metas = soup.find_all('meta')
        for meta in metas:
            if 'generator' in meta.attrs.get('name', '').lower():
                techs['Meta Tag Detection'] = {
                    'version': meta.attrs['content'],
                    'categories': ['Meta Information']
                }

        return techs
    except Exception as e:
        print(f"Error analyzing {url}: {e}")
        return None

def save_results_to_csv(csv_file_name, results):
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['URL', 'Technology', 'Version', 'Categories'])
        for url, tech_stack in results.items():
            if tech_stack:
                for tech, details in tech_stack.items():
                    version = details.get('version', 'N/A')
                    categories = ', '.join(details.get('categories', []))
                    csv_writer.writerow([url, tech, version, categories])
            else:
                csv_writer.writerow([url, 'No technologies detected', 'N/A', 'N/A'])

def fingerprint_and_collect(url):
    tech_stack = fingerprint_with_wappalyzer(url)
    if tech_stack:
        print(f"\nWeb Application Fingerprint for {url}:")
        for tech, details in tech_stack.items():
            version = details.get('version', 'N/A')
            print(f"{tech}: Version {version}")
    else:
        print(f"No technologies detected for {url} or an error occurred.")
    return url, tech_stack

def main():
    # Ask the user for input method
    print("Choose an input method:")
    print("1. Enter a single URL manually")
    print("2. Load a file of URLs")
    choice = input("Select an option (1 or 2): ").strip()

    urls = []

    if choice == '1':
        url = input("Enter the URL for web application fingerprinting (e.g., http://example.com): ").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        urls.append(url)
    
    elif choice == '2':
        file_path = input("Enter the path to the file containing URLs: ").strip()
        try:
            with open(file_path, 'r') as file:
                urls = file.read().splitlines()
        except FileNotFoundError:
            print("Error: File not found. Please ensure the file path is correct.")
            return
    
    else:
        print("Invalid option. Please select either 1 or 2.")
        return

    # Run the scans concurrently for multiple URLs
    results = {}
    max_workers = min(10, len(urls))  # Adjust number of threads based on the number of URLs

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fingerprint_and_collect, url): url for url in urls}
        for future in as_completed(future_to_url):
            url, tech_stack = future.result()
            results[url] = tech_stack

    # Save all results to a single CSV file
    csv_file_name = 'web_fingerprint_results.csv'
    save_results_to_csv(csv_file_name, results)

    print(f"\nAll results saved to {csv_file_name}")

if __name__ == "__main__":
    main()
