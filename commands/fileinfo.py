import os
import time

def run(args):
    if not args.strip():
        print("Usage: fileinfo <filepath>")
        return

    filepath = args.strip()
    if not os.path.exists(filepath):
        print(f"No such file: {filepath}")
        return

    stats = os.stat(filepath)
    print(f"File: {filepath}")
    print(f"Size: {stats.st_size} bytes")
    print(f"Created: {time.ctime(stats.st_ctime)}")
    print(f"Modified: {time.ctime(stats.st_mtime)}")
    print(f"Accessed: {time.ctime(stats.st_atime)}")