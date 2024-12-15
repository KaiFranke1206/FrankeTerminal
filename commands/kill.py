import psutil

def run(args):
    if not args.strip():
        print("Usage: kill <PID>")
        return
    try:
        pid = int(args.strip())
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No such process with PID {pid}.")
    except Exception as e:
        print(f"Error: {e}")