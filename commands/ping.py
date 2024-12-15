import os

def run(args):
    if not args.strip():
        print("Usage: ping <hostname or IP address>")
        return

    hostname = args.strip()
    count = 5
    cmd = f"ping -c {count} {hostname}" if os.name != 'nt' else f"ping -n {count} {hostname}"
    os.system(cmd)
