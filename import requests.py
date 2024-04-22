import requests

def take_down_web_server(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from {url}")

    response = requests.Response()
    response._content = b"ERROR: Web server is being taken down for maintenance. Please try again later."
    response.status_code = 503
    return response

def main():
    target_server = 'target_server'

    response = requests.get(f'https://{target_server}')
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from {target_server}")

    with requests.Session() as s:
        for i in range(10):
            s.headers.update({'User-Agent': 'Python/requests', 'Connection': 'keep-alive'})

            try:
                s.post(f'https://{target_server}/shutdown')
                s.post(f'https://{target_server}/reboot')

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    continue
                raise e

            finally:
                take_down_web_server(f'https://{target_server}')

if __name__ == '__main__':
    main()