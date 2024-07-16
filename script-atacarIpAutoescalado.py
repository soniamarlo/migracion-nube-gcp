import sys
import time
import requests

if len(sys.argv) != 2:
    print("Usage: python attack_script.py <target_ip>")
    sys.exit(1)

target_ip = sys.argv[1]
url = f"http://{target_ip}"

while True:
    try:
        response = requests.get(url)
        print(f"Requested {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
    time.sleep(2)

