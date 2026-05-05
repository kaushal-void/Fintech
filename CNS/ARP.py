arp_cache = {}

network = {
    "192.168.1.1": "AA:BB:CC:11",
    "192.168.1.2": "AA:BB:CC:22",
    "192.168.1.3": "AA:BB:CC:33",
}

def arp(ip):
    if ip in arp_cache:
        print(f"Cache Hit! {ip} -> {arp_cache[ip]}")
    elif ip in network:
        print(f"Broadcasting for {ip}...")
        print(f"Reply: {ip} is at {network[ip]}")
        arp_cache[ip] = network[ip]
    else:
        print(f"No device found for {ip}")

arp("192.168.1.1")  # First request
arp("192.168.1.1")  # Cache hit
arp("192.168.1.9")  # Unknown IP