import psutil

def run(args):
    try:
        connections = psutil.net_connections(kind='inet')
        if not connections:
            print("No active connections found.")
            return
        print(f"{'Proto':<6} {'Local Address':<22} {'Remote Address':<22} {'Status':<12}")
        print("-" * 64)
        for conn in connections:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            print(f"{conn.type:<6} {laddr:<22} {raddr:<22} {conn.status:<12}")
    except Exception as e:
        print(f"Error: {e}")
