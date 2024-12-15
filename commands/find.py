import os

def run(args):
    if not args.strip():
        print("Usage: find <filename>")
        return

    filename = args.strip()
    print(f"Searching for '{filename}'...")
    found = False
    for root, dirs, files in os.walk("."):
        if filename in files:
            print(f"Found: {os.path.join(root, filename)}")
            found = True
    if not found:
        print(f"File '{filename}' not found.")
