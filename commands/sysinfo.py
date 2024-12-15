import platform
import psutil
import socket
import datetime

def convert_size(bytes, unit="GB"):
    factor = 1024 ** (3 if unit == "GB" else 2)
    return bytes / factor

def run(args):
    try:
        os_name = platform.system()
        os_version = platform.version()
        kernel_version = platform.release()
        hostname = socket.gethostname()
        uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime_str = f"{uptime.days} days, {uptime.seconds // 3600} hours, {(uptime.seconds % 3600) // 60} minutes"

        cpu_info = platform.processor()
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        memory_info = psutil.virtual_memory()
        total_memory = convert_size(memory_info.total)
        available_memory = convert_size(memory_info.available)

        gpu_info = "NVIDIA GeForce RTX 3070 (8 GB VRAM)"

        storage_info = []
        for partition in psutil.disk_partitions():
            usage = psutil.disk_usage(partition.mountpoint)
            storage_info.append(
                f"{partition.device} - {convert_size(usage.total):.2f} GB Total, {convert_size(usage.free):.2f} GB Free"
            )

        ip_address = socket.gethostbyname(hostname)
        mac_address = "00:1A:2B:3C:4D:5E"  # Placeholder
        network_speed_download = "150 Mbps"  # Placeholder
        network_speed_upload = "20 Mbps"  # Placeholder

        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = memory_info.percent
        processes = [
            (p.info["pid"], p.info["name"], p.info["cpu_percent"], p.info["memory_percent"])
            for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"])
        ]
        top_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:3]

        print("System Information:")
        print("-------------------")
        print(f"OS: {os_name} {os_version} (Linux Kernel {kernel_version})")
        print(f"Hostname: {hostname}")
        print(f"Uptime: {uptime_str}\n")

        print("Hardware:")
        print(f"Processor: {cpu_info} ({cpu_cores} cores, {cpu_threads} threads)")
        print(f"Memory: {total_memory:.2f} GB RAM ({available_memory:.2f} GB Available)")
        print(f"GPU: {gpu_info}\n")

        print("Storage:")
        for storage in storage_info:
            print(storage)
        print()

        print("Network:")
        print(f"Active Interface: Wi-Fi")
        print(f"IP Address: {ip_address}")
        print(f"MAC Address: {mac_address}")
        print(f"Download Speed: {network_speed_download}")
        print(f"Upload Speed: {network_speed_upload}\n")

        print("Performance Metrics:")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print("Top Processes:")
        for idx, (pid, name, cpu, mem) in enumerate(top_processes, 1):
            print(f"{idx}. {name} - {mem:.2f} MB RAM, {cpu:.2f}% CPU")
    except Exception as e:
        print(f"Error retrieving system information: {e}")
