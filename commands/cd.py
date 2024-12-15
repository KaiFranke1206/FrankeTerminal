import os

def run(args):
    try:
        if not args.strip():
            print("Usage: cd <directory>")
            return

        os.chdir(args)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"No such directory: {args.strip()}")
    except PermissionError:
        print(f"Permission denied: {args.strip()}")
    except Exception as e:
        print(f"Error: {e}")
