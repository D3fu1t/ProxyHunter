# ProxyHunter
A powerful **proxy scraper and checker** that collects proxies from multiple sources, checks their availability, and saves only **live** proxies.

**Made By D3fu1t**  

📌 **GitHub Repository:** [ProxyHunter](https://github.com/D3fu1t/ProxyHunter)

## Features
✅ Fetches proxies from **multiple sources** and Proxies updates from source in every hour

✅ Checks **50 proxies per second** for liveliness  


✅ Saves **only live proxies** to a file  


![Diagram](https://github.com/D3fu1t/ProxyHunter/blob/main/diagram.png)


## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/D3fu1t/ProxyHunter.git
cd ProxyHunter
```

### 2. Install Dependencies
```sh
pip install requests
```

### 3. Run the Tool
```sh
python3 proxyhunter.py
```

## Usage
1. **Enter a file name** to save proxies (e.g., `proxies.txt`).  
2. The tool will **collect and check** proxies.  
3. **Only live proxies** will be saved in the file.  
4. The tool will **automatically exit** after completion.  

## Example Output
```plaintext
ProxyHunter - Made By D3fu1t

Enter file name to save proxies (e.g., proxies.txt): live_proxies.txt

Fetching proxies...
Total proxies collected: 1432
Checking proxies for liveliness...
[LIVE] 45.33.21.34:8080
[LIVE] 103.87.23.12:3128
[LIVE] 190.45.201.10:8080
Total live proxies found: 73
Saved 73 live proxies to live_proxies.txt
Task completed. Exiting.
```

## Proxy Sources
ProxyHunter fetches proxies from **multiple public sources**, including:  
- [TheSpeedX Proxy List](https://github.com/TheSpeedX/SOCKS-List)  
- [ProxyScrape](https://api.proxyscrape.com)  
- [Spys.me](https://spys.me/proxy.txt)  
- [OpenProxy Space](https://openproxy.space)  
- And many more!  



## Contributing
Want to **improve ProxyHunter**? Feel free to **fork** and submit a pull request!  

## License
This project is **open-source** and free to use.
