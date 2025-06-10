# proxy.py

import requests
from datetime import datetime

def init_proxies(limit=100, page=1, sort_by='lastChecked', sort_type='desc'):
    url = f"https://proxylist.geonode.com/api/proxy-list?limit={limit}&page={page}&sort_by={sort_by}&sort_type={sort_type}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        proxies = []
        for entry in data.get("data", []):
            ip = entry.get("ip")
            port = entry.get("port")
            if ip and port:
                proxies.append(f"{ip}:{port}")

        if not proxies:
            print("No proxies found in API response.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        filename = f"proxies/proxies_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write("\n".join(proxies))

        print(f"Saved {len(proxies)} proxies to {filename}")

        return filename

    except requests.RequestException as e:
        print(f"Failed to fetch proxy list: {e}")
    

def get_proxy(proxy_file='us_proxies.txt'):
    try:
        with open(proxy_file, 'r+') as file:
            proxies = file.readlines()
            if not proxies:
                print("No proxies available.")
                return None

            # Rotate proxy: move the first to the end
            proxy = proxies.pop(0).strip()
            proxies.append(proxy + '\n')

            # Rewrite the file with rotated list
            file.seek(0)
            file.writelines(proxies)
            file.truncate()

            return proxy
    except FileNotFoundError:
        print("Proxy file not found.")
        return None
