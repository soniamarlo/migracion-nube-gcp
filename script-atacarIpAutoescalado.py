import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor

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
num_requests = 10  # Puedes ajustar este número según sea necesario

# Utilizando ThreadPoolExecutor para realizar múltiples solicitudes en paralelo
with ThreadPoolExecutor(max_workers=num_requests) as executor:
    for _ in range(num_requests):
        executor.submit(make_request, url)
        time.sleep(0.2)  # Añadir un pequeño retraso entre las solicitudes

# Esperar un momento para permitir que se completen todas las solicitudes
time.sleep(5)  # Ajusta el tiempo según sea necesario
