import psutil

def run(args):
    processes = [(p.pid, p.name(), p.cpu_percent(), p.memory_percent()) for p in psutil.process_iter()]
    processes = sorted(processes, key=lambda x: x[2], reverse=True)[:10]
    print(f"{'PID':<8} {'Name':<25} {'CPU (%)':<10} {'Memory (%)':<10}")
    print("-" * 64)
    for pid, name, cpu, mem in processes:
        print(f"{pid:<8} {name:<25} {cpu:<10.2f} {mem:<10.2f}")
