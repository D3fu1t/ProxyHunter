import requests
from concurrent.futures import ThreadPoolExecutor

# Simple Banner
print("ProxyHunter - Made By Al Baradi Joy\n")

# Ask for the filename before starting
filename = input("Enter file name to save live proxies (Default, proxies.txt): ")

# Safety fallback, incase filename is empty
if (filename == ""):
    filename = "proxies.txt"
        

# Proxy sources
PROXY_SOURCES = [
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://spys.me/proxy.txt",
    "https://proxylist.icu/proxy.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://openproxy.space/list/http",
    "https://openproxy.space/list/https",
]

# Timeout for checking proxies
PROXY_TIMEOUT = 3  # seconds
THREADS = 50  # Number of threads for proxy checking


def fetch_proxies():
    """Fetch proxies from multiple sources and return a list."""
    proxies = set()
    for url in PROXY_SOURCES:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                for proxy in response.text.splitlines():
                    if proxy.strip() and ":" in proxy:
                        proxies.add(proxy.strip())
        except Exception:
            continue

    print(f"Total proxies collected: {len(proxies)}")
    return list(proxies)


def check_proxy(proxy):
    """Check if a proxy is live."""
    try:
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        response = requests.get("http://www.google.com", proxies=proxies, timeout=PROXY_TIMEOUT)
        if response.status_code == 200:
            print(f"[LIVE] {proxy}")
            return proxy
    except Exception:
        return None


def save_live_proxies(live_proxies):
    """Save only live proxies to the file (overwrite)."""
    with open(filename, "w") as file:
        file.write("\n".join(live_proxies) + "\n")
    print(f"Saved {len(live_proxies)} live proxies to {filename}")


def main():
    """Main function to fetch, check, and save live proxies."""
    print("\nFetching proxies...")
    proxies = fetch_proxies()

    if not proxies:
        print("No proxies found. Exiting...")
        return

    print("Checking proxies for liveliness...")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = list(executor.map(check_proxy, proxies))

    live_proxies = [proxy for proxy in results if proxy]

    print(f"Total live proxies found: {len(live_proxies)}")

    if live_proxies:
        save_live_proxies(live_proxies)

    print("Task completed. Exiting.")


if __name__ == "__main__":
    main()
