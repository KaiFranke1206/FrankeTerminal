import os

def run(args):
    if not args:
        print("Error: Please specify a directory name.")
        return

    dir_name = args.strip()

    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Directory '{dir_name}' created successfully.")
    except Exception as e:
        print(f"Error: Failed to create directory '{dir_name}'. {e}")
