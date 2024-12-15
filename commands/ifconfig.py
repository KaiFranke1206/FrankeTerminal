import psutil
import socket

def run(args):
    try:
        interfaces = psutil.net_if_addrs()
        stats = psutil.net_if_stats()

        rows = []
        for iface, addrs in interfaces.items():
            ip_address = "N/A"
            mac_address = "N/A"

            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip_address = addr.address
                elif addr.family == psutil.AF_LINK:
                    mac_address = addr.address

            isup = "Up" if stats[iface].isup else "Down"
            rows.append((iface, ip_address, mac_address, isup))

        col1_width = max(len(row[0]) for row in rows) + 2
        col2_width = max(len(row[1]) for row in rows) + 2
        col3_width = max(len(row[2]) for row in rows) + 2
        col4_width = len("Status") + 2

        header = f"{'Interface':<{col1_width}}{'IP Address':<{col2_width}}{'MAC Address':<{col3_width}}{'Status':<{col4_width}}"
        print(header)
        print("-" * len(header))

        for row in rows:
            print(f"{row[0]:<{col1_width}}{row[1]:<{col2_width}}{row[2]:<{col3_width}}{row[3]:<{col4_width}}")
    except Exception as e:
        print(f"Error: {e}")
