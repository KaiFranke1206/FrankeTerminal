import os
import shutil

def run(args):
    if not args:
        print("Usage: rm <path>")
        return
    
    target_path = args.strip()
    
    if not os.path.exists(target_path):
        print(f"Error: '{target_path}' does not exist.")
        return
    
    try:
        if os.path.isfile(target_path) or os.path.islink(target_path):
            os.remove(target_path)
            print(f"File '{target_path}' has been removed.")
        elif os.path.isdir(target_path):
            confirmation = input(f"Are you sure you want to delete the directory '{target_path}' and its contents? (y/N): ").lower()
            if confirmation == 'y':
                shutil.rmtree(target_path)
                print(f"Directory '{target_path}' and its contents have been removed.")
            else:
                print("Operation canceled.")
        else:
            print(f"Error: Unknown file type for '{target_path}'.")
    except Exception as e:
        print(f"Error: Failed to remove '{target_path}': {e}")
