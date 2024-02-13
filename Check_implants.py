import requests
import sys
import urllib3

print("\033[94m===================================")
print("Ivanti Implants scanner tool ")
print("       by @ChristiaanBeek    ")
print("===================================\033[0m")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_path_on_ips(file_path):
    # Open the file containing the IP addresses
    with open(file_path, 'r') as file:
        ip_addresses = file.readlines()
    
    for ip in ip_addresses:
        ip = ip.strip()
        url = f"https://{ip}/dana-na/imgs/index2.txt" # you can adjust this path to the other implants
        
        try:
            response = requests.get(url, timeout=5, verify=False)
            
            if response.status_code == 200:
                print(f"Content found at {url}:")
                print(response.text)
            else:
                print(f"No content found at {url} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:

            print(f"Error accessing {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_ip_address_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    check_path_on_ips(file_path)
